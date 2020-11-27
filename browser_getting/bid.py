""" Module used for getting the interface with the browser. 
Interface made by entering `BID(path="/path/to/biddriver")`. 
Example:
```python
from BrowserIt.browser_getting.bid import *
from BrowserIt.browser_interaction.interact import *

bid = BID(path="/path/to/biddriver")
interact(bid, "action", ...=..., ...)
```
"""
import ctypes, sys

__all__ = ['BID']

class BID:
    """ Class that is an interface for interacting with the browser. """

    def __init__(self, **kwargs):
        self.path = kwargs['path']
        self._bid = ctypes.CDLL(self.path)
    
    def interaction(self, name="nop", *args, **kwargs):
        self._bid[name](*args, **kwargs)

