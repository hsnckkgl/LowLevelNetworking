import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(),9876))
msg = sock.recv(1024)
sock.close()
print(msg.decode("ascii"))
