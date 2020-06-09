

import socket 
import requests


def request_html_https(url):
    if url[:7] == 'https://':
        return requests.get(url).text
    else:
        url = 'https://' + url
        return requests.get(url).text

print(request_html_https("google.com"))
"""mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('google.com', 80))
cmd = 'GET http://google.com/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
 
    data = mysock.recv(512)
   
    if len(data) < 1:
        break
    print(data.decode(), end=' ')



"""