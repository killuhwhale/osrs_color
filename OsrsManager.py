from multiprocessing import Queue, Process
import pyautogui
import re
import signal
import sys
import threading
import time

from bot_loop import BotLoop
from OsrsClient import OsrsClient
from osrs_input import OsrsInput
from utils import run_cmd, run_script
from config import PLATFORM, SCREEN_TOP_MARGIN, WINDOW_TOP_MARGIN, OS_LINUX, OS_WIN, OS_MAC

DEBUG = True
SOCKS_HOST = ''
SOCKS_PORT = 1080


class OsrsManager:
    '''
        Creates 5 instances of Runelite and finds all pids.
        For each PID, create an instance of OSRS() 

    '''
    CLIENT_WIDTH = 765
    CLIENT_HEIGHT = 535

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080 - SCREEN_TOP_MARGIN

    # POS = [(0, 0 + SCREEN_TOP_MARGIN),
    #        (SCREEN_WIDTH//3, 0 + SCREEN_TOP_MARGIN),
    #        (2*(SCREEN_WIDTH//3), 0 + SCREEN_TOP_MARGIN),

    #        (0, (SCREEN_HEIGHT//2) + SCREEN_TOP_MARGIN),
    #        (SCREEN_WIDTH//3, (SCREEN_HEIGHT//2) + SCREEN_TOP_MARGIN)
    #        ]

    POS = [
        (0, 0 + SCREEN_TOP_MARGIN),
        (CLIENT_WIDTH, 0 + SCREEN_TOP_MARGIN),
        (2*CLIENT_WIDTH, 0 + SCREEN_TOP_MARGIN),

        (0, CLIENT_HEIGHT + SCREEN_TOP_MARGIN),
        (CLIENT_WIDTH, CLIENT_HEIGHT + SCREEN_TOP_MARGIN),
        (2*CLIENT_WIDTH, CLIENT_HEIGHT + SCREEN_TOP_MARGIN),
    ]

    def __init__(self, num_clients):
        self._num_clients = num_clients
        self._os_name = PLATFORM
        self.pids = []
        self.clients = []
        self._main_loop = None
        self._input_thread = None

        # Process queue
        self._q = Queue()

        self._botLoop = BotLoop(DEBUG)
        self._input = OsrsInput()

        self.create_clients()
        print(
            f'''Started {num_clients} on '{PLATFORM}' with pids: {self.pids}''')
        self._sigTerm()  # handling for terminating the process.

    def create_clients(self):
        # Launch Processes
        if not DEBUG:
            for i in range(self._num_clients):
                cmd = f'java -jar ./RuneLite.jar'
                ''' 
                cmd = f'java -DsocksProxyHost={SOCKS_HOST} -DsocksProxyPort={SOCKS_PORT} -jar runelite.jar'

                Plugin:
                    Search response in custom ammo plugin target=".your-ip"
                    /Users/chrisandaya/IdeaProjects/runelite/runelite-client/target/client-1.8.25-SNAPSHOT-shaded.jar
                    CMD to launch Runelite w/ plugin: /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/bin/java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=13377 -jar client-1.8.25-SNAPSHOT-shaded.jar
                
                Regular
                    java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=13377 -jar runelite.jar
                
                    Start Proxy server
                    ssh -D 13377  chrisandaya@34.121.188.5 -i ~/.ssh/google_compute_engine
                '''

                run_cmd(cmd)

        print("Waiting for clients to load")
        time.sleep(1)

        # Find Pids
        self.pids = self._find_pids()

        # Assign a PID and Dimensionss to each Client
        self._assign_pid_and_dims_to_client()

        # Pass clients to BotLoop
        self._botLoop.set_clients(self.clients)

    def _assign_pid_and_dims_to_client(self):
        for i in range(len(self.pids)):
            pid = self.pids[i]
            pos_x = self.POS[i % self._num_clients][0]
            pos_y = self.POS[i % self._num_clients][1]
            dims = [pos_x, pos_y, self.CLIENT_WIDTH,
                    self.CLIENT_HEIGHT]

            if self._os_name == OS_WIN:
                self._resize_window_win11()
            elif self._os_name == OS_MAC:
                self._resize_window_mac(
                    pid, dims[0], dims[1], dims[2], dims[3])
            else:
                win_ids = self._get_win_IDs(pid)
                print('IDS:', win_ids)
                for wid in win_ids:
                    if wid:
                        print("Window id: ", wid)
                        self._resize_window(
                            wid, self.CLIENT_WIDTH, self.CLIENT_HEIGHT)
                        self._move_window(wid, pos_x, pos_y)

            # If mac

            # If Linux

            # Create client
            self.clients.append(OsrsClient(pid, dims))

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
        pid_pattern = r"""^\s*(?P<pid>\d*)\s*.*RuneLite$"""
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

    def _resize_window_mac(self, pid, pos_x, pos_y, w, h):
        '''
            Issues command
        '''
        print("Inner command: ", pid)
        inner_cmd = f"""tell application "System Events"
            tell processes whose unix id is {pid}
                set size of front window to {{{w}, {h}}}
                set position of front window to {{{pos_x}, {pos_y}}}
            end tell
        end tell"""

        run_script('osascript', inner_cmd.encode('utf-8'))

    # Linux
    def _move_window(self, win_id, pos_x, pos_y):
        cmd = f'''xdotool windowmove -- {win_id} {pos_x} {pos_y}'''
        run_cmd(cmd)

    # Linux
    def _resize_window(self, win_id, w, h):
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

    def _get_win_IDs(self, pid):
        """ Gets window ID of Runelite.

        Returns:
            The window ID of Runelite based on the PID.

        """
        assert pid, f"Window ID invalid: {pid}"
        cmd = f"xdotool search --pid {pid}"
        return run_cmd(cmd).split("\n")

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
            (0+x_offset, 0),
            ((SCREEN_WIDTH//2)+x_offset, 0),
            (0+x_offset, SCREEN_HEIGHT//2),
            ((SCREEN_WIDTH//2)+x_offset, SCREEN_HEIGHT//2),
        ]
        for i in range(len(windows)):
            window = windows[i]
            window.resizeTo(self.CLIENT_WIDTH, self.CLIENT_HEIGHT)
            pos = screen_pos[i]
            window.moveTo(pos[0], pos[1])
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
        self._input_thread.daemon = True
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

    def _handle_exit(self, _signum, _frame):
        print(f"Ctl-C pressed! Closing... {_signum} - {_frame}")
        self._main_loop.terminate()

        sys.exit()


if __name__ == "__main__":
    manager = OsrsManager(1)
    manager.begin()
