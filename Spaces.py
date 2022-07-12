from PIL import Image
from PIL.Image import Image as PILImage
import pyautogui

from typing import Tuple, List
from spaces_default import DEFAULT_SPACES
from spaces_andaya import ANDAYA92_SPACES
from spaces_kam import KAMS_SPACES

from config import WINDOW_TOP_MARGIN
from osrs_client import OsrsClient


class Spaces(ANDAYA92_SPACES, KAMS_SPACES, DEFAULT_SPACES):

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
    def get_space(cls, client: OsrsClient, space) -> Tuple[PILImage, int, int]:
        ''' Returns Image and offset of image (x, y), relative to client.
            img, x_offset, y_offset
        '''
        return cls._crop_screen_pos(client, cls.SPACES[space])

    @classmethod
    def get_bounds(cls, client: OsrsClient, space) -> Tuple[int, int, int, int]:
        ''' Get bounds for a certain space. Adjusted to Client and OS window margins.
            BOUNDS == x,y,w,h
            COORDS == x,y,x1,y1
        '''
        x, y, x1, y1 = cls._translate_raw_coords(client, cls.SPACES[space])
        return (x, y, x1-x, y1-y)

    @classmethod
    def get_bounds_from_raw_coords(cls, client: OsrsClient, raw_space) -> Tuple[int, int, int, int]:
        ''' Get bounds for a certain space given raw coords, [x,y,x1,y1]
            Adjusted to Client and OS window margins.
            BOUNDS == x,y,w,h
            COORDS == x,y,x1,y1
        '''

        x, y, x1, y1 = cls._translate_raw_coords(client, raw_space)
        return (x, y, x1-x, y1-y)

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
    def _crop_screen_pos(cls, client: OsrsClient, raw_coords: List, name=None) -> Tuple[PILImage, int, int]:
        ''' Given the Relative Top Left(x,y) and BottomRight(x1, y1) corners, return the cropped image w/ its TL corner offset.

            Returns [img, x_offset, y_offset]

        '''

        x, y, x1, y1 = cls._translate_raw_coords(client, raw_coords)
        return (
            cls._screen_image(x, y, x1, y1, name), x, y
        )

    @classmethod
    def _translate_raw_coords(cls, client: OsrsClient, raw_coords: List) -> Tuple[int, int, int, int]:
        dims = client.dims
        x, y = dims[0], dims[1]
        x_offset, y_offset, x1_offset, y1_offset = raw_coords

        w, h = x1_offset - x_offset, y1_offset - y_offset
        x_offset_adj, y_offset_adj = x_offset + x,  y_offset + \
            y  # Update/adj with client top left corner
        # print(f"Client top left: {x}, {y}")
        # print(f"SS top left: {x_offset_adj}, {y_offset_adj}")

        # SCREEN_TOP_MARGIN + is already added to Client Position...
        PA = WINDOW_TOP_MARGIN
        return (
            x_offset_adj,
            y_offset_adj + PA,
            x_offset_adj + w,
            y_offset_adj + h + PA,
        )
