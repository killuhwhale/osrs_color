# SET_WINDOW   java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=1080 -jar runelite.jar


'''

Launch Windows
    java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=1080 -jar runelite.jar

Collect PIDS of all windows.
    ps ax | grep RuneLite



For each window, postion it:
 
 osascript -e 'tell application "System Events"
    set proc to item 1 of (processes whose unix id is PIDHERE)
    tell proc
        set size of front window to {1920/2, 1080/2}
        set position of front window to {-234, -1080}, {726, -1080}, {-234, -540}, {726, -540}
    end tell
end tell'
'''


def client_launch_cmd(host, port):
    return f'java -DsocksProxyHost={host} -DsocksProxyPort={port} -jar runelite.jar'


def pos_windows():
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
    xoffset = -234
    POS = [(xoffset, -SCREEN_HEIGHT), ((SCREEN_WIDTH//2) + xoffset, -SCREEN_HEIGHT),
           (xoffset, -SCREEN_HEIGHT//2), ((SCREEN_WIDTH//2) + xoffset, -SCREEN_HEIGHT//2)]
    PIDS = [1, 2, 3, 4]
    for i in range(len(PIDS)):
        cmd = f"""osascript -e 'tell application "System Events"
    set proc to item 1 of (processes whose unix id is {PIDS[i]})
    tell proc
        set size of front window to {{{SCREEN_WIDTH//2}, {SCREEN_HEIGHT//2}}}
        set position of front window to {{{POS[i][0]} , {POS[i][1]}}}
    end tell
end tell'"""
        print(cmd)


pos_windows()
