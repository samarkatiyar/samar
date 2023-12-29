import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()