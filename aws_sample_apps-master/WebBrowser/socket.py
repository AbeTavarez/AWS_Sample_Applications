# ==================================
# Using the Socket library
# ==================================
import socket

# Create socket
browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#
browser_socket.connect(('data.pr4e.org', 80))

# Unicode string gets encoded to utf-8 | cmd holds our bytes
cmd = 'GET http://google.com HTTP/1.0\r\n\r\n'.encode()

# sends our encoded bytes
browser_socket.send(cmd)

while True:
    # data holds our bytes | utf-8 code that we recieve
    data = browser_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='') # decodes the bytes | unicode string

browser_socket.close()

