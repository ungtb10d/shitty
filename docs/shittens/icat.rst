icat
========================================

*Display images in the terminal*

The ``icat`` shitten can be used to display arbitrary images in the |shitty|
terminal. Using it is as simple as::

    shitty +shitten icat image.jpeg

It supports all image types supported by `ImageMagick
<https://www.imagemagick.org>`__. It even works over SSH. For details, see the
:doc:`shitty graphics protocol </graphics-protocol>`.

You might want to create an alias in your shell's configuration files::

   alias icat="shitty +shitten icat"

Then you can simply use ``icat image.png`` to view images.

.. note::

    `ImageMagick <https://www.imagemagick.org>`__ must be installed for icat
    shitten to work.

.. note::

    shitty's image display protocol may not work when used within a terminal
    multiplexer such as :program:`screen` or :program:`tmux`, depending on
    whether the multiplexer has added support for it or not.


.. program:: shitty +shitten icat


The ``icat`` shitten has various command line arguments to allow it to be used
from inside other programs to display images. In particular, :option:`--place`,
:option:`--detect-support`, :option:`--silent` and
:option:`--print-window-size`.

If you are trying to integrate icat into a complex program like a file manager
or editor, there are a few things to keep in mind. icat works by communicating
over the TTY device, it both writes to and reads from the TTY. So it is
imperative that while it is running the host program does not do any TTY I/O.
Any key presses or other input from the user on the TTY device will be
discarded. At a minimum, you should use the :option:`--silent` and
:option:`--transfer-mode` command line arguments. To be really robust you should
consider writing proper support for the :doc:`shitty graphics protocol
</graphics-protocol>` in the program instead. Nowadays there are many libraries
that have support for it.


.. include:: /generated/cli-shitten-icat.rst
