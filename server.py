import socket

host = socket.gethostname()
port = 9876

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print("\nServer started!\n")

connect, addr = sock.accept()

print("Connection established with: ", str(addr))

message = "\nThank you for connecting! " + str(addr)
connect.send(message.encode("ascii"))
connect.close()