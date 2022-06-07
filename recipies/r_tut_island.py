from random import gauss
from time import sleep
from utils import rr
import pyautogui as py
import cv2
7

'''  The client has a pos_x and pos_y indicating the top left corner  


    client.dims = [pos_x, pos_y, width, height]

'''


def click_gilinor_guide(client):
    ''' Starting from somewhere in 1st house, lookfor 'FFFF0000' and click him 

    NPC Indicators
    '''
    # Top left & Top right
    tl = client.dims[0]
    tr = client.dims[1]

    # Take screen shot
    # Find a square of the color FFFF0000 in the image
    # Click a random point and wait a second on npc
    # SS to see if we are actually talking to NPC


RECIPIES = {
    'tut_island': {
        'fns': [

        ],
        # ----------------------------------------------------------------------------------------
        'sleeps': [
            # lambda is_running: sleep(max(10, gauss(10.6, 0.59123))) if not is_running else sleep(
            # max(4.75, gauss(4.8, 0.39123))),

        ]
    }
}
