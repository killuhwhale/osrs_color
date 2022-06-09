from random import gauss, randrange
from subprocess import Popen, PIPE, run
from time import sleep
from tokenize import String
import pyautogui
from PIL import Image
# import numpy as np
from enum import Enum
from osrs import OsrsClient
from config import PLATFORM, OS_LINUX, OS_WIN, OS_MAC, SCREEN_TOP_MARGIN, WINDOW_TOP_MARGIN


class Durations(Enum):
    EX_SHORT = 1
    V_SHORT = 2
    SHORT = 3
    MED = 4
    LONG = 5


class Spaces(Enum):
    INV = 1
    ROW_1 = 2
    ROW_2 = 3
    ROW_3 = 4
    ROW_4 = 5
    ROW_5 = 6
    ROW_6 = 7
    ROW_7 = 8
    COL_1 = 9
    COL_2 = 10
    COL_3 = 11
    COL_4 = 12
    N_A = 13   # North A (closer to player)
    N_B = 14   # North B (outside North A)
    E_A = 15
    E_B = 16
    S_A = 17
    S_B = 18
    W_A = 19
    W_B = 20


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


def screen_image(left=0, top=0, right=0, bottom=0, name='screenshot.png') -> Image:
    '''
        Given the screen postions of ea corner, returns an Image of the screen region.
    '''
    myScreenshot: Image = pyautogui.screenshot(
        'test.png', region=(left, top, (right - left), (bottom - top)))
    print(f"SS@: {(left, top), {((right - left), (bottom - top))}}")
    return myScreenshot


def load_img(name):
    ''' Lods image from disk '''
    return Image.open(f'needles/{name}')


def crop_screen_pos(dims, x_offset, y_offset, x1_offset, y1_offset):
    '''

    '''
    x, y = dims[0], dims[1]
    w, h = x1_offset - x_offset, y1_offset - y_offset

    # Update/adj with client top left corner
    x_offset_adj, y_offset_adj = x_offset + x,  y_offset + y

    PA = SCREEN_TOP_MARGIN + WINDOW_TOP_MARGIN
    print(f"Platform adjustment: {PA}")
    return [screen_image(x_offset_adj, y_offset_adj + (PA//2), x_offset_adj + w,
                         y_offset_adj + (PA//2) + h, ''), x_offset_adj, y_offset_adj + (PA//2)]


def crop_inventory(client: OsrsClient):
    """Crops the screenshot of the window to the Inventory.
    Maps screen coords to Image coords

    x_offset = 397 + client.x
    y_offset = 259 + client.y

    ------------------------------------------------------------------------------------------------------------
    | dims[0], dims[1]                                                                                          |
    |                                                                                                           |
    |                                                                                                           |
    |  (397, -820)> ------------------------------------------------------                                      |                  
    |               |  w = 182   h = 265  **Represents Inventoy**         |                                     |
    |               |                                                     |                                     |
    |               |                                                     |                                     |
    |               |                                                     |                                     |
    |               |                                                     |                                     |
    |               ------------------------------------------------------   < (579, -555)                      |
    |                                                                                                           |
    |                                                       x_offset + w                                        |
    |                                                       y_offset + h                                        |
    |                                                                                                           |
    |                                                                                                           |
    ------------------------------------------------------------------------------------------------------------
    """
    return crop_screen_pos(client.dims, 560, 210, 725, 462)


def crop_inv_row_1(client: OsrsClient):
    '''
    641, 266
    804, 298
    '''
    return crop_screen_pos(client.dims, 560, 210, 725, 250)


def crop_inv_row_2(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 250, 725, 285)


def crop_inv_row_3(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 285, 725, 320)


def crop_inv_row_4(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 320, 725, 355)


def crop_inv_row_5(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 355, 725, 390)


def crop_inv_row_6(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 390, 725, 425)


def crop_inv_row_7(client: OsrsClient):
    #                                    x         x1
    return crop_screen_pos(client.dims, 560, 425, 725, 460)


def crop_inv_col_1(client: OsrsClient):
    #                                         y         y1
    return crop_screen_pos(client.dims, 640, 265, 680, 515)


def crop_inv_col_2(client: OsrsClient):
    #                                         y         y1
    return crop_screen_pos(client.dims, 680, 265, 720, 515)


def crop_inv_col_3(client: OsrsClient):
    #                                         y         y1
    return crop_screen_pos(client.dims, 720, 265, 765, 515)


def crop_inv_col_4(client: OsrsClient):
    #                                         y         y1
    return crop_screen_pos(client.dims, 765, 265, 805, 515)


def crop_north_a(client: OsrsClient):
    '''
    100, 95

    -----------, 155-----------------

                            578, 215

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 100, 155, 578, 215)  # north


def crop_north_b(client: OsrsClient):
    '''
    100, 95

    -------------------------------

                            578, 215

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 100, 95, 578, 155)  # top North b


def crop_east_a(client: OsrsClient):
    '''
    345, 63

    -------------460, ------------------

                            576, 388

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 345, 63, 460, 388)  # east  a


def crop_east_b(client: OsrsClient):
    '''
    345, 63

    -------------231, ------------------

                            576, 388

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 460, 63, 576, 388)  # east  b


def crop_south_a(client: OsrsClient):
    '''
    105, 214



    -------------,301 ------------------

                            577, 388

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 105, 214, 577, 301)  # south  a


def crop_south_b(client: OsrsClient):
    '''
    105, 214



    -------------,301 ------------------

                            577, 388

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 105, 301, 577, 388)  # south  b


def crop_west_a(client: OsrsClient):
    '''
    103, 94

    -------------224, ------------------

                            346, 389

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 224, 94, 346, 389)  # west  a


def crop_west_b(client: OsrsClient):
    '''
    103, 94

    -------------224, ------------------

                            346, 389

    '''
    #                                         y         y1
    return crop_screen_pos(client.dims, 103, 94, 224, 389)  # west  b


def locate(needle: Image, hay: Image, grayscale=True, confidence=0.69):

    print(f"Needle size: {needle}")
    print(f"Hay size: {hay}")
    return pyautogui.locate(needle, hay, grayscale=grayscale,  confidence=confidence)


def translate_bounds_randomly(bounds: tuple, x_offset: int, y_offset: int):
    '''
    The top left of the image is being reported at y = 235 but is really at y = 215, d = -20

    Top of inv        -------------------
    item top          -------------------   
    bounds top        -------------------
    bounds bottom     -------------------
    item bottom       -------------------

    '''

    left = bounds[0]
    top = bounds[1]
    width = bounds[2]
    height = bounds[3]
    print("Bounds", bounds)
    print(f"TOp Left of image: {x_offset}, {y_offset}")
    x_left = x_offset + left
    y_top = y_offset + top

    x_right = x_left + width
    y_bottom = y_top + height

    print(f"Click x between {(x_left, x_right)} and y {(y_top, y_bottom)}")
    click_x = rr(x_left, x_right)
    click_y = rr(y_top, y_bottom)
    print(f"Clickk between {click_x} and {click_y}")
    return (click_x, click_y)


def get_space(client, space):
    if space == Spaces.INV:
        return crop_inventory(client)
    if space == Spaces.ROW_1:
        return crop_inv_row_1(client)
    if space == Spaces.ROW_2:
        return crop_inv_row_2(client)
    if space == Spaces.ROW_3:
        return crop_inv_row_3(client)
    if space == Spaces.ROW_4:
        return crop_inv_row_4(client)
    if space == Spaces.ROW_5:
        return crop_inv_row_5(client)
    if space == Spaces.ROW_6:
        return crop_inv_row_6(client)
    if space == Spaces.ROW_7:
        return crop_inv_row_7(client)
    if space == Spaces.COL_1:
        return crop_inv_col_1(client)
    if space == Spaces.COL_2:
        return crop_inv_col_2(client)
    if space == Spaces.COL_3:
        return crop_inv_col_3(client)
    if space == Spaces.COL_4:
        return crop_inv_col_4(client)
    if space == Spaces.N_A:
        return crop_north_a(client)
    if space == Spaces.N_B:
        return crop_north_b(client)
    if space == Spaces.E_A:
        return crop_east_a(client)
    if space == Spaces.E_B:
        return crop_east_b(client)
    if space == Spaces.S_A:
        return crop_south_a(client)
    if space == Spaces.S_B:
        return crop_south_b(client)
    if space == Spaces.W_A:
        return crop_west_a(client)
    if space == Spaces.W_B:
        return crop_west_b(client)


def search_and_click(client: OsrsClient, space: Spaces, item: String, grayscale=True, confidence=0.69):
    x, y = search_space(client, space, item, grayscale, confidence)
    if x is None:
        return None
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Entry, call from client


def search_space(client: OsrsClient, space: Spaces, item: String, grayscale=True, confidence=0.69):
    '''
        Search a space for an item
    '''
    search_space, x_offset, y_offset = get_space(client, space)

    # Img of inventory
    needle = load_img(item)

    # 4-integer tuple: (left, top, width, height)
    bounds = locate(needle, search_space, grayscale, confidence)
    if bounds is None:
        retries = 5
        while bounds is None and retries > 0:
            print(
                f"Image not found, retrying: {retries} more times")
            bounds = locate(needle, search_space, grayscale, confidence)
            retries -= 1
            sleep(.5)

        if bounds is None:
            return None, None

    x, y = translate_bounds_randomly(bounds, x_offset, y_offset)
    return x, y


def r_mouse_duration(dur=None):
    # If duration not given choose randomly
    if dur is None:
        dur = max(0.175, gauss(0.1, 0.6))
        print(f"Duration is {dur}")
        return dur

    if dur == Durations.EX_SHORT:
        return gauss(0.2, 0.6)
    if dur == Durations.V_SHORT:
        return gauss(0.3, 0.1)
    if dur == Durations.SHORT:
        return gauss(0.4, 0.133)
    if dur == Durations.MED:
        return gauss(0.5, 0.15)
    if dur == Durations.LONG:
        return gauss(0.6, 0.175)


def reset_map(client):
    '''
    629, 65
    649, 86
    '''

    x, y = rr(629, 649), rr(65, 86)
    pyautogui.moveTo(x, y, duration=r_mouse_duration())
    pyautogui.click()


def move_map_deg(client, degs):
    '''
    352, 302
    626, 296

    w = client.doms[2]
    h = client.doms[3]
    rr(  )

    deg_90_dist = 10
    (dims[0], dims[1])
    ___________________________________
    |   |        W                |   |
    |   |<-  w- 2 * deg_90_dist ->|   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    -----------------------------------

    90degress = delta x = +274  N -> E      
    '''
    deg_to_x_factor = 2.92

    deg_90_dist = int(degs * deg_to_x_factor)
    dims = client.dims
    x_offset = dims[0]
    y_offset = dims[1]
    w = dims[2]
    h = dims[3]

    margin = deg_90_dist
    inner_width = w - (2 * deg_90_dist)

    first_point_x = rr(x_offset + margin,  x_offset + margin + inner_width)
    first_point_y = rr(y_offset,  y_offset + h)

    second_point_x = first_point_x + deg_90_dist
    second_point_y = first_point_y

    pyautogui.moveTo(first_point_x, first_point_y, duration=r_mouse_duration())
    pyautogui.dragTo(second_point_x, second_point_y,
                     button='middle', duration=r_mouse_duration())

# Yaw, plane looks left and right


def move_map_deg(client, degs):
    '''
    352, 302
    626, 296

    w = client.doms[2]
    h = client.doms[3]
    rr(  )

    deg_90_dist = 10
    (dims[0], dims[1])
    ___________________________________
    |   |        W                |   |
    |   |<-  w- 2 * deg_90_dist ->|   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    -----------------------------------

    90degress = delta x = +274  N -> E      
    '''
    deg_to_x_factor = 2.92

    deg_90_dist = int(degs * deg_to_x_factor)
    dims = client.dims
    x_offset = dims[0]
    y_offset = dims[1]
    w = dims[2]
    h = dims[3]

    margin = deg_90_dist
    inner_width = w - (2 * deg_90_dist)

    first_point_x = rr(x_offset + margin,  x_offset + inner_width)
    first_point_y = rr(y_offset,  y_offset + h)

    second_point_x = first_point_x + deg_90_dist
    second_point_y = first_point_y

    pyautogui.moveTo(first_point_x, first_point_y, duration=r_mouse_duration())
    pyautogui.dragTo(second_point_x, second_point_y,
                     button='middle', duration=r_mouse_duration())


'''
Runelite window margin = |85( game window )120|

So we can't click anywhere within the clients window....
'''

# Pitch, plance moves up or down


def move_map_pitch(client, percentage: int):
    '''
    Params:
        percentage: 1-100

    338, 223
    335, 36

    w = client.dims[2]
    h = client.dims[3]
    rr(  )

    y_dist = 10
    (dims[0], dims[1])
    ___________________________________
    |   |        W                |   |
    |   |  <-  h- 2 * y_dist ->   |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    |   |                         |   |
    -----------------------------------

    90degress = delta x = +274  
    '''
    pitch_factor = 1.46

    y_dist = int(percentage * pitch_factor)
    dims = client.dims
    x_offset = dims[0]
    y_offset = dims[1]
    w = dims[2]
    h = dims[3]

    '''TODO()
        Need to find bounds of clickable area. Black area on left and right of game window is non responsive 
        
    '''

    margin = y_dist
    inner_height = h - (2 * y_dist)

    first_point_x = rr(x_offset,  x_offset + w)
    first_point_y = rr(y_offset + margin,  y_offset + margin + inner_height)

    second_point_x = first_point_x + int(gauss(5, 2))
    second_point_y = first_point_y + y_dist

    pyautogui.moveTo(first_point_x, first_point_y, duration=r_mouse_duration())
    pyautogui.dragTo(second_point_x, second_point_y,
                     button='middle', duration=r_mouse_duration())
