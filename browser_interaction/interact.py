""" Module to interact with the browser. 
Use `interact(bid, actionname, params)` to interact.
Example:
```python
from BrowserIt.browser_getting.bid import *
from BrowserIt.browser_interaction.interact import *

bid = BID(path="/path/to/biddriver")
interact(bid, "action", ...=..., ...)
```
"""

__all__ = ['interact']

def interact(bid, action, **params):
    bid.interact(action)(*params)

