:tocdepth: 2

Controlling shitty from scripts or the shell
==============================================

.. highlight:: sh

Tutorial
----------

|shitty| can be controlled from scripts or the shell prompt. You can open new
windows, send arbitrary text input to any window, name windows and tabs, etc.
Let's walk through a few examples of controlling |shitty|.

Start by running |shitty| as::

    shitty -o allow_remote_control=yes -o enabled_layouts=tall

In order for control to work, :opt:`allow_remote_control` must be enabled in
:file:`shitty.conf`. Here we turn it on explicitly at the command line.

Now, in the new |shitty| window, enter the command::

    shitty @ launch --title Output --keep-focus cat

This will open a new window, running the ``cat`` program that will appear next
to the current window.

Let's send some text to this new window::

    shitty @ send-text --match cmdline:cat Hello, World

This will make ``Hello, World`` show up in the window running the ``cat`` program.
The :option:`shitty @ send-text --match` option is very powerful, it allows selecting windows by their
titles, the command line of the program running in the window, the working
directory of the program running in the window, etc.  See ``shitty @ send-text
--help`` for details.

More usefully, you can pipe the output of a command running in one window to
another window, for example::

    ls | shitty @ send-text --match title:Output --stdin

This will show the output of ls in the output window instead of the current
window. You can use this technique to, for example, show the output of running
``make`` in your editor in a different window. The possibilities are endless.

You can even have things you type show up in a different window. Run::

    shitty @ send-text --match title:Output --stdin

And type some text, it will show up in the output window, instead of the current
window. Type ``Ctrl+D`` when you are ready to stop.

Now, let's open a new tab::

   shitty @ launch --type=tab --tab-title "My Tab" --keep-focus bash

This will open a new tab running the bash shell with the title "My Tab".
We can change the title of the tab with::

   shitty @ set-tab-title --match title:My  New Title

Let's change the title of the current tab::

   shitty @ set-tab-title Master Tab

Now lets switch to the newly opened tab::

   shitty @ focus-tab --match title:New

Similarly, to focus the previously opened output window (which will also switch
back to the old tab, automatically)::

   shitty @ focus-window --match title:Output

You can get a listing of available tabs and windows, by running::

   shitty @ ls

This outputs a tree of data in JSON format. The top level of the tree is all
operating system shitty windows. Each OS window has an id and a list of tabs.
Each tab has its own id, a title and a list of windows. Each window has an id,
title, current working directory, process id (PID) and command-line of the
process running in the window. You can use this information with :option:`shitty @ focus-window --match`
to control individual windows.

As you can see, it is very easy to control |shitty| using the
``shitty @`` messaging system. This tutorial touches only the
surface of what is possible. See ``shitty @ --help`` for more details.

Note that in the example's above, ``shitty @`` messaging works only when run inside a |shitty| window,
not anywhere. But, within a |shitty| window it even works over SSH. If you want to control
|shitty| from programs/scripts not running inside a |shitty| window, you have to implement a couple of
extra steps. First start |shitty| as::

    shitty -o allow_remote_control=yes --listen-on unix:/tmp/myshitty

The :option:`shitty --listen-on` option tells |shitty| to listen for control messages at the
specified path. See ``shitty --help`` for details. Now you can control this
instance of |shitty| using the :option:`shitty @ --to` command line argument to ``shitty @``. For example::

    shitty @ --to unix:/tmp/myshitty ls


Note that if all you want to do is run a single |shitty| "daemon" and have subsequent
|shitty| invocations appear as new top-level windows, you can use the simpler :option:`shitty --single-instance`
option, see ``shitty --help`` for that.

The builtin shitty shell
--------------------------

You can explore the |shitty| command language more easily using the builtin |shitty|
shell. Run ``shitty @`` with no arguments and you will be dropped into the |shitty|
shell with completion for |shitty| command names and options.

You can even open the |shitty| shell inside a running |shitty| using a simple
keyboard shortcut (:sc:`shitty_shell` by default).

.. note:: This has the added advantage that you don't need to use
   ``allow_remote_control`` to make it work.


Allowing only some windows to control shitty
----------------------------------------------

If you do not want to allow all programs running in |shitty| to control it, you can selectively
enable remote control for only some |shitty| windows. Simply create a shortcut
such as::

    map ctrl+k launch --allow-remote-control some_program

Then programs running in windows created with that shortcut can use ``shitty @``
to control shitty. Note that any program with the right level of permissions can
still write to the pipes of any other program on the same computer and
therefore can control |shitty|. It can, however, be useful to block programs
running on other computers (for example, over ssh) or as other users.

.. note:: You dont need ``allow_remote_control`` to make this work as it is
   limited to only programs running in that specific window. Be careful with
   what programs you run in such windows, since they can effectively control
   shitty, as if you were running with ``allow_remote_control`` turned on.


Mapping key presses to remote control commands
--------------------------------------------------

If you wish to trigger a remote control command easily with just a keypress,
you can map it in :file:`shitty.conf`. For example::

    map F1 remote_control set-spacing margin=30

Then pressing the :kbd:`F1` key will set the active window margins to 30.
The syntax for what follows :code:`remote_control` is exactly the same
as the syntax for what follows :code:`shitty @` above.

.. note:: You do not need ``allow_remote_control`` to use these mappings,
   as they are not actual remote programs, but are simply a way to resuse
   the remote control infrastructure via keybings.


Broadcasting what you type to all shitty windows
--------------------------------------------------

As a simple illustration of the power of remote control, lets
have what we type sent to all open shitty windows. To do that define the
following mapping in :file:`shitty.conf`::

    map F1 launch --allow-remote-control shitty +shitten broadcast

Now press, F1 and start typing, what you type will be sent to all windows,
live, as you type it.


Documentation for the remote control protocol
-----------------------------------------------

If you wish to develop your own client to talk to |shitty|, you
can use the :doc:`rc_protocol`.

.. include:: generated/cli-shitty-at.rst
