from enum import Enum
from PIL import Image
import pyautogui

from config import WINDOW_TOP_MARGIN
from osrs import OsrsClient
from utils import rr


class Spaces:
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
    INTF_HP = 21
    INTF_PRAYER = 22
    INTF_RUN = 23
    INTF_SPECIAL = 24
    SKILL_ATT = 25
    SKILL_STR = 26
    SKILL_DEF = 27
    SKILL_RNG = 28
    SKILL_PRY = 29
    SKILL_MAG = 30
    SKILL_RC = 31
    SKILL_CON = 32
    SKILL_CUR_HP = 33
    SKILL_CUR_AGL = 34
    SKILL_CUR_HRB = 35
    SKILL_CUR_THV = 36
    SKILL_CUR_CRA = 37
    SKILL_CUR_FLT = 38
    SKILL_CUR_SLA = 39
    SKILL_CUR_HUN = 40
    SKILL_CUR_MIN = 41
    SKILL_CUR_SMT = 42
    SKILL_CUR_FSH = 43
    SKILL_CUR_CK = 44
    SKILL_CUR_FMA = 45
    SKILL_CUR_WC = 46
    SKILL_CUR_FRM = 47
    SKILL_CUR_TLVL = 48

    ''' Skill Spaces
        15x12

        Interface Spaces
        20x20
    '''

    SKILL_WIDTH = 50
    SKILL_HEIGHT = 20

    BASE_SKILL_X = 555
    BASE_SKILL_Y = 211

    SK_VT_MG = 32  # Skill vertical margin
    SK_HZ_MG = 64

    SPACES = {
        INV: [560, 210, 725, 465],
        ROW_1: [560, 210, 725, 250],
        ROW_2: [560, 245, 725, 285],
        ROW_3: [560, 280, 725, 320],
        ROW_4: [560, 315, 725, 355],
        ROW_5: [560, 350, 725, 390],
        ROW_6: [560, 385, 725, 425],
        ROW_7: [560, 425, 725, 465],
        COL_1: [560, 210, 600, 465],
        COL_2: [600, 210, 640, 465],
        COL_3: [642, 210, 683, 465],
        COL_4: [685, 210, 725, 465],
        N_A: [18, 87, 498, 167],
        N_B: [18, 7, 498, 87],
        E_A: [258, 7, 378, 327],
        E_B: [378, 7, 498, 327],
        S_A: [18, 167, 498, 247],
        S_B: [18, 247, 498, 327],
        W_A: [138, 7, 258, 327],
        W_B: [18, 7, 138, 327],

        INTF_HP: [],
        INTF_PRAYER: [],
        INTF_RUN: [530, 115, 550, 135],
        INTF_SPECIAL: [],

        SKILL_ATT: [BASE_SKILL_X, BASE_SKILL_Y, BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + SKILL_HEIGHT],
        SKILL_STR: [BASE_SKILL_X, BASE_SKILL_Y + (1 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (1 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_DEF: [BASE_SKILL_X, BASE_SKILL_Y + (2 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (2 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_RNG: [BASE_SKILL_X, BASE_SKILL_Y + (3 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (3 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_PRY: [BASE_SKILL_X, BASE_SKILL_Y + (7 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (7 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_MAG: [BASE_SKILL_X, BASE_SKILL_Y + (4 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (4 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_RC:  [BASE_SKILL_X, BASE_SKILL_Y + (5 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (5 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CON: [BASE_SKILL_X, BASE_SKILL_Y + (6 * SK_VT_MG), BASE_SKILL_X + SKILL_WIDTH, BASE_SKILL_Y + (6 * SK_VT_MG) + SKILL_HEIGHT],

        SKILL_CUR_HP: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (0 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (0 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_AGL: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (1 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (1 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_HRB: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (2 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (2 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_THV: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (3 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (3 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_CRA: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (4 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (4 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_FLT: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (5 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (5 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_SLA: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (6 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (6 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_HUN: [BASE_SKILL_X + (1 * SK_HZ_MG), BASE_SKILL_Y + (7 * SK_VT_MG), BASE_SKILL_X + (1 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (7 * SK_VT_MG) + SKILL_HEIGHT],

        SKILL_CUR_MIN: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (0 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (0 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_SMT: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (1 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (1 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_FSH: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (2 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (2 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_CK: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (3 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (3 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_FMA: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (4 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (4 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_WC: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (5 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (5 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_FRM: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (6 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (6 * SK_VT_MG) + SKILL_HEIGHT],
        SKILL_CUR_TLVL: [BASE_SKILL_X + (2 * SK_HZ_MG), BASE_SKILL_Y + (7 * SK_VT_MG), BASE_SKILL_X + (2 * SK_HZ_MG) + SKILL_WIDTH, BASE_SKILL_Y + (7 * SK_VT_MG) + SKILL_HEIGHT],

    }

    @classmethod
    def get_space(cls, client, space):
        x, y, x1, y1 = cls.SPACES[space]
        return cls._crop_screen_pos(client.dims, x, y, x1, y1)

    @classmethod
    def get_bounds(cls, client, space):
        ''' Get bounds for a certain space.

        '''
        dims = client.dims
        x, y = dims[0], dims[1]
        x_offset, y_offset, x1_offset, y1_offset = cls.SPACES[space]
        w, h = x1_offset - x_offset, y1_offset - y_offset

        # Update/adj with client top left corner
        x_offset_adj, y_offset_adj = x_offset + x,  y_offset + y

        # print(f"Client top left: {x}, {y}")

        # print(f"SS top left: {x_offset_adj}, {y_offset_adj}")

        # SCREEN_TOP_MARGIN + is already added to Client Position...
        PA = WINDOW_TOP_MARGIN
        # print(f"Platform adjustment: {PA}")

        # return rr(x_offset_adj, x_offset_adj + w), rr(y_offset_adj + PA, y_offset_adj + h + PA)
        clickx, clicky = rr(x_offset_adj, x_offset_adj +
                            w), rr(y_offset_adj + PA, y_offset_adj + h + PA)
        pyautogui.moveTo(clickx, clicky)
        pyautogui.click()
        return clickx, clicky

    @classmethod
    def _screen_image(cls, left=0, top=0, right=0, bottom=0, name=None) -> Image:
        '''
            Given the screen postions of ea corner, returns an Image of the screen region.
        '''
        myScreenshot: Image = pyautogui.screenshot(
            name, region=(left, top, (right - left), (bottom - top)))
        # print(f"SS@: {(left, top), {((right - left), (bottom - top))}}")
        return myScreenshot

    @classmethod
    def _crop_screen_pos(cls, dims, x_offset, y_offset, x1_offset, y1_offset, name=None):
        ''' Returns [img, x_offset, y_offset]

        '''
        x, y = dims[0], dims[1]
        w, h = x1_offset - x_offset, y1_offset - y_offset

        # Update/adj with client top left corner
        x_offset_adj, y_offset_adj = x_offset + x,  y_offset + y

        # print(f"Client top left: {x}, {y}")

        # print(f"SS top left: {x_offset_adj}, {y_offset_adj}")

        # SCREEN_TOP_MARGIN + is already added to Client Position...
        PA = WINDOW_TOP_MARGIN
        # print(f"Platform adjustment: {PA}")
        return [
            cls._screen_image(
                x_offset_adj,
                y_offset_adj + PA,
                x_offset_adj + w,
                y_offset_adj + h + PA,
                name
            ),
            x_offset_adj, y_offset_adj + PA
        ]
