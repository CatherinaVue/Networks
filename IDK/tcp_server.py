import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
print("UDP server is waiting for messages...")
while True:
    client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print("Received from client:", message)
    print("Client address:", client_address)
    reply = "Hello from UDP server"
    server_socket.sendto(reply.encode(), client_address)