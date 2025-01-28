import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

HOST = "127.0.0.1"
PORT = 5000

# running forever
while True:

    # setting up the basic connection
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()

        # accepting a client request
        conn,addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # data sent by client
                data = conn.recv(1024)
                if not data:
                    break
                
                # getting the RSA private key to decrypt the message
                with open("client_key.txt", "rb") as key_file:
                    private_key = serialization.load_pem_private_key(key_file.read(),password=None)
                
                # decrypting the key
                data = private_key.decrypt(data,padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None))
                
                data = str(data)
                # getting the action and true message
                action,message = data.split(':')
                action = int(action[2:])

                # Getting the public key to encrypt my message
                with open("server_key.txt.pub", "rb") as key_file:
                    public_key = serialization.load_ssh_public_key(key_file.read())

                if action == 1:
                    # action = 1 -> echo the message

                    # encrypting the message and sending it back to client
                    message = public_key.encrypt(message.encode(),padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None))
                    conn.sendall(message)

                elif action == 2:
                    # action = 2 -> convert the message to upper, encrypt and send back to client
                    message = message.upper()
                    message = public_key.encrypt(message.encode(),padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None))
                    conn.sendall(message)

                elif action == 3:
                    # action = 3 -> reverse the message, encrypt and send back to client
                    message = message[::-1]
                    message = public_key.encrypt(message.encode(),padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    ))
                    conn.sendall(message)