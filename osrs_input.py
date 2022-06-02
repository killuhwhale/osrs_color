import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


class OsrsInput:
    def __init__(self):
        self._q = None

    def start_input(self, queue):
        self._q = queue
        self._run()

    def _run(self):
        # while True:
        #     user_input = input("Input: ")
        #     self._q.put(user_input)
        self.listen_socket()

    def listen_socket(self):
        '''
        AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP,

        s.bind((HOST, PORT))
        If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        conn, addr = s.accept()
                    self._q.put(data)
