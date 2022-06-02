from pynput import mouse


class MousePOS:
    def __init__(self):
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed and str(button) == 'Button.left':
            print(f'{int(x)}, {int(y)}')
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
