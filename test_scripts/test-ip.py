import socket

print(socket.gethostbyname(socket.gethostname()))

f = open("output.txt", "w")
f.write(socket.gethostbyname(socket.gethostname()))
f.close()
