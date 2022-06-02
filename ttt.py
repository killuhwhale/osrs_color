from time import sleep
from random import gauss, random, randrange, shuffle


screen_width = 1920
screen_height = 1080


def clickBank(client):
    print(f"Clicking bank.... for client: {client.name}")
    delay = max(10, gauss(4.6, 0.59123))
    client.add_sleep(delay)
    # py.move(x,y,delay, asdasd)


def deposit(client):
    point = (501, 400)
    # target_point = client.translate(point)
    target_point = client + point
    print(f"Despositing items... {target_point} ")


class BaseClient:
    def __init__(self, name):
        self.name = name

    def hi():
        print("Hello")


class Client(BaseClient):
    def __init__(self, name, x, y):
        BaseClient.__init__(name)
        self.x = x
        self.y = y
        self.is_running = False
        self.sleep_time = 0

    def hi():
        print("Hey!")

    def get_y(self):
        return self.x

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def translate(self, point):
        return (self.x + point[0], self.y + point[1])

    def __add__(self, other):
        assert type(other) is type(tuple)
        assert len(other) == 2

        return tuple((self.x + other[0], self.y + other[1]))

    def clear_sleep(self):
        self.sleep_time = 0
        return True

    def add_sleep(self, num):
        self.sleep_time += num
        return True

    def get_sleep_time(self):
        return self.sleep_time


clients = [
    Client('c1', 0, 0),   # takes 8s -> -2s -> 2s -> 2s = 6s
    Client('c2', screen_width/2, 0),  # runs for 2s
    Client('c3', 0, screen_height/2),  # run for 2s
    Client('c4', screen_width/2, screen_height/2),  # run for 2s
]

# 10s - 6s = 4s

fns = [
    clickBank,  # 0
    deposit,  # 1
    # ......
]


sleeps_walking = [
    lambda: max(10, gauss(4.6, 0.59123)),
    (3, 2),
    (3, 7),
]

sleeps_running = [
    (10, 7),
    (3, 2),
    (3, 7),
]


loops = 1000
is_running = True
step = 0  # index to a list, which fn to call for the client

while True:

    '''
        Sleeping and running should work as long as
        each client/ account has the same agility level and weight.... 
        With no misclicks..
    '''

    client_sleep_time = 0
    for client in clients:
        client.clear_sleep()
        fns[step](client)
        client_sleep_time += client.get_sleep_time()

    # Sleep here
    if is_running:
        sleep(sleeps_running[step] - client_sleep_time)
    else:
        sleep(sleeps_walking[step] - client_sleep_time)
    # Depending on the step
    step += 1
