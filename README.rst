BrowserIt
=========

BrowserIt is a tiny (but powerful? and useful) library for interacting
with browsers.

BIDs
----

BIDs are basically the thing that respond to the browsers, and you
download them for usage and you provide the path to them when creating a
``BID`` instance.

Installation
------------

Installing is easy:

::

   $ pip install browserit

OR

::

   $ python -m pip install browserit

Examples
--------

Example 1:

.. code:: python

   from BrowserIt.browser_getting.bid import *
   from BrowserIt.browser_interaction.interact import *

   bid = BID(path="/path/to/biddriver")
   interact(bid, "enter_text", id="text_input", text="hello")

Example 2:

.. code:: python

   from BrowserIt.browser_getting.bid import *
   from BrowserIt.browser_interaction.interact import *

   bid = BID(path="/path/to/biddriver")
   interact(bid, "change_url", url="google.com")
