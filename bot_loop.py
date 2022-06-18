from collections import defaultdict
from random import gauss
from PIL import Image
from time import sleep, time
from Colors import Colors
from Spaces import Spaces
from Search import Search
from Items import Items
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
        user_input = ''
        is_running = True
        img_taken = False  # Testing purposes

        print("starting to bot!")
        if not self.DEBUG:
            self._login()

        while True and len(self._stopped_clients) < len(self._clients):
            if not self._q.empty():
                user_input = self._q.get().decode("UTF-8")

            for i, client in enumerate(self._clients):
                if i in self._stopped_clients:
                    continue

                # res = Search.search_intf_image_to_num(
                #     client, Spaces.INTF_RUN)
                # print(f"Hp: {res}")

                # space = Spaces.INV
                # for item in [Items.GOLD_BAR, Items.DIAMOND, Items.BRACELET_DIAMOND]:
                #     print(item)
                #     Search.click(Search.search_space_item(
                #         client, space, item, confidence=item.value['conf']))

                # Search.click(Search.click_interface(
                #     client, Spaces.SKILL_ATT))

                Search.click(Search.search_space_color(
                    client, Spaces.N_A, Colors.NPC_PURPLE))

                # print(Search.chat_head_showing(client, left=True))

                sleep(1)
                # self.cook_from_book(client, i, user_input)
                if not img_taken:

                    #           End Client Loop          #
                    ######################################
                    pass
            img_taken = True
            user_input = ''
            sleep(.5)


if __name__ == "__main__":
    pass
