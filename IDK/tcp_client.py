import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello from UDP client"
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
data, server_address = client_socket.recvfrom(1024)
print("Server replied:", data.decode())
client_socket.close()