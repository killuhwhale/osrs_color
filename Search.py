

from math import sqrt
from random import gauss
import cv2
from cv2 import sort
import numpy as np
from PIL import Image
import pyautogui
from time import sleep
from Colors import Colors
from Items import Items
from typing import Tuple, List

from OsrsClient import OsrsClient
from Spaces import Spaces
from VerifySpace import VerifySpace
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
    EMPTY_CHAT_HEAD = None

    HORIZONTAL_RUN_IMG_PATH = "assets/horiImgs/hori_run_mask.png"
    EMPTY_CHAT_HEAD_PATH = "assets/chat_heads/chat_head_empty.png"

    ''' I want to search for things.
        Search means we are looking at an area and searching within it.
        I can search by item.png, color

        I want to check Certain Lvls w/ OCR


        I want to click on predefined Interfaces.

    '''

    @classmethod
    def search_intf_image_to_num(cls, client, space) -> int:
        ''' 
            Takes a screen shot and returns the value as an int
            HP, PRAYER, RUN, SPECIAL Image to Int
        '''
        # Check for right space? Not sure
        cls.HORIZONTAL_RUN_IMG = Image.open(
            cls.HORIZONTAL_RUN_IMG_PATH) if cls.HORIZONTAL_RUN_IMG is None else cls.HORIZONTAL_RUN_IMG
        img, offset_x, offset_y = Spaces.get_space(client, space)
        img = cls._transform_img_blk_white_skill(img)
        # imshow(img)
        bounds = pyautogui.locate(img, cls.HORIZONTAL_RUN_IMG,
                                  grayscale=False,  confidence=.92)  # 98 - 90,    63 -> 71 - None
        if bounds is None:
            bounds = [-1]
        return bounds[0] // 20

    @classmethod
    def click_interface(cls, client: OsrsClient, space: Spaces) -> int:
        '''
            Given a Space, return a random coordinate within its bounds.
        '''
        bounds = Spaces.get_bounds(
            client, space)  # Bounds are already adjusted

        # increase bounds on magic spells
        # 93 - 162
        print(space > 0)
        if 93 <= space <= 162:
            bounds = cls._pad_bounds(bounds, padding=6)
        else:
            bounds = cls._pad_bounds(bounds)

        return cls._random_bound(bounds)

    @classmethod
    def click_interface_from_raw_coords(cls, client: OsrsClient, raw_space: List) -> int:
        '''
            Given a a list of coords
            Probably not very useful honestly, just need to know where to click on skill....
            If we want to know the lvls we can probabably do an http request.
        '''
        print(f"client/raw_space: {client}/{raw_space}")
        bounds = Spaces.get_bounds_from_raw_coords(
            client, raw_space)  # Bounds are already adjusted

        bounds = cls._pad_bounds(bounds)
        return cls._random_bound(bounds)

    @classmethod
    def search_space_multi_item(cls, client: OsrsClient, space: Spaces, items: List[Items], grayscale=False, confidence=0.69) -> (List):
        '''
            Search a space for an multiple items, returns a list of their click points or None if the item is not found.
            e.g. [(x,y), None, (x1,y1)]
        '''
        search_space, x_offset, y_offset = Spaces.get_space(client, space)
        image_data = (search_space, x_offset, y_offset,)
        ans = []
        for item in items:
            ans.append(cls._search_space_item(client, space,
                       item, grayscale, confidence, image_data))

        return ans

    @classmethod
    def search_space_item(cls, client: OsrsClient, space: Spaces, item: Items, grayscale=False, confidence=0.69) -> (Tuple[int, int] or None):
        '''
            Search a space for an item
        '''
        return cls._search_space_item(client, space, item, grayscale, confidence)

    @classmethod
    def _search_space_item(cls, client: OsrsClient, space: Spaces, item: Items, grayscale=False, confidence=0.69, image_data: Tuple[Image.Image, int, int] = None) -> (Tuple[int, int] or None):
        '''
            Search a space for an item
        '''
        search_space, x_offset, y_offset = None, 0, 0

        if image_data is None:
            search_space, x_offset, y_offset = Spaces.get_space(client, space)
        else:
            search_space, x_offset, y_offset = image_data

        needle = cls._load_img(f"items/{str(item)}.png")
        # imshow(needle)

        if needle is None:
            return None

        # 4-integer tuple: (left, top, width, height)
        bounds = pyautogui.locate(
            needle, search_space, grayscale=item.value['grayscale'], confidence=item.value['conf'])
        if bounds is None:
            # retries = 5  TODO() Change back
            retries = 0
            while bounds is None and retries > 0:
                print(
                    f"Image not found, retrying: {retries} more times")
                bounds = pyautogui.locate(
                    needle, search_space, grayscale, confidence)
                retries -= 1
                sleep(.5)

            if bounds is None:
                return None, None

        bounds = cls._adjust_locate_bounds(bounds, x_offset, y_offset)  #
        bounds = cls._pad_bounds(bounds)
        return cls._random_bound(bounds)

    @classmethod
    def search_space_color(cls, client: OsrsClient, space: Spaces, color: Colors, grayscale=True, confidence=0.69, padding=2) -> (Tuple[int, int] or None):
        '''
            Search a space for an item
        '''
        # Offset from space
        search_space, x_offset, y_offset = Spaces.get_space(client, space)

        # 4-integer tuple: (left, top, width, height)
        # Offset from image
        pt = cls._locate_color(
            np.array(color.value['low']), np.array(color.value['hi']), search_space, grayscale, confidence, padding)

        if pt is None:
            return None

        x, y = pt[0] + x_offset, pt[1] + y_offset
        return (x, y)

    @classmethod
    def verify_space(cls, client: OsrsClient, v_space: VerifySpace) -> bool:
        needle = cls._load_img(f"spaces/{str(v_space)}.png")

        # VerifySpace references Spaces Object for its position.
        search_space, x_offset, y_offset = Spaces._crop_screen_pos(
            client, Spaces.SPACES[v_space.value["pos"]])
        # imshow(search_space)
        bounds = pyautogui.locate(
            needle, search_space, grayscale=v_space.value['grayscale'], confidence=v_space.value['conf'])
        return bounds is not None

    @classmethod
    def click(cls, pt=None):
        if pt is None:
            return
        x, y = pt
        print(f"Clicking: {x} {y} ")
        # TODO Randomize move tos
        pyautogui.moveTo(x, y, duration=gauss(0.4, .1))
        pyautogui.click()

    @classmethod
    def _adjust_locate_bounds(cls, bounds: tuple, x_offset: int, y_offset: int) -> Tuple[int, int, int, int]:
        ''' Adjusts the bounds of the item found in image to where it is on screen.
            Bounds of the item in the image or relative to the image's top left corner @ x = 0, y = 0
            The image is taken as a screenshot at a specific x y offset.

            This method returns the items bounds relative to the screen.
        '''

        left = bounds[0]
        top = bounds[1]
        width = bounds[2]
        height = bounds[3]
        x_left = x_offset + left
        y_top = y_offset + top

        return (x_left, y_top, width, height)

    @classmethod
    def _random_bound(cls, bounds: tuple) -> Tuple[int, int]:
        '''
            Given adjust bounds for a client, pick a random point.
        '''
        left = bounds[0]
        top = bounds[1]
        width = bounds[2]
        height = bounds[3]

        right = left + width
        bottom = top + height

        click_x = rr(left, right)
        click_y = rr(bottom, top)

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
        # cv2.imshow("Org", np_img)
        # # cv2.imshow("HSV", hsv)
        # cv2.imshow("blkwhite mask", mask)
        # cv2.moveWindow("blkwhite mask", 1000, 30)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return Image.fromarray(mask)

    @classmethod
    def _locate_color(cls, color_low: list, color_high: list, search_space: Image, grayscale: bool, confidence: float, padding: int) -> Tuple[int, int]:

        # Convert Space to HSV color space
        img = np.asarray(search_space)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        # print("Low/ high")
        # print(color_low, color_high)
        # cv2.imshow('img', img)
        # cv2.moveWindow('img', 1000, 0)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Threshold the HSV image to get only red colors
        mask = cv2.inRange(hsv, color_low, color_high)

        # cv2.imshow('mask', mask)
        # cv2.waitKey(0)
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print("No contours found")
            return None

        contours = sorted(contours, key=lambda c: cv2.contourArea(c))
        largest_contour = contours[-1]
        largest_contour_area = cv2.contourArea(largest_contour)
        # print(f"Coutour size: {largest_contour_area}")

        if largest_contour_area <= 19.0:
            print(f"Contour too small {largest_contour_area}")
            return None

        bounds = cv2.boundingRect(largest_contour)

        # Bounds includes more points than we want.
        # Lets pick a point in bounds
        bounds = cls._pad_bounds(bounds, padding=padding)

        pt = cls._random_bound(bounds)
        # Lets check if its in the contour still
        test_res = cv2.pointPolygonTest(largest_contour, pt, False)
        retries = 5
        while test_res < 3.0 and retries > 0:
            pt = cls._random_bound(bounds)
            test_res = cv2.pointPolygonTest(largest_contour, pt, True)
            retries -= 1

        ''' DEBUG
        '''
        # print(f"Picked pt: {pt} and the test result is: {test_res}")
        # Draw and show contours
        # boximg = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
        # x, y, w, h = bounds
        # cv2.rectangle(boximg, (x, y), (x+w, y+h), (2550, 0, 0))
        # cv2.circle(boximg, pt, 3, (0, 0, 255), thickness=-1)

        # cv2.imshow('img', img)
        # cv2.imshow('mask', mask)
        # cv2.imshow('res', boximg)
        # cv2.moveWindow('res', 1000, 0)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Instead of return raw bounds, which may be inaacruate
        # Lets return a point known to be in the bounds AND contour.
        return pt

    @classmethod
    def _load_img(cls, name) -> Image:
        ''' Lods image from disk '''
        img = None
        try:
            return Image.open(f'needles/{name}')
        except FileNotFoundError:
            print("Image not found")
        return img

    @classmethod
    def _pad_bounds(cls, bounds, padding=3) -> Tuple[int, int, int, int]:
        '''
            Adds padding to the bound so no clicks will happen on the border which may cause a misclick.
        '''
        x, y, w, h = bounds

        return (x + padding, y + padding, w - (2 * padding), h - (2 * padding))

    @classmethod
    def chat_head_showing(cls, client, left=True, both=False) -> bool:
        space = Spaces.CHAT_HEAD if left else Spaces.CHAT_HEAD_RIGHT
        img, x, y = Spaces.get_space(client, space)
        img = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)

        # cls.EMPTY_CHAT_HEAD = cls.EMPTY_CHAT_HEAD if cls.EMPTY_CHAT_HEAD is not None else cv2.imread(
        #     cls.EMPTY_CHAT_HEAD_PATH)

        def dist(p1, p2): return sqrt(
            (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[1])**2)
        pixels = np.float32(img.reshape(-1, 3))

        n_colors = 5
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv2.kmeans(
            pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        dominant = palette[np.argmax(counts)]
        distance = dist([132.03435, 162.98283, 177.95706], dominant)

        print(
            f"dominant color background: { [132.03435, 162.98283, 177.95706]}")
        print(f"dominant color: {dominant}")
        print(f"Dist: {distance}")

        '''
            cur_avg = np.average(np.average(np.average(img, axis=0), axis=0))
            # empty_avg = np.average(np.average(
            #     np.average(cls.EMPTY_CHAT_HEAD, axis=0), axis=0))
            empty_avg_left = 158.324889520202  # left
            empty_avg_right = 165.99164054336464  # right

            empty_avg = empty_avg_left if left else empty_avg_right
            delta = abs(empty_avg - cur_avg)

            print(
                f"No chat head val: {np.average(empty_avg)},  Current val: {np.average(cur_avg)}, Delta: {delta}")
        
        '''

        return distance > 17.0
