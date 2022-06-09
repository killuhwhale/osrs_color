from random import gauss
from time import sleep
from utils import rr
import pyautogui as py


def print1(client):
    print(f"Step1: {client.get_pid()}")


def print2(client):
    print(f"Step2: {client.get_pid()}")


def print3(client):
    print(f"Step3: {client.get_pid()}")


def print4(client):
    print(f"Step4: {client.get_pid()}")


def print5(client):
    print(f"Step5: {client.get_pid()}")


def sleep1(is_running):
    print("Sleep1")
    return max(10, gauss(10.6, 0.59123)) if not is_running else max(4.75, gauss(4.8, 0.39123))


def sleep2(is_running):
    print("Sleep2")
    return max(.250, gauss(.3, .29123))


def sleep3(is_running):
    print("Sleep3")
    return max(10, gauss(10.4002, .59123)) if not is_running else max(4.75, gauss(4.8, 0.39123))


def sleep4(is_running):
    print("Sleep4")
    return max(24.5, gauss(25.4002, 2.29123))


def sleep5(is_running):
    print("Sleep5")
    return max(24.5, gauss(25.4002, 2.29123))


RECIPIE = {
    'fns': [
        print1,
        print2,
        print3,
        print4,
        print5,
    ],
    # ----------------------------------------------------------------------------------------
    'sleeps': [
        sleep1,
        sleep2,
        sleep3,
        sleep4,
        sleep5,
    ]
}
