from time import sleep


ACCOUNTS = [
    ['thisiscrazy@really.net', 'qpwoei1337'],
    ['thisiscrazy1@really.net', 'qpwoei1337'],
    ['thisiscrazy2@really.net', 'qpwoei1337'],
    ['thisiscrazy3@really.net', 'qpwoei1337'],
]


class BotLoop:
    def __init__(self):
        self._clients = []
        self._q = None

    def set_clients(self, clients):
        self._clients = clients
        return True

    def start_bot(self, queue):
        self._q = queue
        self._run()

    def _login(self):
        print("Logging in!")
        for i, client in enumerate(self._clients):
            creds = ACCOUNTS[i]
            print(f"Loggin in with {creds}")
            client.login(creds[0], creds[1])

        print("Logged in!")

    def _run(self):
        print("starting to bot!")
        self._login()

        user_input = ''
        while True:
            if not self._q.empty():
                user_input = self._q.get().decode("UTF-8")

            if user_input:
                print(f"User gave cmd: {user_input}")
                if user_input == 'stop':
                    pass

            for i, client in enumerate(self._clients):
                # print(f"Sending command to client {i}")
                # client.click_center()
                pass

            user_input = ''
            # sleep(2.5)


if __name__ == "__main__":
    pass
