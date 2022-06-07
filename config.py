import sys


'''
Each platform has a different margin at the top of the screen
Also, each have a different App window title bar margin.
So we should assign a value to each SCREEN_TOP_MARGIN, WINDOW_TOP_MARGIN


TODO() find each WINDOW margin and figure out where to use the window one.... THe problem is the difference between the develpopment machine which is mac.... 


Screen                           _____________
    SCREEN_TOP_MARGIN           |             |   Mac=25 , Win, Linux = 30
Screen                          +-------------+
App                             +-------------+
    WINDOW_TOP_MARGIN           |             |   Mac=30 , Win, Linux = 35
App                             +-------------+


MAC
'''

OS_MAC = 'darwin'
OS_LINUX = "linux"
OS_WIN = 'windows'

# Dev Machine
DEV_TARGET = 'darwin'

PLATFORM = sys.platform

SCREEN_TOP_MARGIN_MAC = 25
WINDOW_TOP_MARGIN_MAC = 30

SCREEN_TOP_MARGIN_LINUX = 30
WINDOW_TOP_MARGIN_LINUX = 35

SCREEN_TOP_MARGIN_WINDOWS = 30
WINDOW_TOP_MARGIN_WINDOWS = 30

# Target
SCREEN_TOP_MARGIN = SCREEN_TOP_MARGIN_MAC if PLATFORM == OS_MAC else SCREEN_TOP_MARGIN_WINDOWS if PLATFORM == OS_WIN else SCREEN_TOP_MARGIN_LINUX
WINDOW_TOP_MARGIN = WINDOW_TOP_MARGIN_MAC if PLATFORM == OS_MAC else WINDOW_TOP_MARGIN_WINDOWS if PLATFORM == OS_WIN else WINDOW_TOP_MARGIN_LINUX

# Platform Adjustment
'''
    On Development machine, there is specific margin SCREEN + WINDOW margins.
    Then we plot the points FROM the top left corner, but there is this MARGIN that is contained within the point we are clicking.
    So, the MARIGN only affects the Y Coordinate
    Therefore, we can adjust all of the Y positions by the difference of:
        - the development machine(mac) margins and the machine currently running the program.
'''

PA = (SCREEN_TOP_MARGIN_MAC + WINDOW_TOP_MARGIN_MAC) - \
    (SCREEN_TOP_MARGIN + WINDOW_TOP_MARGIN)
