import collections
import cv2
from cv2 import cvtColor
from Search import Items
from Spaces import Spaces
from VerifySpace import VerifySpace
import pytesseract
import numpy as np
import pyautogui
from PIL import Image

from utils import run_cmd

'''
Parameter optimization

scale_up=
scale_down=
kernal_a=
kernal_b=
iterations=
tesseract_oem=
tesseract_=?


'''


class CLIENT:
    dims = [0, 25, 765, 535]


CLIENT_DIMS = [0, 25, 765, 535]


def ocr(img: np.mat, scale_up, scale_down, kernal_a, kernal_b, iters, image=False):
    # img = cv2.imread(filepath) if not image else cv2.cvtColor(
    #     np.array(filepath.convert("RGB")), cv2.COLOR_RGB2BGR)

    scale_percent = scale_up
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)
    # resize image
    # img = cv2.resize(img, dsize)

    # cv2.imshow("Res", img)
    # cv2.moveWindow("Res", 1000, 30)
    # cv2.waitKey(0)

    # Alternatively: can be skipped if you have a Blackwhite image
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    lo = [13, 162, 190]
    # lo = lows[i]
    hi = [180, 255, 255]
    color_range_low = np.array(lo)
    color_range_high = np.array(hi)
    mask = cv2.inRange(hsv, color_range_low, color_range_high)
    img = mask
    # cv2.imshow("Res2", mask)
    # cv2.waitKey(0)

    kernel = np.ones((kernal_a, kernal_b), np.uint8)

    # Try
    # img = cv2.dilate(mask, kernel, iterations=iters)

    # if scale up and down are equal, it goes back to original size

    width = int(img.shape[1] * (scale_down/100))
    height = int(img.shape[0] * (scale_down/100))
    dsize = (width, height)
    # img = cv2.resize(img, dsize)
    img = cv2.bitwise_not(img)
    out_below = pytesseract.image_to_string(
        img, config="--psm 6  -c tessedit_char_whitelist=0123456789")

    print(f"OUTPUT: {out_below}")

    cv2.imshow("Res", img)
    cv2.moveWindow("Res", 1000, 30)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return int(out_below) if out_below else -1


def test_live_screenshots():
    '''
        Run area
        1 = 530, 125 
        2 = 552, 140 
    '''
    c = 0
    search = Search()
    while True:
        img = search._crop_screen_pos([0, 25, 765, 535], 530, 115,
                                      555, 135, f"runImgs/run_{c}.png")
        c += 1

        np_img = np.array(img[0])
        bgr_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
        cv2.imshow("Res", bgr_img)
        cv2.moveWindow("Res", 1000, 30)
        cv2.waitKey(0)


def test_run_images():

    images = [cv2.imread(f"runImgs/run_{i}.png") for i in range(101)]
    single_run = True

    if single_run:
        # 0.66: [(300, 75, 4, 3, 1)]
        for i in range(101):
            ocr(images[i], 100, 100, 6, 2, 4)
    else:
        # Parameters
        scale_ups = [x for x in range(350, 376)]
        scale_downs = [x for x in range(65, 101)]
        kernal_as = [4]
        kernal_bs = [3]
        iterations = [1]

        # Accuracy: 0.57 w/ (275, 50, 3, 3, 1)
        # Accuracy: 0.62 w/ (300, 75, 4, 3, 1)
        # Accuracy: 0.72 w/ (300, 75, 3, 3, 1)
        # Accuracy: 0.78 w/ (300, 75, 4, 3, 1)
        # 0.82: [(350, 74, 4, 3, 1)]
        answers = collections.defaultdict(list)

        for scale_up in scale_ups:
            for scale_down in scale_downs:
                for kernal_a in kernal_as:
                    for kernal_b in kernal_bs:
                        for iteration in iterations:
                            s = 0
                            for i in range(100):
                                res = ocr(images[i], scale_up, scale_down,
                                          kernal_a, kernal_b, iteration)
                                s += 1 if i == res else 0
                            a = s/100
                            answers[a].append(
                                (scale_up, scale_down, kernal_a, kernal_b, iteration))
                            print(
                                f"Accuracy: {a} w/ {(scale_up, scale_down, kernal_a, kernal_b, iteration)}")

        for k in sorted(answers.keys()):
            print(f"{k}: {answers[k]}")

        # for k in sorted(results.keys()):
        #     print(k, results[k])
        #     s += 1 if results[k][0] else 0

        run_cmd(cmd)


def transform_hori(img: Image):

    np_img = np.array(img.convert("RGB"))

    hsv = cv2.cvtColor(np_img, cv2.COLOR_RGB2HSV)
    # (0, 155, 0)  -   (180, 255, 255)
    lo = [0, 155, 0]
    hi = [180, 255, 255]
    color_range_low = np.array(lo)
    color_range_high = np.array(hi)
    mask = cv2.inRange(hsv, color_range_low, color_range_high)

    cv2.imshow("Res", mask)
    cv2.moveWindow("Res", 1000, 30)
    cv2.waitKey(0)
    # cv2.imwrite("runImgs/hori_mask.png", mask)
    return mask


def test_pyauto_search():
    hori_img = Image.open("runImgs/hori_mask.png")
    images = [Image.open(f"runImgs/run_{i}.png") for i in range(101)]

    client_dims = [0, 25, 765, 535]

    for i in range(101):
        img = images[i]
        img = transform_hori(img)
        res = pyautogui.locate(
            img, hori_img, grayscale=True,  confidence=.95)
        print(res[0]//20)


def test_multicolor():
    multi = Image.open("multicolor.png")
    multi = np.array(multi.convert('RGB'))

    multi = cv2.cvtColor(multi, cv2.COLOR_RGB2HSV)

    color = [
        [[8, 231, 242], [31, 255, 255]],
        [[115, 240, 191], [121, 255, 255]],
        [[0, 0, 192], [1, 7, 255]],
        [[61, 254, 0], [69, 255, 255]],
        [[145, 254, 0], [150, 255, 255]],
        [[0, 254, 0], [1, 255, 255]],
        [[88, 254, 0],	[92, 255, 255]]

    ]
    for i in range(len(color)):
        res = cv2.inRange(
            multi, np.array(color[i][0]), np.array(color[i][1]))

        cv2.imshow("Res", res)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


def imshow(img: Image):
    cv2.imshow("imshow", np.array(img.convert('RGB')))
    cv2.moveWindow("imshow", 1000, 30)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def take_ss_of_item():
    RUNE_SHOT = False
    # CITEM = Items.SILVER_ORE
    CITEM = VerifySpace.CONTINUE
    img_type = "spaces"
    FIXED_INV_SLOT = False
    while True:
        img = None
        if FIXED_INV_SLOT:
            if RUNE_SHOT:
                img, x, y = Spaces._crop_screen_pos(
                    CLIENT(), [565, 220, 590, 237], f"needles/{img_type}/{CITEM}.png")
            else:
                img, x, y = Spaces._crop_screen_pos(
                    CLIENT(), [560, 210, 595, 245], f"needles/{img_type}/{CITEM}.png")
        else:
            img, x, y = Spaces._crop_screen_pos(
                CLIENT(), Spaces.SPACES[CITEM.value["pos"]], f"needles/{img_type}/{CITEM}.png")

        if img:
            imshow(img)


def avg_color():
    img = cv2.imread('chat_head.png')
    img_empty = cv2.imread('chat_head_empty.png')

    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    avg_color_per_row_empty = np.average(img_empty, axis=0)
    avg_color_empty = np.average(avg_color_per_row_empty, axis=0)
    print(avg_color, avg_color_empty)
    print(np.average(avg_color), np.average(avg_color_empty))


if __name__ == "__main__":
    take_ss_of_item()
