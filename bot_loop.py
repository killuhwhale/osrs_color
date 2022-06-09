from collections import defaultdict
from time import sleep, time
from utils import Spaces, search_space, move_map_deg, reset_map, move_map_pitch, search_and_click
from cookbooks import cookbook_template

ACCOUNTS = [
    ['thisiscrazy@really.net', 'qpwoei1337'],
    ['thisiscrazy1@really.net', 'qpwoei1337'],
    ['thisiscrazy2@really.net', 'qpwoei1337'],
    ['thisiscrazy3@really.net', 'qpwoei1337'],
]

''' The main bot loop.

The loop will run until stopped. 
The loop will execute a step and sleep from a recipie for each client.


 How To add new recipies/ actions:

    1. Add new action to all_actions.py
    2. Add new recipie into new file under recipies/
    3. Update all_recipies with new recipie
        - import new recipie file from recipies.*
        - add code to update main RECIPIE dict
'''


class SleepCycle:
    def __init__(self):
        self.start = 0.0
        self.dur = 0.0

    def set(self, start, dur):
        self.start = start
        self.dur = dur

    def is_ready(self):
        return time() - self.start >= self.dur


class BotLoop:
    def __init__(self, DEBUG):
        self._clients = []
        self._q = None
        self.DEBUG = DEBUG
        self._stopped_clients = []
        # each client will update this with how long they need to sleep for
        self._sleeps = defaultdict(SleepCycle)
        self._steps = defaultdict(int)
        self._cookbook = cookbook_template.COOKBOOK_TEMPLATE

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

    def cook_from_book(self, client, i, user_input=""):
        recipie = self._cookbook[i]  # Get recipie from cookbook for client
        step = self._steps[i]
        # print(f'Checking if {i} isReady')

        if self._sleeps[i].is_ready():
            recipie['fns'][step](client)  # Do the step for the client
            self._steps[i] += 1  # Update the clients current step.
            # Update the sleep time, call lambda function to generate random sleep val
            is_running = True
            self._sleeps[i].set(time(), recipie['sleeps'][step](is_running))

        # End of recipie reached
        if step == len(recipie['fns']) - 1:
            self._steps[i] = 0  # Update the clients current step.
            # chance to add client to stopped_clients
            if user_input == "stop":
                self._stopped_clients.append(i)

    def _run(self):
        print("starting to bot!")
        if not self.DEBUG:
            self._login()

        img_taken = False  # Testing purposes
        user_input = ''
        # Need a way to monitor running for each account as well...
        is_running = True

        while True and len(self._stopped_clients) < len(self._clients):
            if not self._q.empty():
                user_input = self._q.get().decode("UTF-8")

            for i, client in enumerate(self._clients):
                if i in self._stopped_clients:
                    continue

                # self.cook_from_book(client, i, user_input)
                if not img_taken:
                    spaces = Spaces.ROW_1
                    item = "test/cluescroll.png"
                    # Searches a space on screen for a target and randomly clicks within its bounds if found.
                    result = search_and_click(
                        client, spaces, item, grayscale=False, confidence=0.74)

                    print("Img result: ", result)

            img_taken = True
            # End Client Loop

            # Reset user input
            user_input = ''
            # sleep(2.5)


if __name__ == "__main__":
    pass
