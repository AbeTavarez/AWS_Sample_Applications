import socket

# Create socket
browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
browser_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

browser_socket.send(cmd)

while True:
    data = browser_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

browser_socket.close()

