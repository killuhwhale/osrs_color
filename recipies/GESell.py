from random import gauss, shuffle
from time import sleep
from Tasks import RecipieTask as R
from VerifySpace import VerifySpace
from utils import rr

from Colors import Colors
from Items import Items
from Map import Map
from PyKey import PyKey
from Search import Search
from Spaces import Spaces


class GESell(R.RecipieTask):
    ''' Takes player to GE starting from Bank,
    Player must have tele runes (Fire, Air, Law) in Bank tab one. 

    '''

    def __init__(self, client):
        super().__init__(client)

    def _r_(self, client):
        pass

    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    SLEEPS    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    '''

    def _s_(self, is_running):
        pass
    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    Validators    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    Returns:
        True=> Move to next step, False => Repeat step, None=> exit recipie
    '''

    def _v_(self, client):
        pass
