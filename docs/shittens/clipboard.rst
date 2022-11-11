clipboard - copy/paste to the system clipboard
==================================================

.. highlight:: sh


The ``clipboard`` shitten can be used to read or write to the system clipboard
from the shell. It even works over SSH. Using it is as simple as::

    echo hooray | shitty +shitten clipboard

All text received on :file:`stdin` is copied to the clipboard.

To get text from the clipboard you have to enable reading of the clipboard
in :opt:`clipboard_control` in :file:`shitty.conf`. Once you do that, you can
use::

    shitty +shitten clipboard --get-clipboard


.. program:: shitty +shitten clipboard


Command Line Interface
--------------------------

.. include:: /generated/cli-shitten-clipboard.rst
