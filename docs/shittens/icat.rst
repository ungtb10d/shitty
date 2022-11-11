icat - Display images in the terminal
========================================

The ``icat`` shitten can be used to display arbitrary images in the |shitty|
terminal. Using it is as simple as::

    shitty +shitten icat image.jpeg

It supports all image types supported by `ImageMagick
<https://www.imagemagick.org>`_. It even works over SSH. For details, see
the :doc:`shitty graphics protocol </graphics-protocol>`.

You might want to create an alias in your shell's configuration files::

   alias icat="shitty +shitten icat"

Then you can simply use ``icat image.png`` to view images.

.. note::

    `ImageMagick <https://www.imagemagick.org>`_ must be installed for ``icat`` to
    work.

.. note::

    shitty's image display protocol may not work when used within a terminal
    multiplexer such as ``screen`` or ``tmux``, depending on whether the
    multiplexer has added support for it or not.


.. program:: shitty +shitten icat


The ``icat`` shitten has various command line arguments to allow it to be used
from inside other programs to display images. In particular, :option:`--place`,
:option:`--detect-support` and :option:`--print-window-size`.

Command Line Interface
--------------------------

.. include:: /generated/cli-shitten-icat.rst
