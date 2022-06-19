from random import gauss
from time import sleep
from utils import rr, Map
from Spaces import Spaces
from Search import Search
from Items import Items
from Colors import Colors
from PyKey import PyKey

'''  The client has a pos_x and pos_y indicating the top left corner  


    client.dims = [pos_x, pos_y, width, height]

'''


CHAT_PAUSE = 1.1


def click_gilinor_guide(client):
    ''' Starting from somewhere in 1st house, lookfor 'FFFF0000' and click him 

    NPC Indicators
    '''
    pt = Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.NPC_PURPLE)
    Search.click(pt)

    sleep(1)

    while not Search.chat_head_showing(client):
        pt = Search.search_space_color(
            client, Spaces.PLAYER_CENTER_LG, Colors.NPC_PURPLE)
        Search.click(pt)
        sleep(gauss(.6, .15))


def talk_up_to_setting_icon(client):

    # First press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # Second press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # 3 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # 4 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # 5 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # CHoose option
    PyKey.press(PyKey.TWO)
    sleep(gauss(CHAT_PAUSE, .12))

    # 1 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # 2 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    # 5 press
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))


def click_settings_icon(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_SETTINGS))


def talk_up_to_door(client):
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))


def click_on_door(client):
    Search.click(Search.search_space_color(client, Spaces.E_B, Colors.Red))
    sleep(1.2)


def walk_to_fish(client):
    '''
        692, 121
        711, 145

        Fish spot on minimap
    '''
    Search.click(Search.click_interface(
        client, Spaces.TUT_ISLAND_MINI_MAP_FISH_SPOT))
    sleep(10)


def talk_survival_expert_1(client):
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))


def click_INV(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_INV))
    sleep(1)


def click_shrimp(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Cyan))
    sleep(3)

    # while Search.search_space_item(client, Spaces.INV, Items.RAW_SHRIMP) is None:
    #     Search.click(Search.search_space_color(client, Spaces.PLAYER_CENTER_LG, Colors.Cyan))
    #     sleep(5)


def click_skills_panel(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_SKILLS))
    sleep(1)


def talk_until_wc(client):
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))

    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE, .12))


def click_tree(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_MED, Colors.Green))


def make_fire(client):
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.TINDERBOX))
    sleep(.6)
    Search.click(Search.search_space_item(client, Spaces.INV, Items.LOGS))


def cook_shrimp(client):
    # Click Shrimp
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.RAW_SHRIMP))
    # Click Fire
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_MED, Colors.LOGS_ON_FIRE))


def walk_east_to_yellow(client):
    Search.click(Search.search_space_color(client, Spaces.WEST, Colors.Yellow))


def walk_east_to_red_gate(client):
    Search.click(Search.search_space_color(client, Spaces.WEST, Colors.Red))


def turn_and_click_door(client):
    Map.move_map_deg(client, -90)
    Search.click(Search.search_space_color(client, Spaces.WEST, Colors.Red))


'''
----------





---------
'''
#  ###############   Sleeps    ##############################


def click_gilinor_guide_sleep(is_running):
    return max(1, gauss(1.6, .5))


def talk_up_to_setting_icon_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_settings_icon_sleep(is_running):
    return max(1, gauss(1.6, .5))


def talk_up_to_door_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_on_door_sleep(is_running):
    return max(1, gauss(1.6, .5))


def walk_to_fish_sleep(is_running):
    return max(1, gauss(1.6, .5))


def talk_survival_expert_1_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_INV_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_shrimp_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_skills_panel_sleep(is_running):
    return max(1, gauss(1.6, .5))


def talk_until_wc_sleep(is_running):
    return max(1, gauss(1.6, .5))


def click_tree_sleep(is_running):
    return max(1, gauss(1.6, .5))


def make_fire_sleep(is_running):
    return max(1, gauss(1.6, .5))


def cook_shrimp_sleep(is_running):
    return max(1, gauss(1.6, .5))


def walk_to_gate_sleep(is_running):
    return max(1, gauss(1.6, .5))


def walk_east_to_yellow_sleep(is_running):
    return max(4, gauss(4.6, .5))


def walk_east_to_red_gate_sleep(is_running):
    return max(4, gauss(4.6, .5))


def turn_and_click_door_sleep(is_running):
    return max(4, gauss(4.6, .5))


RECIPIE = {
    'fns': [
        # click_gilinor_guide,
        # talk_up_to_setting_icon,
        # click_settings_icon,
        # click_gilinor_guide,
        # talk_up_to_door,
        # click_on_door,
        # walk_to_fish,
        # click_gilinor_guide,  # Survival Expert.
        # talk_survival_expert_1,
        # click_INV,
        # click_shrimp,
        # click_skills_panel,
        # click_gilinor_guide,  # Survival Expert.
        # talk_until_wc,
        # click_tree,
        # make_fire,
        # cook_shrimp,
        # walk_east_to_yellow,
        # walk_east_to_red_gate,
        # walk_east_to_yellow,
        # turn_and_click_door,
        click_gilinor_guide,  # Master Chef.
    ],
    # ----------------------------------------------------------------------------------------
    'sleeps': [
        # click_gilinor_guide_sleep,
        # talk_up_to_setting_icon_sleep,
        # click_settings_icon_sleep,
        # click_gilinor_guide_sleep,
        # talk_up_to_door_sleep,
        # click_on_door_sleep,
        # walk_to_fish_sleep,
        # click_gilinor_guide_sleep,
        # talk_survival_expert_1_sleep,
        # click_INV_sleep,
        # click_shrimp_sleep,
        # click_skills_panel_sleep,
        # click_gilinor_guide_sleep,
        # talk_until_wc_sleep,
        # click_tree_sleep,
        # make_fire_sleep,
        # cook_shrimp_sleep,
        # walk_to_gate_sleep,
        # walk_east_to_yellow_sleep,
        # walk_east_to_red_gate_sleep,
        # walk_east_to_yellow_sleep,
        # turn_and_click_door_sleep,
        click_gilinor_guide_sleep
    ]

}
