from time import sleep
from cookbooks import cookbook_template, smithing_cookbook

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


_COOKBOOK = smithing_cookbook.COOKBOOK
LOOP_SLEEP = 0.5


class BotLoop:

    def __init__(self, DEBUG):
        self._clients = []
        self._q = None
        self.DEBUG = DEBUG
        self._stopped_clients = []
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

    def _login(self, client):
        print("Logging in!")
        for i, client in enumerate(self._clients):
            client.login()

        print("Logged in!")

    def _run(self):
        user_input = ''

        print(f"starting to bot!  Num clients {len(self._clients)}")
        if not self.DEBUG:
            self._login()

        while True and len(self._stopped_clients) < len(self._clients):
            if not self._q.empty():
                # Do something on user_input, possibly pass to each task
                user_input = self._q.get().decode("UTF-8")

            for task in self._cookbook:
                task.run()

            user_input = ''
            sleep(LOOP_SLEEP)
