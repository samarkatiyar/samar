import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
       client_socket.connect(('192.168.4.74', 5400))
    except:
       print("Unable to establish connection with Server")
       exit(12)


    while True:
        try:
            message = input("Enter your message: ")
            client_socket.send(message.encode('utf-8'))
        except:
            print("Unable to establish connection with Server")
            exit(12)
if __name__ == "__main__":
    start_client()