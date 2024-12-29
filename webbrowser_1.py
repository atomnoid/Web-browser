import socket
import ssl

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context()
secure_socket = context.wrap_socket(my_socket, server_hostname ='cats.com')
secure_socket.connect(('cats.com', 443))

message = 'GET / HTTP/1.1\r\nHOST: cats.com\r\n\r\n'.encode()
secure_socket.send(message)

while True:
    information = secure_socket.recv(512)
    if len(information) < 1:
        break
    final_information = information.decode()
    print(final_information)

secure_socket.close()

