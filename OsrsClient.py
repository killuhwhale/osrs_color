""" A prepresentation of a client. An instanace of this class will contain a clients dimensions and the PID.

    Used to determine which client to perform actions on.
"""


class OsrsClient:
    def __init__(self, pid=None, dims=None):
        # A list to store dimensions: x, y postition, height and width of window.
        self.dims = dims
        self._pid = pid

    def get_pid(self):
        return self._pid


if __name__ == "__main__":
    print("No intended to be ran.")
