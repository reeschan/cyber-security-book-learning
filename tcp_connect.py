import socket

target_host = "0.0.0.0"
target_port = 9998

# create a socket object  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the server
client.connect((target_host, target_port))

# send some data to the server
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# receive data from the server
response = client.recv(4096)

print(response.decode())

# close the connection
client.close()

