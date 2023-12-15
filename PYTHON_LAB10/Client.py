import socket

HOST="localhost"
PORT=1234

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
f=b"Salut"

while True:
    s.sendall(f)
    break
print("Sending complete!")
s.close()
