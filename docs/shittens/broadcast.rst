broadcast
==================================================

*Type text in all shitty windows simultaneously*

The ``broadcast`` shitten can be used to type text simultaneously in all
:term:`shitty windows <window>` (or a subset as desired).

To use it, simply create a mapping in :file:`shitty.conf` such as::

    map f1 launch --allow-remote-control shitty +shitten broadcast

Then press the :kbd:`F1` key and whatever you type in the newly created window
will be sent to all shitty windows.

You can use the options described below to control which windows are selected.

For example, only broadcast to other windows in the current tab::

    map f1 launch --allow-remote-control shitty +shitten broadcast --match-tab state:focused

.. program:: shitty +shitten broadcast


.. include:: /generated/cli-shitten-broadcast.rst
