from pynput.keyboard import Key, Controller, KeyCode
from utils import Constant


class PyKey:

    keyboard = Controller()
    ENTER = Key.enter
    SPACE = Key.space
    LEFT = Key.left
    RIGHT = Key.right
    UP = Key.up
    DOWN = Key.down

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"

    @classmethod
    def press(cls, key: Key or str):
        # Press and release space
        cls.keyboard.press(key)
        cls.keyboard.release(key)
