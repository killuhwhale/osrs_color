''' Follow this template when creating new recipies.

Make sure:
1. define RECIPIES as 
 = {
     'recipie_name' : {
         fns: []
         sleeps: []
     }
 }

 2. fns and sleeps must be same length
    - sleep after calling fn

'''

from random import gauss
from time import sleep
from utils import rr
import pyautogui as py


'''  The client has a pos_x and pos_y indicating the top left corner  


    client.dims = [pos_x, pos_y, width, height]

'''


def click_bank(client):
    # x, y = search_inventory(client, "steelbar.png")
    # max_tries = 5
    # while x < 0 and max_tries > 0:
    #     x, y = search_inventory(client, "steelbar.png")
    #     max_tries -= 1

    # Top left & Top right
    tl = client.dims[0]
    tr = client.dims[1]

    ''' Starting from furnace, click on bank. '''
    py.moveTo(rr(501, 513), rr(411, 430), max(
        0.256, gauss(0.5002, .4123)), py.easeOutBounce)
    py.click()


def deposit(client):
    py.moveTo(rr(1785, 1800), rr(265, 289),
              duration=max(0.256, gauss(0.3002, .1123)))
    py.click()


def withdraw_and_walk_back(client):
    # Click Ruby
    py.moveTo(rr(1036, 1055), rr(175, 195),
              duration=max(0.156, gauss(0.2002, .1123)))
    py.click()

    # 4. Click Gold
    py.moveTo(rr(1038, 1054), rr(210, 230),
              duration=max(0.1, gauss(0.1002, .2123)))
    py.click()

    # 5. Click furnance
    py.moveTo(rr(1232, 1240), rr(232, 243),
              duration=max(0.256, gauss(0.3002, .1123)))
    py.click()


def click_furance_interface(client):
    # click ammy mould spot
    py.moveTo(rr(880, 895), rr(330, 345),
              duration=max(0.256, gauss(0.5002, .2123)))
    py.click()


RECIPIES = {
    'make_cbs': {
        'fns': [
            click_bank,
            deposit,
            withdraw_and_walk_back,
            click_furance_interface,
        ],
        # ----------------------------------------------------------------------------------------
        'sleeps': [
            lambda is_running: sleep(max(10, gauss(10.6, 0.59123))) if not is_running else sleep(
                max(4.75, gauss(4.8, 0.39123))),
            lambda is_running: sleep(max(.250, gauss(.3, .29123))),
            lambda is_running: sleep(max(10, gauss(10.4002, .59123))) if not is_running else sleep(
                max(4.75, gauss(4.8, 0.39123))),
            lambda is_running: sleep(max(24.5, gauss(25.4002, 2.29123)))
        ]
    }
}
