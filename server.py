import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        # Receive client message
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'exit':
            break

        print(f"Client {client_address}: {message}")

        # Send response to client
        response = "Message received"
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

start_server()
