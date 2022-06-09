"""Color bot for OSRS using Runelite.

The bot can detect colors and find the area to click on.
As long as runelite can highlight something with a specified color, the bot
can locate it and click on it.

Use:
    python3 osrs.py
"""

import pyautogui
import random
import time


class OsrsClient:
    def __init__(self, pid=None, dims=None):
        # self._pid = self._find_pid()
        self._pid = pid
        # A list to store dimensions: x, y postition, height and width of window.
        # All window capture cropping functionality is relative to these values.
        self.dims = dims
        self._center_x = (self.dims[2] // 2) + self.dims[0]
        self._center_y = (self.dims[3] // 2) + self.dims[1]

    def get_pid(self):
        return self._pid

    def attack(self):
        """ The main attack cycle.
        """
        while(True):

            time.sleep(random.uniform(3, 8))

    def _closest(self, contour, x, y):
        """  Finds the closest point on a contour to a given point.
        Args:
            countour: List of points indicating a contour.
            x: target x coordinate
            y: target y coordinate
        Returns:
            _min: The closest distance from a countour.
        """
        _min = 2**100
        for pt in contour:
            pt = pt[0]
            d = (x - pt[0])**2 + (y - pt[1])**2
            if d < _min:
                _min = d
        return _min

    def _closest_center(self, contour):
        """ Returns the closest point in a contour to the center of the screen.
        """
        return self._closest(contour, self._center_x, self._center_y)

    def _closest_contour(self, contours):
        """ Finds the contour closest to the center of the screen.
        Args:
            contours: A list of contours.
        Returns:
            _i: The index of the countour closest to the center.
        """
        _min = 2**100
        _i = 0
        for i, contour in enumerate(contours):
            d = self._closest_center(contour)
            if d < _min:
                _min = d
                _i = i
        return _i

    def click_center(self):
        """Test center click. """
        # print(f'Clicking: {self._center_x}, {self._center_y} ')
        b = random.uniform(0.25, 0.5)
        pyautogui.moveTo(self._center_x, self._center_y, duration=b)
        pyautogui.click()

    def login(self, username, password):
        """Logs user into the game.
        User must be on the login screen ready to login.
        """
        print(f"Loggin in w/ {username}, {password}")
        b = random.uniform(0.05, 0.2)
        pyautogui.moveTo(self._center_x, self._center_y, duration=b)
        pyautogui.click()  # TODO() Make this click more generally instead of center
        msg = []
        msg.append("enter")
        msg.extend(list(username))
        msg.append("enter")
        pyautogui.typewrite(msg, interval=b)
        msg = []
        msg.extend(list(password))
        # msg.append("enter")
        pyautogui.typewrite(msg, interval=b)
        msg = []


if __name__ == "__main__":
    # NPC color indicator: #FF00FAFF
    # osrs = Osrs()
    # osrs.login("email@mail.com", "password")
    # osrs.attack()
    print("")
