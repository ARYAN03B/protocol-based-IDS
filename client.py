# client.py

import socket

class IDSClient:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def connect_to_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address, self.server_port))
            print("Connected to server.")
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def send_data(self, data):
        try:
            self.socket.sendall(data.encode())
            print("Data sent to server.")
        except Exception as e:
            print(f"Error sending data to server: {e}")

    def close_connection(self):
        try:
            self.socket.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")

def main():
    # Example usage
    client = IDSClient("localhost", 8888)
    client.connect_to_server()
    client.send_data("Hello, server!")
    client.close_connection()

if __name__ == "__main__":
    main()

