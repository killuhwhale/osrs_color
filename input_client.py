import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


class OsrsInputClient:
    def __init__(self):
        pass

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                user_input = input("Input: ")
                s.sendall(user_input.encode('UTF-8'))


if __name__ == "__main__":
    client = OsrsInputClient()

    client.connect()
