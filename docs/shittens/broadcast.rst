broadcast - type text in all shitty windows
==================================================

The ``broadcast`` shitten can be used to type text simultaneously in
all shitty windows (or a subset as desired).

To use it, simply create a mapping in :file:`shitty.conf` such as::

    map F1 launch --allow-remote-control shitty +shitten broadcast

Then press the :kbd:`F1` key and whatever you type in the newly created widow
will be sent to all shitty windows.

You can use the options described below to control which windows
are selected.

.. program:: shitty +shitten broadcast


Command Line Interface
--------------------------

.. include:: /generated/cli-shitten-broadcast.rst
