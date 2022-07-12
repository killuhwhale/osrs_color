from typing import List
import search
import spaces
import py_key
""" A prepresentation of a client. An instanace of this class will contain a clients dimensions and the PID.

    Used to determine which client to perform actions on.
"""


class OsrsClient:
    def __init__(self, pid: str, dims: List[int, int, int, int], creds: List[str, str]):
        # A list to store dimensions: x, y postition, height and width of window.
        self.dims = dims
        self._pid = pid
        self._creds = creds

    def get_pid(self):
        return self._pid

    def login(self):
        print(f"Logging in w: {self._creds[0]}/{self._creds[1]}")
        # Click Existing User
        search.Search.click(search.Search.click_interface(
            self, spaces.Spaces.LOGIN_EXISTING_USER))
        [py_key.PyKey.press(k) for k in self._creds[0]]
        py_key.PyKey.press(py_key.PyKey.ENTER)  # Go to password
        [py_key.PyKey.press(k) for k in self._creds[1]]
        py_key.PyKey.press(py_key.PyKey.ENTER)  # Login


if __name__ == "__main__":
    print("Not intended to be ran.")
