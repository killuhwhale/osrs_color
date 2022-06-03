from time import sleep
from all_recipies import get_all_recipies
from all_actions import get_all_actions
from utils import search_inventory
ACCOUNTS = [
    ['thisiscrazy@really.net', 'qpwoei1337'],
    ['thisiscrazy1@really.net', 'qpwoei1337'],
    ['thisiscrazy2@really.net', 'qpwoei1337'],
    ['thisiscrazy3@really.net', 'qpwoei1337'],
]

ALL_RECIPIES = get_all_recipies()
ALL_ACTIONS = get_all_actions()

print("All actions: ", ALL_ACTIONS)


''' How To add new recipies/ actions:

    1. Add new action to all_actions.py
    2. Add new recipie into new file under recipies/
    3. Update all_recipies with new recipie
        - import new recipie file from recipies.*
        - add code to update main RECIPIE dict
'''


class BotLoop:
    def __init__(self, DEBUG):
        self._clients = []
        self._q = None
        self.DEBUG = DEBUG

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
        if not self.DEBUG:
            self._login()
        user_input = ''
        action = 'make_cbs'
        step = 0
        next_action = ''
        is_running = True
        img_taken = False
        while True:
            if not self._q.empty():
                user_input = self._q.get().decode("UTF-8")

            if user_input:
                print(f"User gave cmd: {user_input}")
                if user_input in ALL_ACTIONS:
                    next_action = ALL_ACTIONS[user_input]

                if user_input == 'stop':
                    pass

            for i, client in enumerate(self._clients):
                # ALL_RECIPIES[action]['fns'][step](client)
                if not img_taken:
                    search_inventory(client, "jug.png")
                    img_taken = True
                sleep(1)

            # Calls sleep lambda sleep function
            '''
            ALL_RECIPIES[action]['sleeps'][step](is_running)

            step += 1
            if step >= len(ALL_RECIPIES[action]['fns']):
                step = 0  # Reset
                # Check if a next action is set
                if next_action:
                    action = next_action
                    next_action = ''
            '''

            user_input = ''
            # sleep(2.5)


if __name__ == "__main__":
    pass
