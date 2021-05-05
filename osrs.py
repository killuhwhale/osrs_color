"""Color bot for OSRS using Runelite.

The bot can detect colors and find the area to click on.
As long as runelite can highlight something with a specified color, the bot
can locate it and click on it.

Use:
    python3 osrs.py

"""
import numpy as np
import cv2
import pyautogui
import random
import time
from PIL import Image
import os
import re
import subprocess


class Osrs:
    def __init__(self):
        self._pid = self._find_pid()
        # Window ID of Runelite client.
        self._win_id = self._get_win_ID()
        
        #Resizes window to set dimension.
        self._resize_window()

        # A list to store dimensions: x, y postition, height and width of window.
        # All window capture cropping functionality is relative to these values.
        self._dims = self._get_win_dimensions()
        self._center_x = (self._dims[2] // 2) + self._dims[0] - 35
        self._center_y = (self._dims[3] // 2) + self._dims[1] - 45

    def _resize_window(self):
        assert self._win_id, f"Window ID invalid: {self._win_id}"
        cmd = f"xdotool windowsize {self._win_id} 600 600"
        self._run_cmd(cmd)

    def _get_win_dimensions(self):
        """ Returns the postition of the top left corner of the window.
        Returns the top left corner and the width and height of the window.

        Returns:
            values: A list of screen coordinates indicating window position and size.
            [position x, position y, width, height]
        """
        _pos_pattern = r"""
        Position:\s*(?P<p_x>\d*),(?P<p_y>\d*)\s*\(\w*:\s*\d*\)
        """
        _geo_pattern = r"""
        Geometry:\s*(?P<g_x>\d*)x(?P<g_y>\d*)\s*
        """
        assert self._win_id, f"Window ID invalid: {self._win_id}"
        pos_pattern = re.compile(_pos_pattern, re.MULTILINE | re.VERBOSE)
        geo_pattern = re.compile(_geo_pattern, re.MULTILINE | re.VERBOSE)
        cmd = f"xdotool getwindowgeometry {self._win_id}"
        res = self._run_cmd(cmd)
        pos_match = re.search(pos_pattern, res)
        geo_match = re.search(geo_pattern, res)
        px = pos_match.group('p_x')
        py = pos_match.group('p_y')
        gx = geo_match.group('g_x')
        gy = geo_match.group('g_y')

        # Position(top left corner x, y coord) and Geometry(widthxheight)
        values = [px, py, gx, gy]
        values = [int(val) for val in values]
        assert all(values), f"Unable to find pos or geo of window: {self._win_id}"
        return values


    def _find_pid(self):
        """ Finds PID of runelite.
        #   Runelite 
        #   10521 pts/0    Sl+   35:25 ./RuneLite.AppImage
        """
        top = self._run_cmd("ps ax")
        pid_pattern = r"""^\s*
        (?P<pid>\d*)\s*
        \w*/\d*\s*
        \w*\+\s*
        \d*:\d*\s*
        \.\/RuneLite\.AppImage$"""
        pattern = re.compile(pid_pattern, re.MULTILINE | re.VERBOSE )
        match = re.search(pattern, top)
        assert match, f"Did not find pid: \n{top[:200]}"
        return match.group('pid')

    def _get_win_ID(self):
        """ Gets window ID of Runelite.

        Returns:
            The window ID of Runelite based on the PID.
            
        """
        assert self._pid, f"Window ID invalid: {self._pid}"
        cmd = f"xdotool search --pid {self._pid}"
        return self._run_cmd(cmd).split("\n")[-2]
    
    def _run_cmd(self, cmd):
        """ Runs a bash command.

        Args:
            cmd: A string that represents the command.
        Returns:
            stdout from bash command
        """
        return subprocess.run(cmd.split(), check=True, encoding='utf-8', capture_output=True).stdout

    def _crop_inventory(self):
        """Crops the screenshot of the window to the Inventory.
        """
        dims = self._dims
        # 200x270
        x = dims[0]+535
        y = dims[1]+250
        self._screen_Image(x, y, x+200, y+270, 'inventshot.png')

    def _crop_window(self):
        """Crops the screenshot of the window to the Runelite Window.
        """
        dims = self._dims
        x = dims[0] + dims[2]-10
        y = dims[1] + dims[3]-50
        self._screen_Image(dims[0]-10, dims[1]-50, x, y, "whole.png")

    def _screen_Image(self, left=0, top=0, right=0, bottom=0, name='screenshot.png'):
        myScreenshot = pyautogui.screenshot()
        # open_cv_image = np.array(img) 
        # # Convert RGB to BGR 
        # open_cv_image = open_cv_image[:, :, ::-1].copy()
        myScreenshot.save(r'screenshot.png')
        if left != 0 or top != 0 or right != 0 or bottom != 0:
            im = Image.open(r'screenshot.png')  # uses PIL library to open image in memory
            im = im.crop((left, top, right, bottom))  # defines crop points
            im.save(name)  # saves new cropped image
            print('screeenshot saved')

    def attack(self):
        """ The main attack cycle.
        """
        while(True):
            self._findarea_attack(3, 2)
            time.sleep(random.uniform(3, 8))

    def  _closest(self, contour, x, y):
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

    def _findarea_attack(self, object, deep=20):
        """Finds the highlighted area on Runelite window.
        """
        # Gets screenshot of entire screen
        image = np.array(pyautogui.screenshot())
        # Cropped to Runelite Window.
        dims = self._dims
        w = dims[2]-10
        h = dims[3]-50
        x = dims[0]-10
        y = dims[1]-50
        image = image[y:y+h, x:x+w]
        
        # Convert RGB to BGR 
        image = image[:, :, ::-1].copy()
        
        # B, G, R
        #--------------------- ADD OBJECTS -------------------
        red = ([0, 0, 180], [80, 80, 255])
        green = ([0, 180, 0], [80, 255, 80])
        pickup_high = ([200,0,100], [255,30,190])
        attack_blue = ([200, 200, 0], [255, 255, 50])
        amber = ([0, 160, 160], [80, 255, 255])
        # --------------------- ADD OBJECTS -------------------
        ore_list = [red, green, pickup_high, attack_blue, amber]
        boundaries = [ore_list[object]]
        
        # loop over the boundaries
        for (lower, upper) in boundaries:
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            # Create black and white image where the highlighted color is/
            
            # Find the color in the image
            mask = cv2.inRange(image, lower, upper)
            # Create blk and wht image using mask.
            output = cv2.bitwise_and(image, image, mask=mask)
            # Find threshold
            ret, thresh = cv2.threshold(mask, 50, 255, 0)
            # Get contours from threshold image.
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            
        if len(contours) != 0:
            # cv2.drawContours(output, contours, -1, 255, 3)
            # find the biggest countour (c) by the area
            
            # Find closest contour to the center of the screen.
            c_i = self._closest_contour(contours)
            c = contours[c_i]
            
            # Drawg contour
            x, y, w, h = cv2.boundingRect(c)
            whalf = max(round(w/2), 1)
            hhalf = max(round(h/2), 1)
            print(x, y, w, h)

            # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            x = random.randrange(x + dims[0]-10 + whalf - deep, x + dims[0]-10 + max(whalf + deep, 1)) # 950,960
            y = random.randrange(y + dims[1]-50 + hhalf - deep, y + dims[1]-50 + max(hhalf + deep, 1))  # 490,500
            print('attack x: ', x)
            print('attack y: ', y)
            b = random.uniform(0.05, 0.1)
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.01, 0.05)
            pyautogui.click(duration=b)
            # cv2.imshow("Result", np.hstack([image, output]))
            # cv2.waitKey(20)
            return True
        return False

    def click_center(self):
        """Test center click. """
        b = random.uniform(0.01, 0.05)
        pyautogui.moveTo(self._center_x, self._center_y, duration=b)
        pyautogui.click()

    def login(self, username, password):
        """Logs user into the game.
        User must be on the login screen ready to login.
        """
        b = random.uniform(0.01, 0.05)
        pyautogui.moveTo(self._center_x, self._center_y, duration=b)
        pyautogui.click()
        msg = []
        msg.extend(list(username))
        msg.append("enter")
        msg.extend(list(password))
        msg.append("enter")
        pyautogui.typewrite(msg, interval=0.1)

if __name__ == "__main__":
    # NPC color indicator: #FF00FAFF
    osrs = Osrs()
    osrs.login("testminnie001@gmail.com", "testminnie123")
    osrs.attack()
    

    