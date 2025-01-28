import socket
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

HOST = "127.0.0.1"
PORT = 5000

def client(message,action):

    # setting up the connection
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))

        # appending the action to be performed on the message
        message = f"{action}: {message}"

        # getting the public key to encrypt
        with open("client_key.txt.pub", "rb") as key_file:
                public_key = serialization.load_ssh_public_key(key_file.read())
        message = message.encode()

        # encypting
        message = public_key.encrypt(message,padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))  
        # sending the message
        s.sendall(message)

        # receiving the data
        data = s.recv(1024)

        # getting the private key
    with open("server_key.txt", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(),password=None)

        # decrypting the message sent by the server using  private key
    data = private_key.decrypt(data,padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))

    # returning the message
    return str(data)



# Setting up the client

# Task 01,02,03 Setting up the localhost itself as the server
data_received = client("Hello World",1)
print(data_received)
# waiting till the server resumes back

# Task 4
time.sleep(5)
data_received = client("this message is to be in upper case",2)
print(data_received)
time.sleep(5)

# Task 05
data_received = client("This message is to be reversed",3)
print(data_received)