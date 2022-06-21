from random import gauss, randrange
from subprocess import Popen, PIPE, run
from enum import Enum


class Durations(Enum):
    EX_SHORT = 1
    V_SHORT = 2
    SHORT = 3
    MED = 4
    LONG = 5


def run_script(proc, script):
    p = Popen([proc, '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(script)
    return stdout, stderr


def run_cmd(cmd, as_list=False):
    """ Runs a bash command.

    Args:
        cmd: A string that represents the command.
    Returns:
        stdout from bash command
    """

    return run(cmd.split()if not as_list else cmd, check=True, encoding='utf-8', capture_output=True).stdout


def rr(a, b):
    return randrange(min(a, b), max(a, b))


def r_mouse_duration(dur=None):
    # If duration not given choose randomly
    if dur is None:
        dur = max(0.175, gauss(0.1, 0.6))
        print(f"Duration is {dur}")
        return dur

    if dur == Durations.EX_SHORT:
        return gauss(0.2, 0.6)
    if dur == Durations.V_SHORT:
        return gauss(0.3, 0.1)
    if dur == Durations.SHORT:
        return gauss(0.4, 0.133)
    if dur == Durations.MED:
        return gauss(0.5, 0.15)
    if dur == Durations.LONG:
        return gauss(0.6, 0.175)


class Constant:
    def __init__(self, value):
        self.value = value

    def __get__(self, *args):
        return self.value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __add__(self, other):
        return int(self.value) + other

    def __radd__(self, other):
        return int(self.value) + other

    def __sub__(self, other):
        return int(self.value) - other

    def __rsub__(self, other):
        return other - int(self.value)

    def __mul__(self, other):
        return int(self.value) * other

    def __rmul__(self, other):
        return int(self.value) * other
