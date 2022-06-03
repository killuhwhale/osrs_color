from random import randrange
from subprocess import Popen, PIPE, run
import pyautogui
from PIL import Image
import numpy as np

from osrs import OsrsClient


def run_script(proc, script):
    p = Popen([proc, '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(script)
    return stdout, stderr


def run_cmd(cmd, as_list=False):
    """ Runs a bash command.

    Args:
        cmd: A string that represents the command.
    Returns:
        stdout from bash command
    """

    return run(cmd.split()if not as_list else cmd, check=True, encoding='utf-8', capture_output=True).stdout


def rr(a, b):
    ''' Returns random range between a and b. '''
    return randrange(a, b)


def screen_image(left=0, top=0, right=0, bottom=0, name='screenshot.png'):
    myScreenshot: Image = pyautogui.screenshot(
        'test.png', region=(left*2, top*2, (right - left)*2, (bottom - top)*2))
    print(f'{name} saved')
    return myScreenshot


def load_img(name):
    return Image.open(name)


def crop_inventory(client: OsrsClient):
    """Crops the screenshot of the window to the Inventory.
    Maps screen coords to Image coords

    x_offset = 397 + client.x
    y_offset = 259 + client.y

    (397, -820) => top left corner of Inventory (From click pos tool)
    ------------------------------------------------------                                          
    |  w = 182   h = 265                                  |
    |                                                     |
    |                                                     |                        
    |                                                     |                        
    |                                                     |
    ------------------------------------------------------
                                            (579, -555) => Bottom right corner of Inventory (From click pos tool)
                                            x_offset + w
                                            y_offset + h
    """
    dims = client.dims
    # Top left of client on Screen
    x = dims[0]
    y = dims[1]
    # Now x and y are without the offsets
    x_offset = 658 + x  # Offset for top left corner of Inventory
    y_offset = 264 + y  #
    w = 159  # w of Inventory
    h = 250  # h of Inventory

    print(
        f"Taking image at {(x_offset, y_offset)} , {(x_offset + w, y_offset + h)} ")
    return [screen_image(x_offset, y_offset, x_offset + w,
                         y_offset + h, 'inventshot.png'), x_offset, y_offset]


# item = id, img/ SS
'''
TODO() Figure out a system to get images.

'''


def search_inventory(client, item):
    # Img of inventory
    inv, x_offset, y_offset = crop_inventory(client)
    needle = load_img(item)

    # 4-integer tuple: (left, top, width, height)
    bounds = pyautogui.locate(needle, inv)
    print("Found needle @: ")
    print(bounds)
    if bounds is None:
        print("DIDNT FIND THE IMAGE.")
        return -1, -1

    left = bounds[0] // 2
    top = bounds[1] // 2
    width = bounds[2] // 2
    height = bounds[3] // 2

    x_left = x_offset + left
    y_top = y_offset + top

    x_right = x_left + width
    y_bottom = y_top + height

    print(f"Click x between {(x_left, x_right)} and y {(y_top, y_bottom)}")

    # return rr(x_left, x_right), rr(y_top, y_bottom)
    pyautogui.moveTo(rr(x_left, x_right), rr(y_top, y_bottom))
    pyautogui.click()


def crop_window(client: OsrsClient):
    """Crops the screenshot of the window to the Runelite Window.
    """
    dims = client.dims
    x = dims[0]
    y = dims[1]
    w = dims[2]
    h = dims[3]

    screen_image(x, y, x+w, y+w, "whole.png")
