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

'''
TODOs

Maybe make a plugin that can send things to input....



RL notifies of idle, SS for a lvl, plugin gives status of "not smithing" 


'''


class GoToGE(R.RecipieTask):
    ''' Takes player to GE starting from Bank,
    Player must have tele runes (Fire, Air, Law) in Bank tab one. 

    '''
    init = True

    def __init__(self, client):
        super().__init__(client)
        self.tile_walk = False

    def _t_withdraw_tele_varrock_runes(self, client):
        ''' 
            1. Search [tab | click search & type | ]
            1a. Click tab with predetermine rune
            1b. click search button
                - autotype "rune"

            2. Locate fire and law rune
        '''
        Search.click(Search.click_interface(client, Spaces.BANK_TAB_1))
        sleep(max(0.212, gauss(.3, .1012)))

        shuffled = Items.shuffle_index(3)
        items = [
            Items.AIR_RUNE,
            Items.FIRE_RUNE,
            Items.LAW_RUNE,
        ]

        for i in shuffled:
            item = items[i]
            Search.click(Search.search_space_item(
                client, Spaces.PLAYER_CENTER_LG, item))
            sleep(max(0.212, gauss(.3, .1012)))

    def _t_close_bank(self, client):
        Search.click(Search.click_interface(client, Spaces.RESET_MAP))
        sleep(max(8.212, gauss(.9, .1512)))
        Search.click(Search.click_interface(client, Spaces.CLOSE_BANK))

    def _t_tele_varrock(self, client):
        Search.click(Search.click_interface(client, Spaces.PANEL_MAGIC))
        sleep(max(0.212, gauss(.4, .1512)))
        Search.click(Search.click_interface(client, Spaces.MAGIC_VARROCK_TELE))

    def _t_walk_to_ge_1(self, client):
        # if we do random points, we will be at different points in the game,
        # can build a variemty of paths in differtn chunks.
        # E.G. step_1 step_2 step_3 step_4
        #   within each step, we can make 5 differnt types fo click for 5 paths.
        # each step would have a segemnt for the path.
        # we can randomly pick which path in step 1 and track it.
        Search.click(Search.search_space_color(
            client, Spaces.PLAYER_CENTER_LG, Colors.Blue))

    def _t_walk_to_ge_2(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.NORTH, Colors.Green))

    def _t_walk_to_ge_3(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.NORTH, Colors.Blue))

    def _t_walk_to_ge_4(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.WEST, Colors.Green))

    def _t_walk_to_ge_5(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.NORTH, Colors.Blue))

    def _t_walk_to_ge_6(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.NORTH, Colors.Green))

    def _r_walk_and_click_bank(self, client):
        return
        if rr(0, 100) < 50:
            Search.click(Search.search_space_color(
                client, Spaces.EAST, Colors.Yellow))
            sleep(max(0.412, gauss(.8, .1512)))
            Map.move_map_deg(client, -90)
            sleep(max(0.612, gauss(.9, .1512)))
            Search.click(Search.search_space_color(
                client, Spaces.NORTH, Colors.Green))
        else:
            Search.click(Search.search_space_color(
                client, Spaces.WEST, Colors.Yellow))
            sleep(max(1.212, gauss(1.4, .1512)))
            Map.move_map_deg(client, 90)
            sleep(max(3.312, gauss(3.3, .1512)))
            Search.click(Search.search_space_color(
                client, Spaces.NORTH, Colors.Blue))

    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    SLEEPS    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    '''

    def _d_withdraw_tele_varrock_runes(self, is_running):
        return max(1, gauss(1.6, 0.59123))

    def _d_close_bank(self, is_running):
        return max(1, gauss(1.6, 0.59123))

    def _d_tele_varrock(self, is_running):
        return max(4, gauss(4.6, 0.59123))

    def _d_walk_to_ge_1(self, is_running):
        return max(6.8, gauss(6.9, 0.59123))

    def _d_walk_to_ge_2(self, is_running):
        return max(10, gauss(10.9, 0.59123))

    def _d_walk_to_ge_3(self, is_running):
        return max(8.9, gauss(8.9, 0.59123))

    def _d_walk_to_ge_4(self, is_running):
        return max(10.6, gauss(10.9, 0.59123))

    def _d_walk_to_ge_5(self, is_running):
        return max(9.9, gauss(9.9, 0.59123))

    def _d_walk_to_ge_6(self, is_running):
        return max(8.9, gauss(9, 0.59123))

    def _s_walk_and_click_bank(self, is_running):
        return max(8.9, gauss(9, 0.59123))

    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    Validators    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    Returns:
        True=> Move to next step, False => Repeat step, None=> exit recipie
    '''

    def _b_withdraw_tele_varrock_runes(self, client):
        # Check Air rune Fire rune and law run in inventory
        res = Search.search_space_multi_item(
            client, Spaces.INV, [Items.AIR_RUNE, Items.FIRE_RUNE, Items.LAW_RUNE])
        print(f"Multi search item res: {res}")
        return all(res)

    def _b_close_bank(self, client):
        return True

    def _b_tele_varrock(self, client):
        # Check for a specific color on the ground to know we have finished the tele

        pt = Search.search_space_color(client, Spaces.WEST, Colors.Blue)
        return True if pt else False

    def _b_walk_to_ge_1(self, client):
        return True

    def _b_walk_to_ge_2(self, client):
        return True

    def _b_walk_to_ge_3(self, client):
        return True

    def _b_walk_to_ge_4(self, client):
        return True

    def _b_walk_to_ge_5(self, client):
        return True

    def _b_walk_to_ge_6(self, client):
        return True

    def _v_walk_and_click_bank(self, client):
        # verify bank, search for  something
        return None if Search.verify_space(client, VerifySpace.CONTINUE) else False
