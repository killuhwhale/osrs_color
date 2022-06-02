from multiprocessing import Queue, Process
import pyautogui
import re
import signal
import sys
import threading
import time

from bot_loop import BotLoop
from osrs import OsrsClient
from osrs_input import OsrsInput
from utils import run_cmd, run_script



class OsrsManager:
    '''
        Creates 5 instances of Runelite and finds all pids.
        For each PID, create an instance of OSRS() 

    '''
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
    xoffset = -234
    POS = [(xoffset, -SCREEN_HEIGHT), ((SCREEN_WIDTH//2) + xoffset, -SCREEN_HEIGHT),
           (xoffset, -SCREEN_HEIGHT//2), ((SCREEN_WIDTH//2) + xoffset, -SCREEN_HEIGHT//2)]
    OS_WIN = 'win'
    OS_MAC = 'mac'


    def __init__(self, num_clients, os_name):
        self._num_clients = num_clients
        self._os_name = os_name
        self.pids = []
        self.clients = []
        self._main_loop = None
        self._input_thread = None
        # Process queue
        self._q = Queue()

        self._botLoop = BotLoop()
        self._input = OsrsInput()

        self.create_clients()
        print(f'Started {num_clients} with pids: {self.pids}')

    def create_clients(self):
        # Launch Processes
        for i in range(self._num_clients):
            cmd = f'java -jar ./RuneLite.jar'
            run_cmd(cmd)

        print("Waiting for clients to load")
        time.sleep(3)

        # Assign a PID and Dimensionss to each Client
        self.pids = self._find_pids()
        for i in range(len(self.pids)):
            pid = self.pids[i]
            pos_x = self.POS[i % 4][0]
            pos_y = self.POS[i % 4][1]
            dims = [pos_x, pos_y, self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2]



            if self._os_name == self.OS_WIN:
                self._resize_window_win11()
            elif self._os_name == self.OS_MAC:
                self._resize_window_mac(pid, pos_x, pos_y, f'name{i}test')
            else:
                win_id = self._get_win_ID(pid)
                self._resize_window(win_id, self.SCREEN_HEIGHT//2, self.SCREEN_WIDTH//2)
                self._move_window(win_id, pos_x, pos_y)



            # If mac

            # If Linux

            # Create client
            self.clients.append(OsrsClient(pid, dims))

        self._botLoop.set_clients(self.clients)

    def _find_pids(self):
        """ Finds PID of runelite.
        #   Runelite 
        #   10521 pts/0    Sl+   35:25 ./RuneLite.AppImage
        """
        top = run_cmd("ps ax")
        # pid_pattern = r"""^\s*(?P<pid>\d*)\s*
        # \w*\s*
        # \w*\+*\s*
        # \d*\:\d*\.\d*\s*
        # \/opt\/homebrew\/Cellar\/openjdk.*$"""
        pid_pattern = r"""^\s*(?P<pid>\d*)\s*\w*\s*\w*\+*\s*\d*\:\d*\.\d*\s*\/opt\/homebrew\/Cellar\/openjdk.*$"""
        pattern = re.compile(pid_pattern, re.MULTILINE | re.VERBOSE)
        # match = re.search(pattern, top)
        matches = re.finditer(pattern, top)
        pids = []
        for match in matches:
            pid = match.group('pid')
            print(f'Pid found: {pid}')
            pids.append(pid)

        assert len(
            pids) >= self._num_clients, f"Did not find pid: \n{top}"

        return pids

    def _resize_window_mac(self, pid, pos_x, pos_y, name):
        '''
            Issues command
        '''
        print("Inner command: ", pid)
        inner_cmd = f"""tell application "System Events"
            tell processes whose unix id is {pid}
                set size of front window to {{{self.SCREEN_WIDTH//2}, {self.SCREEN_HEIGHT//2}}}
                set position of front window to {{{pos_x}, {pos_y}}}
            end tell
        end tell"""

        run_script('osascript', inner_cmd.encode('utf-8'))

    # Linux

    def _move_window(self, win_id, pos_x, pos_y):
        pass
    # Linux

    def _resize_window(self, win_id, h, w):
        assert win_id, f"Window ID invalid: {win_id}"
        cmd = f"xdotool windowsize {win_id} {w} {h}"
        run_cmd(cmd)
    # Linux

    def _get_win_dimensions(self, win_id):
        """ Returns the postition of the top left corner of the window.
        Returns the top left corner and the width and height of the window.

        Returns:
            values: A list of screen coordinates indicating window position and size.
            [position x, position y, width, height]
        """
        _pos_pattern = r"""
        Position:\s*(?P<p_x>\d*),(?P<p_y>\d*)\s*\(\w*:\s*\d*\)
        """
        _geo_pattern = r"""
        Geometry:\s*(?P<g_x>\d*)x(?P<g_y>\d*)\s*
        """
        assert win_id, f"Window ID invalid: {win_id}"
        pos_pattern = re.compile(_pos_pattern, re.MULTILINE | re.VERBOSE)
        geo_pattern = re.compile(_geo_pattern, re.MULTILINE | re.VERBOSE)
        cmd = f"xdotool getwindowgeometry {win_id}"
        res = run_cmd(cmd)
        pos_match = re.search(pos_pattern, res)
        geo_match = re.search(geo_pattern, res)
        px = pos_match.group('p_x')
        py = pos_match.group('p_y')
        gx = geo_match.group('g_x')
        gy = geo_match.group('g_y')

        # Position(top left corner x, y coord) and Geometry(widthxheight)
        values = [px, py, gx, gy]
        values = [int(val) for val in values]
        assert all(
            values), f"Unable to find pos or geo of window: {win_id}"
        return values
    # Linux

    def _get_win_ID(self, pid):
        """ Gets window ID of Runelite.

        Returns:
            The window ID of Runelite based on the PID.

        """
        assert pid, f"Window ID invalid: {pid}"
        cmd = f"xdotool search --pid {pid}"
        return run_cmd(cmd).split("\n")[-2]


    def _resize_window_win11(self):
        windows = pyautogui.getWindowsWithTitle("RuneLite")
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080

        '''
        -1920,0            -1,0                





        -1920,1079         -1,1079
        '''
        x_offset = -1920
        screen_pos = [
            (0+x_offset,0),
            ((SCREEN_WIDTH//2)+x_offset,0),
            (0+x_offset,SCREEN_HEIGHT//2),
            ((SCREEN_WIDTH//2)+x_offset,SCREEN_HEIGHT//2), 
            ]
        for i in range(len(windows)):
            window = windows[i]
            window.resizeTo(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
            pos = screen_pos[i]
            window.moveTo(pos[0],pos[1])    
            print(f'giving window {i} pos:{pos}')




    def start_it(self):
        # main_loop = threading.Thread(target=self.run, args=(99,))
        self._main_loop = Process(target=self._run, args=(self._q,))
        self._main_loop.start()
        while(True):
            user_input = input("Enter a command: ")
            self._q.put(user_input)

    def stop_it(self):
        self._main_loop.terminate()

    def begin(self):
        # Start process
        self._main_loop = Process(
            target=self._botLoop.start_bot, args=(self._q,))
        self._main_loop.start()

        self._input_thread = threading.Thread(
            target=self._input.start_input, args=(self._q, ))
        self._input_thread.start()
        # Start thread
        while True:
            pass

    def _sigTerm(self):
        """Sets up the handling for terminating the process.
        The signal.SIGTERM signal is used for terminating a process.
        The signal.SIGINT is an tnterrupt from keyboard (CTRL + C).
        When the script terminates or interrupted by the user,
        the handle_exit method will be invoked.
        """
        signal.signal(signal.SIGTERM, self._handle_exit)
        signal.signal(signal.SIGINT, self._handle_exit)

    def _handle_exit(self):
        print("Ctl-C pressed! Closing...")
        self._main_loop.terminate()
        self._input_thread.join()
        sys.exit()


if __name__ == "__main__":
    os_name = OsrsManager.OS_WIN
    manager = OsrsManager(2, os_name)
    manager.begin()

