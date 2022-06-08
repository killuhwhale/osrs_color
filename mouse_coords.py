from pynput import mouse
from config import SCREEN_TOP_MARGIN, WINDOW_TOP_MARGIN


class MousePOS:
    def __init__(self):
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed and str(button) == 'Button.left':
            print(
                f'abs coords {int(x)}, {int(y - SCREEN_TOP_MARGIN - WINDOW_TOP_MARGIN)}')
            # print('{0} at {1}'.format(
            #     'Pressed' if pressed else 'Released', (x, y)))
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
