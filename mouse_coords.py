from pynput import mouse
from config import SCREEN_TOP_MARGIN, WINDOW_TOP_MARGIN


''' A program to find relative screen coordinates.

    When a click is received, the y coordinate is adjusted by the size of the screen and client margin.
'''


class MousePOS:
    def __init__(self):
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed and str(button) == 'Button.left':
            print(
                f'abs coords {int(x)}, {int(y - SCREEN_TOP_MARGIN - WINDOW_TOP_MARGIN)}  Reg:  {int(x)}, {int(y)}')

        if not pressed:
            # Stop listener
            # return False
            pass

    def start(self):
        self.listener = mouse.Listener(
            on_click=self.on_click)
        self.listener.start()
        while True:
            pass


if __name__ == "__main__":
    tool = MousePOS()
    tool.start()
