from enum import Enum

import spaces


class VerifySpace(Enum):
    '''
        Map to Screenshot which are used as needle images to search in a space to verify things on screen.

        Used when needed to verify an icon is on screen.
         For example, checking when a bank or the GE is open.

    '''
    PATH_TO_SPACE_IMGS = "needles/spaces"
    BANK_DEPOSIT_WORN_ITEMS = {
        "n": "BANK_DEPOSIT_WORN_ITEMS", "pos": spaces.Spaces.BANK_DEPOSIT_WORN_ITEMS, "grayscale": False, "conf": 0.92}

    GE_HISTORY = {
        "n": "GE_HISTORY", "pos": spaces.Spaces.GE_HISTORY, "grayscale": False, "conf": 0.92}

    CONTINUE = {
        "n": "CONTINUE", "pos": spaces.Spaces.CONTINUE, "grayscale": False, "conf": 0.92}

    @classmethod
    def get_image_path(cls, v_space,):
        return f"{cls.PATH_TO_SPACE_IMGS}/{str(v_space)}"

    def __str__(self):
        return self.name
