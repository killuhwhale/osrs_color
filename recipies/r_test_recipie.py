from random import gauss
from time import sleep
from utils import rr

from Colors import Colors
from Items import Items
from Map import Map
from PyKey import PyKey
from Search import Search
from Spaces import Spaces


def walk_to_bank(client):
    ct = rr(0, 100)
    if ct < 50:
        Search.click(Search.click_interface_from_raw_coords(
            client, [583, 92, 600, 105]))
    else:
        Search.click(Search.search_space_color(
            client, Spaces.WEST, Colors.Blue))


def click_on_bank(client):
    Search.click(Search.search_space_color(client, Spaces.SOUTH, Colors.Red))


def walk_to_bank_sleep(is_running):
    return max(9, gauss(9.6, 0.59123))


def click_on_bank_sleep(is_running):
    return max(3, gauss(3.6, 0.59123))


RECIPIE = {
    'fns': [
        walk_to_bank,
        click_on_bank,
    ],
    # ----------------------------------------------------------------------------------------
    'sleeps': [

        walk_to_bank_sleep,
        click_on_bank_sleep,

    ]
}
