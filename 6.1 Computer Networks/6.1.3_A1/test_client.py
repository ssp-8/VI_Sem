import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),5000))
s.send("Hello, how are you doing?".encode())
msg = s.recv(1024)
print(msg)