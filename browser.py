

<<<<<<< HEAD
import socket 
"""import requests
=======
import socket
import requests
>>>>>>> 96f93bbdf13191e3ccb716c4f7fcbc49c4f55f42



<<<<<<< HEAD
print(request_html_https("google.com"))
"""
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('google.com', 80))
cmd = 'GET http://www.google.com HTTP/1.0\r\n\r\n'.encode()
=======
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('google.com', 80))
cmd = 'GET http://google.com/ HTTP/1.0\r\n\r\n'.encode()

>>>>>>> 96f93bbdf13191e3ccb716c4f7fcbc49c4f55f42
mysock.send(cmd)


while True:
<<<<<<< HEAD
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=' ')



=======

    data = mysock.recv(512)

    if len(data) < 1:
        break
    print(data.decode(), end=' ')
>>>>>>> 96f93bbdf13191e3ccb716c4f7fcbc49c4f55f42
