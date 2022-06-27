from collections import defaultdict
from random import gauss
from PIL import Image
from time import sleep, time
from Colors import Colors
from Spaces import Spaces
from Search import Search
from Items import Items
from cookbooks import cookbook_template, smithing_cookbook
from PyKey import PyKey

from recipies.EdgeFurnace import EdgeFurnace

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


# class SleepCycle:
#     def __init__(self):
#         self.start = 0.0
#         self.dur = 0.0

#     def set(self, start, dur):
#         self.start = start
#         self.dur = dur

#     def is_ready(self):
#         return time() - self.start >= self.dur

_COOKBOOK = smithing_cookbook.COOKBOOK


class BotLoop:

    def __init__(self, DEBUG):
        self._clients = []
        self._q = None
        self.DEBUG = DEBUG
        self._stopped_clients = []
        # each client will update this with how long they need to sleep for
        # self._sleeps = defaultdict(SleepCycle)
        # self._steps = defaultdict(int)
        # Cookbook Will hold the initilized Task for the client.
        self._cookbook = []

    def set_clients(self, clients):
        self._clients = clients
        if len(clients) > len(_COOKBOOK):
            print(
                f"Too many clients for the number of recipies given. Clients: {len(clients)} Recipies: {len(_COOKBOOK)}")
            return

        # Init each task with the client.
        for i in range(len(clients)):
            client = clients[i]
            meal = _COOKBOOK[i]
            initilized_tasks = []
            for recipie_data_row in meal.tasks:
                # recipie_data_row = meal
                recipe = recipie_data_row[0]
                r = None
                if len(recipie_data_row) > 1:
                    recipe_data = recipie_data_row[1]
                    r = recipe(client, *recipe_data)
                else:
                    r = recipe(client)
                initilized_tasks.append(r)

            meal.tasks = initilized_tasks
            self._cookbook.append(meal)

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

        # End of recipie reached
        if step == len(recipie['fns']):
            self._steps[i] = 0
            step = 0

            if user_input == "stop":
                self._stopped_clients.append(i)
                return

        # print(f'Checking if {i} isReady')
        if self._sleeps[i].is_ready():
            print(f"\nRunning step: {step}\n")
            recipie['fns'][step](client)  # Do the step for the client
            self._steps[i] += 1  # Update the clients current step.
            # Update the sleep time, call lambda function to generate random sleep val
            is_running = True
            self._sleeps[i].set(time(), recipie['sleeps'][step](is_running))
        else:
            print(f"\Sleeping on step: {step}\n")

    def _run(self):
        user_input = ''
        img_taken = False  # Testing purposes

        print(f"starting to bot!  Num clients {len(self._clients)}")
        if not self.DEBUG:
            self._login()

        while True and len(self._stopped_clients) < len(self._clients):
            if not self._q.empty():
                user_input = self._q.get().decode("UTF-8")

            for task in self._cookbook:
                task.run()

            # # Test indiviual snippets
            # for i, client in enumerate(self._clients):
            #     if i in self._stopped_clients:
            #         continue

            #     sleep(1)

            #     if not img_taken:

            #         #           End Client Loop          #
            #         ######################################
            #         pass

            # img_taken = True
            user_input = ''
            sleep(.5)
