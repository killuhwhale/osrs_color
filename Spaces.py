from enum import Enum
from itertools import chain
from random import gauss
from PIL import Image
from PIL.Image import Image as PILImage
import pyautogui


from DEFAULT_SPACES import DEFAULT_SPACES
from ANDAYA_SPACES import ANDAYA92_SPACES
from KAMS_SPACES import KAMS_SPACES

from config import WINDOW_TOP_MARGIN
from osrs import OsrsClient
from utils import rr, Constant


class Spaces(ANDAYA92_SPACES, KAMS_SPACES, DEFAULT_SPACES):
    # _ignore_ = 'member cls'
    # cls = vars()
    # for member in chain(list(KAMS_SPACES), list(ANDAYA92_SPACES), list(DEFAULT_SPACES)):
    #     cls[member.name] = member.value

    ''' Skill Spaces
        15x12

        Interface Spaces
        20x20

        Prayer icons
        33x33

        Item Image for Search 
        40x40

    '''

    SPACES = dict()
    SPACES.update(KAMS_SPACES.SPACES)
    SPACES.update(ANDAYA92_SPACES.SPACES)
    SPACES.update(DEFAULT_SPACES.SPACES)

    @classmethod
    def get_space(cls, client: OsrsClient, space) -> tuple[PILImage, int, int]:
        ''' Returns Image and offset of image (x, y), relative to client.
            img, x_offset, y_offset
        '''
        x, y, x1, y1 = cls.SPACES[space]
        return cls._crop_screen_pos(client.dims, x, y, x1, y1)

    @classmethod
    def get_bounds(cls, client: OsrsClient, space) -> tuple[int, int, int, int]:
        ''' Get bounds for a certain space. Adjusted to Client and OS window margins.

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
        # clickx = rr(x_offset_adj, x_offset_adj + w)
        # clicky = rr(y_offset_adj + PA,
        #             y_offset_adj + h + PA)

        return (x_offset_adj, y_offset_adj + PA, w, h)

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
    def _crop_screen_pos(cls, dims: list, x_offset, y_offset, x1_offset, y1_offset, name=None) -> tuple[PILImage, int, int]:
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
        return (
            cls._screen_image(
                x_offset_adj,
                y_offset_adj + PA,
                x_offset_adj + w,
                y_offset_adj + h + PA,
                name
            ),
            x_offset_adj, y_offset_adj + PA
        )
