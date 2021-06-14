import socket

# Create socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

