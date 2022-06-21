from random import gauss
from time import sleep
from utils import rr
from Map import Map
from Spaces import Spaces
from Search import Search
from Items import Items
from Colors import Colors
from PyKey import PyKey

'''  The client has a pos_x and pos_y indicating the top left corner  


    client.dims = [pos_x, pos_y, width, height]

'''


CHAT_PAUSE = 1.1


def click_gilinor_guide(client, space=Spaces.PLAYER_CENTER_LG, chat_head_left=True):
    ''' Starting from somewhere in 1st house, lookfor 'FFFF0000' and click him 

    NPC Indicators
    '''
    if Search.chat_head_showing(client):
        return

    pt = Search.search_space_color(
        client, space, Colors.NPC_PURPLE)
    Search.click(pt)

    sleep(3)

    while not Search.chat_head_showing(client, left=chat_head_left):
        pt = Search.search_space_color(
            client, space, Colors.NPC_PURPLE)
        Search.click(pt)
        sleep(gauss(3, 0.5))


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


def talk_cook_until_water_and_dough(client):
    for _ in range(5):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def make_dough(client):
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.POT_OF_FLOUR))
    sleep(.6)
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.BUCKET_OF_WATER))


def make_bread(client):
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.BREAD_DOUGH))
    sleep(.6)
    Map.move_map_deg(client, -90)

    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Cyan))


def leave_kitchen_walk_north(client):
    Search.click(Search.click_interface(client, Spaces.RESET_MAP))
    # Click mini map,
    Search.click(Search.click_interface_from_raw_coords(
        client, [606, 26, 691, 45]))


def leave_kitchen_open_door(client):
    # Click door
    Search.click(Search.search_space_color(client, Spaces.WEST, Colors.Red))


def double_click_run(client):
    Search.click(Search.click_interface(client, Spaces.INTF_RUN))
    sleep(max(.230, gauss(.250, .2)))
    Search.click(Search.click_interface(client, Spaces.INTF_RUN))


def walk_west_to_tile1(client):
    # Click door
    Search.click(Search.search_space_color(
        client, Spaces.WEST, Colors.Yellow))


def walk_north_to_tile2(client):
    # Click door
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Yellow))


def walk_east_to_tile3(client):
    # Click door
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Yellow))


def walk_north_to_tile4(client):
    # Click door
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Yellow))


def open_door_to_quest_guy(client):
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Red))


def click_panel_quest_icon(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_QUESTS))


def talk_quest_guide_until_trapdoor(client):
    for _ in range(6):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_trapdoor(client):
    Map.move_map_deg(client, 180)
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Cyan))


def walk_to_smith_click_mini_map(client):
    Search.click(Search.click_interface(client, Spaces.RESET_MAP))
    Search.click(Search.click_interface_from_raw_coords(
        client, [627, 144, 653, 155]))


def talk_smith_until_mining(client):
    for _ in range(5):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_tin_rock(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Cyan))


def click_copper_rock(client):
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Blue))


def click_furnace(client):
    Search.click(Search.search_space_color(
        client, Spaces.WEST, Colors.Yellow))


def talk_smith_until_make_weapon(client):
    for _ in range(3):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_anvil(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Green))


def click_dagger(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [21, 47, 63, 97]))


def click_combat_gate(client):
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Red))


def click_combat_instructor(client):
    click_gilinor_guide(client, Spaces.EAST)


def talk_smith_until_click_gear(client):
    for _ in range(3):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_panel_gear(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_GEAR))


def click_panel_gear_equipment(client):
    Search.click(Search.click_interface(client, Spaces.GEAR_EQUIPMENT))


def close_equipment(client):
    Search.click(Search.click_interface(client, Spaces.GEAR_EQUIPMENT_CLOSE))


def equip_dagger(client):
    Search.click(Search.search_space_item(
        client, Spaces.INV, Items.BRONZE_DAGGER))


def talk_combatinstructor_until_fight(client):
    for _ in range(2):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def equip_sword_and_shield(client):
    coin_toss = rr(0, 100)
    if coin_toss < 50:
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.BRONZE_SWORD))
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.WOODEN_SHIELD))
    else:
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.WOODEN_SHIELD))
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.BRONZE_SWORD))


def click_panel_combat(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_COMBAT))


def walk_to_rat_tile(client):
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Yellow))


def click_rat_gate(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Red))


def attack_rat_melee(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_MED, Colors.Purple))


def leave_cage_mini_map(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [690, 38, 712, 75]))


def leave_cage_click_door(client):
    Search.click(Search.search_space_color(client, Spaces.EAST, Colors.Red))


def walk_tile_south_to_comabt_instructor(client):
    Search.click(Search.search_space_color(
        client, Spaces.SOUTH, Colors.Yellow))


def walk_south_to_blue(client):
    Search.click(Search.search_space_color(client, Spaces.SOUTH, Colors.Blue))


def click_combat_instructor_south(client):
    click_gilinor_guide(client, Spaces.SOUTH)


def talk_combatinstructor_until_fight_arrows(client):
    for _ in range(4):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_shortbow_and_arrows(client):
    ct = rr(0, 100)
    if ct < 50:
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.SHORTBOW))
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.BRONZE_ARROWS))
    else:
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.BRONZE_ARROWS))
        Search.click(Search.search_space_item(
            client, Spaces.INV, Items.SHORTBOW))


def click_giant_rat_range(client):
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.GIANT_RAT))


def click_ladder_mini_map_exit(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [631, 14, 679, 34]))


def click_ladder_exit(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Cyan))


def walk_to_bank(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [673, 93, 688, 107]))


def click_bank_booth(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Cyan))


def close_bank(client):
    ct = rr(0, 100)
    if ct < 50:
        Search.click(Search.click_interface(client, Spaces.CLOSE_BANK))
    else:
        Search.click(Search.click_interface_from_raw_coords(
            client, [638, 80, 653, 94]))


def click_poll_booth(client):
    Search.click(Search.search_space_color(
        client, Spaces.PLAYER_CENTER_LG, Colors.Blue))


def space_through_poll_chat(client):
    for _ in range(3):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_bank_door(client):
    Map.move_map_deg(client, 90)
    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.Red))


def click_account_guide(client):
    Search.click(Search.click_interface(
        client, Spaces.RESET_MAP))
    click_gilinor_guide(client, chat_head_left=False)


def talk_to_account_guide_until_panel(client):
    for _ in range(5):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE, .12))


def click_panel_account_management(client):
    Search.click(Search.click_interface(client, Spaces.PANEL_ACCOUNT))


def click_account_guide_again(client):
    click_gilinor_guide(client)


def talk_to_account_guide_until_exit(client):
    for _ in range(18):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def click_door_exit_bank_second(client):
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Red))


def walk_south_to_altar(client):
    ct = rr(0, 100)
    if ct < 50:
        Search.click(Search.search_space_color(
            client, Spaces.EAST, Colors.Yellow))
    else:
        Search.click(Search.click_interface_from_raw_coords(
            client, [663, 110, 690, 119]))


def walk_south_to_altar2(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [611, 120, 625, 136]))


def walk_south_to_altar3(client):
    Search.click(Search.search_space_color(
        client, Spaces.WEST, Colors.Yellow))


def click_brother_brace(client):
    click_gilinor_guide(client, chat_head_left=False)


def click_brother_brace_left(client):
    click_gilinor_guide(client)


def talk_brother_until_panel_prayer(client):
    for _ in range(2):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def click_panel_prayer(client):
    Search.click(Search.click_interface(
        client, Spaces.PANEL_PRAYER))


def talk_brother_until_panel_friends(client):
    for _ in range(4):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def click_panel_friends(client):
    Search.click(Search.click_interface(
        client, Spaces.PANEL_FRIENDS))


def talk_brother_until_exit(client):
    for _ in range(4):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def click_prayer_exit_door(client):
    Search.click(Search.search_space_color(
        client, Spaces.SOUTH, Colors.Red))


def walk_to_magic_guy(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [632, 136, 653, 153]))


def walk_to_magic_guy2(client):
    Search.click(Search.search_space_color(
        client, Spaces.EAST, Colors.Yellow))


def click_magic_instructor(client):
    click_gilinor_guide(client, Spaces.EAST, chat_head_left=False)


def talk_to_magic_instructor_until_panel_magic(client):
    for _ in range(2):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def click_panel_magic(client):
    Search.click(Search.click_interface(
        client, Spaces.PANEL_MAGIC))


def click_magic_instructor2(client):
    click_gilinor_guide(client)


def talk_to_magic_instructor_until_air_strike(client):
    for _ in range(2):
        PyKey.press(PyKey.SPACE)
        sleep(gauss(CHAT_PAUSE + 0.250, .12))


def walk_north_to_chickens(client):
    Search.click(Search.search_space_color(client, Spaces.NORTH, Colors.Blue))
    sleep(max(.25, gauss(.5, .3)))
    Map.zoom_map(client, 15)


def cast_air_strike(client):
    Search.click(Search.click_interface_from_raw_coords(
        client, [608, 220, 627, 239]))

    Search.click(Search.search_space_color(
        client, Spaces.NORTH, Colors.CHICKEN_TUT_ISLAND))


def click_to_magic_guy_exit(client):
    Map.zoom_map(client, -20)
    sleep(max(.25, gauss(.5, .3)))
    click_gilinor_guide(client)


def talk_to_magic_instructor_until_exit(client):
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.ONE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    # TODO this is random on each account, 1-3. Recognize random chat options... Pain in the ass. Runelite plugin to see which option is which...
    PyKey.press(PyKey.THREE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))
    PyKey.press(PyKey.SPACE)
    sleep(gauss(CHAT_PAUSE + 0.250, .12))


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


def talk_cook_until_water_and_dough_sleep(is_running):
    return max(4, gauss(4.6, .5))


def make_dough_sleep(is_running):
    return max(4, gauss(4.6, .5))


def make_bread_sleep(is_running):
    return max(4, gauss(4.6, .5))


def leave_kitchen_walk_north_sleep(is_running):
    return max(3.3, gauss(3.6, .5))


def leave_kitchen_open_door_sleep(is_running):
    return max(4, gauss(4.6, .5))


def double_click_run_sleep(is_running):
    return max(1, gauss(1.6, .5))


def walk_west_to_tile1_sleep(is_running):
    return max(3, gauss(3.6, .5))


def walk_north_to_tile2_sleep(is_running):
    return max(3, gauss(3.6, .5))


def walk_east_to_tile3_sleep(is_running):
    return max(3.5, gauss(3.9, .5))


def walk_north_to_tile4_sleep(is_running):
    return max(3.3, gauss(3.7, .5))


def open_door_to_quest_guy_sleep(is_running):
    return max(3.7, gauss(4.3, .5))


def click_panel_quest_icon_sleep(is_running):
    return max(.6, gauss(1, .5))


def talk_quest_guide_until_trapdoor_sleep(is_running):
    return max(.6, gauss(1, .5))


def click_trapdoor_sleep(is_running):
    return max(.6, gauss(1, .5))


def walk_to_smith_click_mini_map_sleep(is_running):
    return max(.6, gauss(1, .5))


def talk_smith_until_mining_sleep(is_running):
    return max(.6, gauss(1, .5))


def click_tin_rock_sleep(is_running):
    return max(7, gauss(7.5, .5))


def click_copper_rock_sleep(is_running):
    return max(7, gauss(7.5, .5))


def click_furnace_sleep(is_running):
    return max(6, gauss(6.5, .5))


def talk_smith_until_make_weapon_sleep(is_running):
    return max(1, gauss(1.5, .5))


def click_anvil_sleep(is_running):
    return max(3.2, gauss(3.7, .5))


def click_dagger_sleep(is_running):
    return max(3.2, gauss(3.7, .5))


def click_combat_gate_sleep(is_running):
    return max(5.2, gauss(5.7, .5))


def click_combat_instructor_sleep(is_running):
    return max(6.2, gauss(6.7, .5))


def click_panel_gear_sleep(is_running):
    return max(1.2, gauss(1.7, .5))


def click_panel_gear_equipment_sleep(is_running):
    return max(5.2, gauss(5.7, .5))


def close_equipment_sleep(is_running):
    return max(1.2, gauss(1.7, .5))


def equip_dagger_sleep(is_running):
    return max(2.2, gauss(2.7, .5))


def talk_combatinstructor_until_fight_sleep(is_running):
    return max(2.2, gauss(2.7, .5))


def equip_sword_and_shield_sleep(is_running):
    return max(2.2, gauss(2.7, .5))


def click_panel_combat_sleep(is_running):
    return max(1.2, gauss(2.7, .5))


def walk_to_rat_tile_sleep(is_running):
    return max(3.2, gauss(3.7, .5))


def click_rat_gate_sleep(is_running):
    return max(1.2, gauss(2.7, .5))


def attack_rat_melee_sleep(is_running):
    return max(20.2, gauss(20.7, 1.5))


def leave_cage_mini_map_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def leave_cage_click_door_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def walk_tile_south_to_comabt_instructor_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def walk_south_to_blue_sleep(is_running):
    return max(1.2, gauss(1.7, 1.5))


def click_combat_instructor_south_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def talk_combatinstructor_until_fight_arrows_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def click_shortbow_and_arrows_sleep(is_running):
    return max(1.2, gauss(1.7, 1.5))


def click_giant_rat_range_sleep(is_running):
    return max(20.2, gauss(20.7, 1.5))


def click_ladder_mini_map_exit_sleep(is_running):
    return max(7.2, gauss(7.7, 1.5))


def click_ladder_exit_sleep(is_running):
    return max(5.2, gauss(5.7, 1.5))


def walk_to_bank_sleep(is_running):
    return max(9.2, gauss(5.7, 1.5))


def click_bank_booth_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def close_bank_sleep(is_running):
    return max(1.2, gauss(1.7, 1.5))


def click_poll_booth_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def space_through_poll_chat_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_bank_door_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_account_guide_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def talk_to_account_guide_until_panel_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_panel_account_management_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_account_guide_again_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def talk_to_account_guide_until_exit_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_door_exit_bank_second_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def walk_south_to_altar_sleep(is_running):
    return max(6.2, gauss(6.7, 1.5))


def walk_south_to_altar2_sleep(is_running):
    return max(9.2, gauss(9.7, 1.5))


def walk_south_to_altar3_sleep(is_running):
    return max(5.2, gauss(5.7, 1.5))


def click_brother_brace_sleep(is_running):
    return max(6.2, gauss(6.7, 1.5))


def talk_brother_until_panel_prayer_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_panel_prayer_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def talk_brother_until_panel_friends_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_panel_friends_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def talk_brother_until_exit_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_prayer_exit_door_sleep(is_running):
    return max(5.2, gauss(5.7, 1.5))


def walk_to_magic_guy_sleep(is_running):
    return max(8.2, gauss(8.7, 1.5))


def walk_to_magic_guy2_sleep(is_running):
    return max(6.2, gauss(6.7, 1.5))


def click_magic_instructor_sleep(is_running):
    return max(5.2, gauss(5.7, 1.5))


def talk_to_magic_instructor_until_panel_magic_sleep(is_running):
    return max(5.2, gauss(5.7, 1.5))


def click_panel_magic_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def click_magic_instructor2_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


def walk_north_to_chickens_sleep(is_running):
    return max(3.2, gauss(3.7, 1.5))


def cast_air_strike_sleep(is_running):
    return max(4.2, gauss(4.7, 1.5))


def click_to_magic_guy_exit_sleep(is_running):
    return max(4.2, gauss(4.7, 1.5))


def talk_to_magic_instructor_until_exit_sleep(is_running):
    return max(2.2, gauss(2.7, 1.5))


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
        # click_gilinor_guide,  # Master Chef.
        # talk_cook_until_water_and_dough,
        # make_dough,
        # make_bread,
        # leave_kitchen_walk_north,
        # leave_kitchen_open_door,
        # double_click_run,
        # walk_west_to_tile1,
        # walk_north_to_tile2,
        # walk_east_to_tile3,
        # walk_north_to_tile4,
        # open_door_to_quest_guy,
        # click_gilinor_guide,  # Quest Guide
        # click_panel_quest_icon,
        # click_gilinor_guide,  # Quest Guide
        # click_trapdoor,
        # walk_to_smith_click_mini_map,
        # click_gilinor_guide,  # Smith instructor
        # talk_smith_until_mining,
        # click_tin_rock,
        # click_copper_rock,
        # click_furnace,
        # click_gilinor_guide,  # Smith instructor
        # talk_smith_until_make_weapon,
        # click_anvil,
        # click_dagger,
        # click_combat_gate,
        # click_combat_instructor,  # Combat instructor
        # click_panel_gear,
        # click_panel_gear_equipment,
        # close_equipment,
        # equip_dagger,
        # click_combat_instructor,  # Combat instructor
        # talk_combatinstructor_until_fight,
        # equip_sword_and_shield,
        # click_panel_combat,
        # walk_to_rat_tile,
        # click_rat_gate,
        # attack_rat_melee,
        # leave_cage_mini_map,
        # leave_cage_click_door,
        # walk_tile_south_to_comabt_instructor,
        # walk_south_to_blue,
        # click_combat_instructor_south,
        # talk_combatinstructor_until_fight_arrows,
        # click_shortbow_and_arrows,
        # click_giant_rat_range,
        # click_ladder_mini_map_exit,
        # click_ladder_exit,
        # walk_to_bank,
        # click_bank_booth,
        # close_bank,
        # click_poll_booth,
        # space_through_poll_chat,
        # close_bank,
        # click_bank_door,
        # click_account_guide,
        # talk_to_account_guide_until_panel,
        # click_panel_account_management,
        # click_account_guide_again,
        # talk_to_account_guide_until_exit,
        # click_door_exit_bank_second,
        # walk_south_to_altar,
        # walk_south_to_altar2,
        # walk_south_to_altar3,
        # click_brother_brace,
        # talk_brother_until_panel_prayer,
        # click_panel_prayer,
        # click_brother_brace_left,
        # talk_brother_until_panel_friends,
        # click_panel_friends,
        # click_brother_brace_left,
        # talk_brother_until_exit,
        # click_prayer_exit_door,
        # walk_to_magic_guy,
        # walk_to_magic_guy2,
        # click_magic_instructor,
        # talk_to_magic_instructor_until_panel_magic,
        # click_panel_magic,
        # click_magic_instructor2,
        walk_north_to_chickens,
        cast_air_strike,
        click_to_magic_guy_exit,
        talk_to_magic_instructor_until_exit,


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
        # click_gilinor_guide_sleep,
        # talk_cook_until_water_and_dough_sleep,
        # make_dough_sleep,
        # make_bread_sleep,
        # leave_kitchen_walk_north_sleep,
        # leave_kitchen_open_door_sleep,
        # double_click_run_sleep,
        # walk_west_to_tile1_sleep,
        # walk_north_to_tile2_sleep,
        # walk_east_to_tile3_sleep,
        # walk_north_to_tile4_sleep,
        # open_door_to_quest_guy_sleep,
        # click_gilinor_guide_sleep,
        # click_panel_quest_icon_sleep,
        # click_gilinor_guide_sleep,
        # click_trapdoor_sleep,
        # walk_to_smith_click_mini_map_sleep,
        # click_gilinor_guide_sleep,
        # talk_smith_until_mining_sleep,
        # click_tin_rock_sleep,
        # click_copper_rock_sleep,
        # click_furnace_sleep,
        # click_gilinor_guide_sleep,
        # talk_smith_until_make_weapon_sleep,
        # click_anvil_sleep,
        # click_dagger_sleep,
        # click_combat_gate_sleep,
        # click_combat_instructor_sleep,
        # click_panel_gear_sleep,
        # click_panel_gear_equipment_sleep,
        # close_equipment_sleep,
        # equip_dagger_sleep,
        # click_combat_instructor_sleep,
        # talk_combatinstructor_until_fight_sleep,
        # equip_sword_and_shield_sleep,
        # click_panel_combat_sleep,
        # walk_to_rat_tile_sleep,
        # click_rat_gate_sleep,
        # attack_rat_melee_sleep,
        # leave_cage_mini_map_sleep,
        # leave_cage_click_door_sleep,
        # walk_tile_south_to_comabt_instructor_sleep,
        # walk_south_to_blue_sleep,
        # click_combat_instructor_south_sleep,
        # talk_combatinstructor_until_fight_arrows_sleep,
        # click_shortbow_and_arrows_sleep,
        # click_giant_rat_range_sleep,
        # click_ladder_mini_map_exit_sleep,
        # click_ladder_exit_sleep,
        # walk_to_bank_sleep,
        # click_bank_booth_sleep,
        # close_bank_sleep,
        # click_poll_booth_sleep,
        # space_through_poll_chat_sleep,
        # close_bank_sleep,
        # click_bank_door_sleep,
        # click_account_guide_sleep,
        # talk_to_account_guide_until_panel_sleep,
        # click_panel_account_management_sleep,
        # click_account_guide_again,
        # talk_to_account_guide_until_exit_sleep,
        # click_door_exit_bank_second_sleep,
        # walk_south_to_altar_sleep,
        # walk_south_to_altar2_sleep,
        # walk_south_to_altar3_sleep,
        # click_brother_brace_sleep,
        # talk_brother_until_panel_prayer_sleep,
        # click_panel_prayer_sleep,
        # click_brother_brace_sleep,
        # talk_brother_until_panel_friends_sleep,
        # click_panel_friends_sleep,
        # click_brother_brace_sleep,
        # talk_brother_until_exit_sleep,
        # click_prayer_exit_door_sleep,
        # walk_to_magic_guy_sleep,
        # walk_to_magic_guy2_sleep,
        # click_magic_instructor_sleep,
        # talk_to_magic_instructor_until_panel_magic,
        # click_panel_magic_sleep,
        # click_magic_instructor2_sleep,
        walk_north_to_chickens_sleep,
        cast_air_strike_sleep,
        click_to_magic_guy_exit_sleep,
        talk_to_magic_instructor_until_exit_sleep,


    ]

}
