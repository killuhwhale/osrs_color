from enum import Enum
import numpy as np


class Colors(Enum):
    '''
        Tile/ Object/ NPC Color indicators
    '''

    # Color = HSV Range  Low       High          Hex Color

    NPC_PURPLE = {
        'low': list([129, 187, 218]),
        'hi': list([141, 208, 241]),
        'hex_target': 'FFA434EE'
    }
    Yellow = {
        'low': list([8, 231, 242]),
        'hi': list([31, 255, 255]),
        'hex_target': 'FFFFFF00'
    }
    Blue = {
        'low': list([115, 240, 191]),
        'hi': list([121, 255, 255]),
        'hex_target': 'FF0000FF'
    }
    White = {
        'low': list([0, 0, 192]),
        'hi': list([1, 7, 255]),
        'hex_target': 'FFFFFFFF'
    }
    Green = {
        'low': list([61, 254, 0]),
        'hi': list([69, 255, 255]),
        'hex_target': 'FF00FF13'
    }
    Purple = {
        'low': list([145, 254, 0]),
        'hi': list([150, 255, 255]),
        'hex_target': 'FFFF00FF'
    }
    Red = {
        'low': list([0, 254, 0]),
        'hi': list([1, 255, 255]),
        'hex_target': 'FFFF0000'
    }
    Cyan = {
        'low': list([71, 240, 85]),
        'hi': list([94, 255, 255]),
        'hex_target': 'FF00FFFF'
    }
    LOGS_ON_FIRE = {
        'low': list([21, 242, 59]),
        'hi': list([25, 255, 97]),
        'hex_target': '???'
    }
