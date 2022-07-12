from random import gauss, shuffle
from time import sleep
from tasks import RecipieTask as R
from utils import rr

from colors import Colors
from items import Items
from map import Map
from py_key import PyKey
from search import Search
from spaces import Spaces

'''
TODOs

Maybe make a plugin that can send things to input....



RL notifies of idle, SS for a lvl, plugin gives status of "not smithing" 


'''


class EdgeFurnace(R.RecipieTask):
    init = True

    # item_to_make = str(Items.SILVER_BAR)
    # items_to_withdraw = [Items.SILVER_ORE]
    # space_to_click_to_smelt = Spaces.SMELT_BAR_SILVER
    # smelt_time = 92  # seconds

    smelt_bar_numbers = {
        str(Items.BRONZE_BAR): PyKey.ONE,
        str(Items.IRON_BAR): PyKey.TWO,
        str(Items.SILVER_BAR): PyKey.THREE,
        str(Items.STEEL_BAR): PyKey.FOUR,
        str(Items.GOLD_BAR): PyKey.FIVE,
        str(Items.MITHRIL_BAR): PyKey.SIX,
        str(Items.ADAMANTITE_BAR): PyKey.SEVEN,
        str(Items.RUNITE_BAR): PyKey.EIGHT,
    }

    # bar_num_to_press = smelt_bar_numbers[item_to_make]
    def __init__(self, client, item_to_make, items_to_withdraw, space_to_click_to_smelt, smelt_time):
        print("Edge Furance INIT!#@@#@#", item_to_make,
              items_to_withdraw, space_to_click_to_smelt, smelt_time)
        super().__init__(client)
        self.item_to_make = item_to_make
        self.items_to_withdraw = items_to_withdraw
        self.space_to_click_to_smelt = space_to_click_to_smelt
        self.smelt_time = smelt_time
        self.bar_num_to_press = self.smelt_bar_numbers[item_to_make]

    def check_state(self):
        ''' Ex: combat bot

            atFightSpot = True

            didTeleToBank = False
            shouldBank = False 


            check the current state
            if atFightSpot:
                1. Health health -> eat food | none
                2. Prayer -> drink | None
                3. Check Inv -> Tele | none
                4. In Combat -> Attack | none
            elif didTele and shouldBank:
                # sleeps when the steps look like recipie steps.
                5. Walk to bank 
                6 Deposit & withdraw
            elif not atFightSpot and didTeleToBank and not shouldBank:
                7. get back to fight spot






        '''
        pass

    def _r_walk_to_bank(self, client):
        global init
        # if init:
        #     Search.click(Search.click_interface(client, Spaces.RESET_MAP))
        #     Map.move_map_deg(client, -90)
        #     init = False

        ct = rr(0, 100)
        if ct < 50:
            Search.click(Search.click_interface_from_raw_coords(
                client, [627, 19, 640, 36]))
        else:
            Search.click(Search.search_space_color(
                client, Spaces.NORTH, Colors.Blue))

    def _r_click_on_bank(self, client):
        Search.click(Search.search_space_color(
            client, Spaces.WEST, Colors.Red))

    def _r_withdraw_items(self, client):

        Search.click(Search.click_interface(client, Spaces.BANK_DEPOSIT_INV))

        items = list(range(0, len(self.items_to_withdraw)))
        shuffle(items)  # Randomize items to withdraw

        for i in items:
            item = self.items_to_withdraw[i]
            Search.click(Search.search_space_item(
                client, Spaces.PLAYER_CENTER_LG, item))

    def _r_walk_to_furnace(self, client):
        Search.click(Search.click_interface_from_raw_coords(
            client, [650, 122, 667, 136]))

    def _r_click_on_furnace(self, client):

        Search.click(Search.search_space_color(
            client, Spaces.PLAYER_CENTER_LG, Colors.Red, padding=10))
        sleep(max(3.25, gauss(3.5, .15)))
        ct = rr(0, 100)
        print("Starting to smith!")

        if ct < 50 or self.init:
            Search.click(Search.click_interface(
                client, self.space_to_click_to_smelt))
        else:
            PyKey.press(self.bar_num_to_press)

        self.init = False

    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    SLEEPS    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    '''

    def _s_walk_to_bank(self, is_running):
        return max(9, gauss(9.6, 0.59123))

    def _s_click_on_bank(self, is_running):
        return max(3, gauss(3.6, 0.59123))

    def _s_withdraw_items(self, is_running):
        return max(1, gauss(2, 0.59123))

    def _s_walk_to_furnace(self, is_running):
        return max(11, gauss(11.6, 0.59123))

    def _s_click_on_furnace(self, is_running):
        return max(self.smelt_time, gauss(self.smelt_time + 1.6, 0.99123))

    '''
    #############################################################################

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    Validators    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #############################################################################
    Returns:
        True=> Move to next step, False => Repeat step, None=> exit recipie
    '''

    def _v_walk_to_bank(self, client):
        # Code to check for red
        return True

    def _v_click_on_bank(self, client):
        # Code to check for red
        return True

    def _v_withdraw_items(self, client):
        '''
            Check that we have items in the bank, if we dont, exit.
        '''
        return None

    def _v_walk_to_furnace(self, client):
        # Code to check for red
        return True

    def _v_click_on_furnace(self, client):
        # Code to check for red
        return True


if __name__ == "__main__":
    # Need to run as a module:
    # python3  -m recipies.r_make_edge_bronze_barsw
    print("hello")
    r = EdgeFurnace()
    print(r)
    r.run()
