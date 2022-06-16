
import cv2
import numpy as np
from PIL import Image
import pyautogui
from time import sleep

from osrs import OsrsClient
from Spaces import Spaces
from utils import rr


def imshow(img: Image):
    cv2.imshow("imshow", np.array(img.convert('RGB')))
    cv2.moveWindow("imshow", 1000, 30)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
Open Interface

Equipment Interface
- open stats, prices, death, follower

- head cape neck quiver 
    weapon body shield legs gloves boots ring
    - Check if empty
    - Click on spot

Prayer

- click prayer
- check if prayer on]

Magic

Select spells


Combat
    - 4 quads
    - 1 col of 3
    - auto retaliate


'''


class Search:
    ''' Returns random range between a and b. '''

    # Image Assets, hay images used in template matching to "OCR" numbers
    HORIZONTAL_RUN_IMG = None  # Run interface numvers, prayer, health, special. 0 - 100
    HORIZONTAL_SKILL_IMG = None  # Skills interface numbers = 1 - 99
    HORIZONTAL_RUN_IMG_PATH = "horiImgs/hori_run.png"
    HORIZONTAL_SKILL_IMG_PATH = "horiImgs/hori_run_mask.png"

    @classmethod
    def search_run(cls, client) -> int:
        ''' 
            Takes a screen shot and returns the value as an int
        '''
        cls.HORIZONTAL_RUN_IMG = Image.open(
            cls.HORIZONTAL_RUN_IMG_PATH) if cls.HORIZONTAL_RUN_IMG is None else cls.HORIZONTAL_RUN_IMG
        img, offset_x, offset_y = Spaces.get_space(client, Spaces.INTF_RUN)

        # imshow(cls.HORIZONTAL_RUN_IMG)
        bounds = pyautogui.locate(img, cls.HORIZONTAL_RUN_IMG,
                                  grayscale=False,  confidence=.92)  # 98 - 90,    63 -> 71 - None
        if bounds is None:
            bounds = [-1]
        return bounds[0] // 20

    @classmethod
    def search_skill_lvl(cls, client: OsrsClient, skillSpace: Spaces) -> int:
        '''
            Given a skillSpace, return current skill lvl
            Probably not very useful honestly, just need to know where to click on skill....
            If we want to know the lvls we can probabably do an http request.
        '''
        return Spaces.get_bounds(client, skillSpace)

    @classmethod
    def search_space_item(cls, client: OsrsClient, space: Spaces, item: str, grayscale=True, confidence=0.69):
        '''
            Search a space for an item
        '''
        search_space, x_offset, y_offset = Spaces.get_space(client, space)

        # Img of inventory
        needle = cls._load_img(item)

        # 4-integer tuple: (left, top, width, height)
        bounds = cls._locate(needle, search_space, grayscale, confidence)
        if bounds is None:
            # retries = 5  TODO() Change back
            retries = 0
            while bounds is None and retries > 0:
                print(
                    f"Image not found, retrying: {retries} more times")
                bounds = cls._locate(
                    needle, search_space, grayscale, confidence)
                retries -= 1
                sleep(.5)

            if bounds is None:
                return None, None

        return cls._translate_bounds_randomly(bounds, x_offset, y_offset)

    @classmethod
    def search_space_color(cls, client: OsrsClient, space: Spaces, color: list, grayscale=True, confidence=0.69):
        '''
            Search a space for an item
        '''
        # Offset from space
        search_space, x_offset, y_offset = Spaces.get_space(client, space)

        color = [279, 82, 93]
        # 4-integer tuple: (left, top, width, height)
        # Offset from image
        bounds = cls._locate_color(
            color, color, search_space, grayscale, confidence)

        return cls._translate_bounds_randomly(bounds, x_offset, y_offset)

    @classmethod
    def _locate(cls, needle: Image, hay: Image, grayscale=True, confidence=0.69):

        print(f"Needle size: {needle}")
        print(f"Hay size: {hay}")
        return pyautogui.locate(needle, hay, grayscale=grayscale,  confidence=confidence)

    @classmethod
    def _translate_bounds_randomly(cls, bounds: tuple, x_offset: int, y_offset: int):
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

    @classmethod
    def _transform_img_blk_white_skill(cls, img: Image) -> Image:
        '''
            Set to transform skill Screenshots to black and white.
        '''
        np_img = np.array(img.convert("RGB"))
        hsv = cv2.cvtColor(np_img, cv2.COLOR_RGB2HSV)
        # (0, 254, 0)  -   (115, 255, 255)
        color_range_low = np.array([0, 254, 0])
        color_range_high = np.array([115, 255, 255])

        mask = cv2.inRange(hsv, color_range_low, color_range_high)
        cv2.imshow("Org", np_img)
        # cv2.imshow("HSV", hsv)
        cv2.imshow("blkwhite mask", mask)
        cv2.moveWindow("blkwhite mask", 1000, 30)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return Image.fromarray(mask)

    @classmethod
    def _locate_color(cls, color_low: list, color_high: list, search_space: Image, grayscale: bool, confidence: float) -> tuple:

        # CV2 to locate a color
        # Convert Space to HSV color space
        img = np.asarray(search_space)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        color_range_low = color_low
        color_range_high = color_high

        color_range_low = np.array([107, 209, 23])
        color_range_high = np.array([180, 210, 238])
        # color_range_low = np.array([30, 254, 254])
        # color_range_high = np.array([62, 255, 255])
        # Threshold the HSV image to get only red colors
        mask = cv2.inRange(hsv, color_range_low, color_range_high)

        cv2.imshow('mask', mask)
        cv2.waitKey(0)
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # TODO() sort and choose largest bound.
        bounds = cv2.boundingRect(contours[0])
        x, y, w, h = bounds
        print(f"Top left {(x, y)} w: {w}  h: {h}")

        # Draw and show contours
        boximg = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
        cv2.imshow('img', img)
        cv2.imshow('mask', mask)
        cv2.imshow('res', boximg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return bounds

    @classmethod
    def _load_img(cls, name):
        ''' Lods image from disk '''
        return Image.open(f'needles/{name}')
