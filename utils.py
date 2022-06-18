from random import gauss, randrange
from subprocess import Popen, PIPE, run
from time import sleep

from enum import Enum


class Durations(Enum):
    EX_SHORT = 1
    V_SHORT = 2
    SHORT = 3
    MED = 4
    LONG = 5


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
    return randrange(min(a, b), max(a, b))


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


class Map:
    def __init__(self):
        pass

    def reset_map(self, client):
        '''
        629, 65
        649, 86
        '''

        x, y = rr(629, 649), rr(65, 86)
        pyautogui.moveTo(x, y, duration=r_mouse_duration())
        pyautogui.click()

    def move_map_deg(self, client, degs):
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

        pyautogui.moveTo(first_point_x, first_point_y,
                         duration=r_mouse_duration())
        pyautogui.dragTo(second_point_x, second_point_y,
                         button='middle', duration=r_mouse_duration())

    '''
    Runelite window margin = |85( game window )120|

    So we can't click anywhere within the clients window....
    '''
    # Pitch, plance moves up or down

    def move_map_pitch(self, client, percentage: int):
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
        first_point_y = rr(y_offset + margin,  y_offset +
                           margin + inner_height)

        second_point_x = first_point_x + int(gauss(5, 2))
        second_point_y = first_point_y + y_dist

        pyautogui.moveTo(first_point_x, first_point_y,
                         duration=r_mouse_duration())
        pyautogui.dragTo(second_point_x, second_point_y,
                         button='middle', duration=r_mouse_duration())
