from random import gauss
from time import sleep
from search import Search
from spaces import Spaces
from utils import r_mouse_duration, rr
import pyautogui


class Map:

    @classmethod
    def move_map_deg(cls, client, degs):
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

            Pretty BROKEN, lets just use Spaces.PLAYER_MED as a starting point,
            draw from there to whereever......


        90degress = delta x = +274  N -> E      
        '''
        print("Moving map degs: ", degs)
        deg_to_x_factor = 2.92

        deg_90_dist = int(degs * deg_to_x_factor)
        dims = client.dims
        x_offset = dims[0] + 50
        y_offset = dims[1] + 50
        w = dims[2] - 300
        h = dims[3] - 200

        margin = abs(deg_90_dist)
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
    @classmethod
    def move_map_pitch(cls, client, percentage: int):
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

    @classmethod
    def zoom_map(cls, client, deg):
        one = 1 if deg > 0 else -1
        # Move mouse somewhere in
        x, y = Search.click_interface(client, Spaces.NORTH)
        pyautogui.scroll(one, x=x, y=y)
        sleep(max(.1, gauss(.25, .08)))
        for _ in range(deg):
            pyautogui.scroll(one)
            sleep(max(.1, gauss(.25, .08)))
