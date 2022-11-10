Control shitty from scripts
----------------------------

.. highlight:: sh

|shitty| can be controlled from scripts or the shell prompt. You can open new
windows, send arbitrary text input to any window, change the title of windows
and tabs, etc.

Let's walk through a few examples of controlling |shitty|.


Tutorial
------------

Start by running |shitty| as::

    shitty -o allow_remote_control=yes -o enabled_layouts=tall

In order for control to work, :opt:`allow_remote_control` or
:opt:`remote_control_password` must be enabled in :file:`shitty.conf`. Here we
turn it on explicitly at the command line.

Now, in the new |shitty| window, enter the command::

    shitty @ launch --title Output --keep-focus cat

This will open a new window, running the :program:`cat` program that will appear
next to the current window.

Let's send some text to this new window::

    shitty @ send-text --match cmdline:cat Hello, World

This will make ``Hello, World`` show up in the window running the :program:`cat`
program. The :option:`shitty @ send-text --match` option is very powerful, it
allows selecting windows by their titles, the command line of the program
running in the window, the working directory of the program running in the
window, etc. See :ref:`shitty @ send-text --help <at-send-text>` for details.

More usefully, you can pipe the output of a command running in one window to
another window, for example::

    ls | shitty @ send-text --match 'title:^Output' --stdin

This will show the output of :program:`ls` in the output window instead of the
current window. You can use this technique to, for example, show the output of
running :program:`make` in your editor in a different window. The possibilities
are endless.

You can even have things you type show up in a different window. Run::

    shitty @ send-text --match 'title:^Output' --stdin

And type some text, it will show up in the output window, instead of the current
window. Type :kbd:`Ctrl+D` when you are ready to stop.

Now, let's open a new tab::

   shitty @ launch --type=tab --tab-title "My Tab" --keep-focus bash

This will open a new tab running the bash shell with the title "My Tab".
We can change the title of the tab to "New Title" with::

   shitty @ set-tab-title --match 'title:^My' New Title

Let's change the title of the current tab::

   shitty @ set-tab-title Master Tab

Now lets switch to the newly opened tab::

   shitty @ focus-tab --match 'title:^New'

Similarly, to focus the previously opened output window (which will also switch
back to the old tab, automatically)::

   shitty @ focus-window --match 'title:^Output'

You can get a listing of available tabs and windows, by running::

   shitty @ ls

This outputs a tree of data in JSON format. The top level of the tree is all
:term:`OS windows <os_window>`. Each OS window has an id and a list of
:term:`tabs <tab>`. Each tab has its own id, a title and a list of :term:`shitty
windows <window>`. Each window has an id, title, current working directory,
process id (PID) and command-line of the process running in the window. You can
use this information with :option:`shitty @ focus-window --match` to control
individual windows.

As you can see, it is very easy to control |shitty| using the ``shitty @``
messaging system. This tutorial touches only the surface of what is possible.
See ``shitty @ --help`` for more details.

In the example's above, ``shitty @`` messaging works only when run
inside a |shitty| window, not anywhere. But, within a |shitty| window it even
works over SSH. If you want to control |shitty| from programs/scripts not running
inside a |shitty| window, see the section on :ref:`using a socket for remote control <rc_via_socket>`
below.


Note that if all you want to do is run a single |shitty| "daemon" and have
subsequent |shitty| invocations appear as new top-level windows, you can use the
simpler :option:`shitty --single-instance` option, see ``shitty --help`` for that.


.. _rc_via_socket:

Remote control via a socket
--------------------------------
First, start |shitty| as::

    shitty -o allow_remote_control=yes --listen-on unix:/tmp/mykitty

The :option:`shitty --listen-on` option tells |shitty| to listen for control
messages at the specified UNIX-domain socket. See ``shitty --help`` for details.
Now you can control this instance of |shitty| using the :option:`shitty @ --to`
command line argument to ``shitty @``. For example::

    shitty @ --to unix:/tmp/mykitty ls


The builtin shitty shell
--------------------------

You can explore the |shitty| command language more easily using the builtin
|shitty| shell. Run ``shitty @`` with no arguments and you will be dropped into
the |shitty| shell with completion for |shitty| command names and options.

You can even open the |shitty| shell inside a running |shitty| using a simple
keyboard shortcut (:sc:`kitty_shell` by default).

.. note:: This has the added advantage that you don't need to use
   :opt:`allow_remote_control` to make it work.


Allowing only some windows to control shitty
----------------------------------------------

If you do not want to allow all programs running in |shitty| to control it, you
can selectively enable remote control for only some |shitty| windows. Simply
create a shortcut such as::

    map ctrl+k launch --allow-remote-control some_program

Then programs running in windows created with that shortcut can use ``shitty @``
to control shitty. Note that any program with the right level of permissions can
still write to the pipes of any other program on the same computer and therefore
can control |shitty|. It can, however, be useful to block programs running on
other computers (for example, over SSH) or as other users.

.. note:: You don't need :opt:`allow_remote_control` to make this work as it is
   limited to only programs running in that specific window. Be careful with
   what programs you run in such windows, since they can effectively control
   shitty, as if you were running with :opt:`allow_remote_control` turned on.

    You can further restrict what is allowed in these windows by using
    :option:`shitty @ launch --remote-control-password`.


Fine grained permissions for remote control
----------------------------------------------

.. versionadded:: 0.26.0

The :opt:`allow_remote_control` option discussed so far is a blunt
instrument, granting the ability to any program running on your computer
or even on remote computers via SSH the ability to use remote control.

You can instead define remote control passwords that can be used to grant
different levels of control to different places. You can even write your
own script to decide which remote control requests are allowed. This is
done using the :opt:`remote_control_password` option in :file:`shitty.conf`.
Set :opt:`allow_remote_control` to :code:`password` to use this feature.
Let's see some examples:

.. code-block:: conf

   remote_control_password "control colors" get-colors set-colors

Now, using this password, you can, in scripts run the command::

    shitty @ --password="control colors" set-colors background=red

Any script with access to the password can now change colors in shitty using
remote control, but only that and nothing else. You can even supply the
password via the :envvar:`KITTY_RC_PASSWORD` environment variable, or the
file :file:`~/.config/shitty/rc-password` to avoid having to type it repeatedly.
See :option:`shitty @ --password-file` and :option:`shitty @ --password-env`.

The :opt:`remote_control_password` can be specified multiple times to create
different passwords with different capabilities. Run the following to get a
list of all action names::

    shitty @ --help

You can even use glob patterns to match action names, for example:

.. code-block:: conf

   remote_control_password "control colors" *-colors

If no action names are specified, all actions are allowed.

If ``shitty @`` is run with a password that is not present in
:file:`shitty.conf`, then shitty will interactively prompt the user to allow or
disallow the remote control request. The user can choose to allow or disallow
either just that request or all requests using that password. The user's
decision is remembered for the duration of that shitty instance.

.. note::
   For password based authentication to work over SSH, you must pass the
   :envvar:`KITTY_PUBLIC_KEY` environment variable to the remote host. The
   :doc:`ssh shitten <kittens/ssh>` does this for you automatically. When
   using a password, :ref:`rc_crypto` is used to ensure the password
   is kept secure. This does mean that using password based authentication
   is slower as the entire command is encrypted before transmission. This
   can be noticeable when using a command like ``shitty @ set-background-image``
   which transmits large amounts of image data. Also, the clock on the remote
   system must match (within a few minutes) the clock on the local system.
   shitty uses a time based nonce to minimise the potential for replay attacks.

.. _rc_custom_auth:

Customizing authorization with your own program
____________________________________________________________

If the ability to control access by action names is not fine grained enough,
you can define your own Python script to examine every remote control command
and allow/disallow it. To do so create a file in the shitty configuration
directory, :file:`~/.config/shitty/my_rc_auth.py` and add the following
to :file:`shitty.conf`:

.. code-block:: conf

    remote_control_password "testing custom auth" my_rc_auth.py

:file:`my_rc_auth.py` should define a :code:`is_cmd_allowed` function
as shown below:

.. code-block:: py

    def is_cmd_allowed(pcmd, window, from_socket, extra_data):
        cmd_name = pcmd['cmd']  # the name of the command
        cmd_payload = pcmd['payload']  # the arguments to the command
        # examine the cmd_name and cmd_payload and return True to allow
        # the command or False to disallow it. Return None to have no
        # effect on the command.

        # The command payload will vary from command to command, see
        # the rc protocol docs for details. Below is an example of
        # restricting the launch command to allow only running the
        # default shell.

        if cmd_name != 'launch':
            return None
        if cmd_payload.get('args') or cmd_payload.get('env') or cmd_payload.get('copy_cmdline') or cmd_payload.get('copy_env'):
            return False
        # prints in this function go to the parent shitty process STDOUT
        print('Allowing launch command:', cmd_payload)
        return True


.. _rc_mapping:

Mapping key presses to remote control commands
--------------------------------------------------

If you wish to trigger a remote control command easily with just a keypress,
you can map it in :file:`shitty.conf`. For example::

    map f1 remote_control set-spacing margin=30

Then pressing the :kbd:`F1` key will set the active window margins to
:code:`30`. The syntax for what follows :ac:`remote_control` is exactly the same
as the syntax for what follows :code:`shitty @` above.

If you wish to ignore errors from the command, prefix the command with an
``!``. For example, the following will not return an error when no windows
are matched::

    map f1 remote_control !focus-window --match XXXXXX

.. note:: You do not need :opt:`allow_remote_control` to use these mappings,
   as they are not actual remote programs, but are simply a way to resuse the
   remote control infrastructure via keybings.


Broadcasting what you type to all shitty windows
--------------------------------------------------

As a simple illustration of the power of remote control, lets
have what we type sent to all open shitty windows. To do that define the
following mapping in :file:`shitty.conf`::

    map f1 launch --allow-remote-control shitty +shitten broadcast

Now press :kbd:`F1` and start typing, what you type will be sent to all windows,
live, as you type it.


The remote control protocol
-----------------------------------------------

If you wish to develop your own client to talk to |shitty|, you can use the
:doc:`remote control protocol specification <rc_protocol>`.


.. _search_syntax:

Matching windows and tabs
----------------------------

Many remote control operations operate on windows or tabs. To select these, the
:code:`--match` option is often used. This allows matching using various
sophisticated criteria such as title, ids, cmdlines, etc. These criteria are
expressions of the form :code:`field:query`. Where :italic:`field` is the field
against which to match and :italic:`query` is the expression to match. They can
be further combined using Boolean operators, best illustrated with some
examples::

    title:"My special window" or id:43
    title:bash and env:USER=kovid
    not id:1
    (id:2 or id:3) and title:something

.. toctree::
   :hidden:

   rc_protocol

.. include:: generated/cli-shitty-at.rst
