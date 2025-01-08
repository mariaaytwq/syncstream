import socket
import threading
import json
import time

class SyncStreamServer:
    def __init__(self, host='0.0.0.0', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
        self.clients = []

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.sendall(message)
            except Exception as e:
                print(f"Error sending message to client: {e}")

    def handle_client(self, client_socket, address):
        print(f"New connection from {address}")
        self.clients.append(client_socket)
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                self.broadcast(data)
        finally:
            client_socket.close()
            self.clients.remove(client_socket)
            print(f"Connection from {address} closed")

    def start(self):
        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()


class SyncStreamClient:
    def __init__(self, server_ip, server_port=12345):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        print(f"Connected to server at {self.server_ip}:{self.server_port}")

    def send_message(self, message):
        self.client_socket.sendall(json.dumps(message).encode('utf-8'))

    def receive_messages(self):
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = json.loads(data.decode('utf-8'))
                print(f"Received message: {message}")
        finally:
            self.client_socket.close()

    def start_receiving(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python syncstream.py [server|client] [server_ip (for client)]")
        sys.exit(1)

    role = sys.argv[1].lower()

    if role == 'server':
        server = SyncStreamServer()
        server.start()
    elif role == 'client':
        if len(sys.argv) < 3:
            print("Usage: python syncstream.py client [server_ip]")
            sys.exit(1)
        server_ip = sys.argv[2]
        client = SyncStreamClient(server_ip)
        client.start_receiving()

        # Example of sending a sync message
        time.sleep(2)  # Wait before sending a test message
        client.send_message({"action": "sync", "timestamp": time.time()})
    else:
        print("Invalid role. Use 'server' or 'client'.")