shitty - Binary install
========================

.. |ins| replace:: curl -L :literal:`https://sw.ungtb10d.net/shitty/installer.sh` | sh /dev/stdin

.. highlight:: sh

You can install pre-built binaries of |shitty| if you are on macOS or Linux using
the following simple command:

.. parsed-literal::
    :class: pre

    |ins|


The binaries will be installed in the standard location for your OS,
:file:`/Applications/shitty.app` on macOS and :file:`~/.local/shitty.app` on
Linux. The installer only touches files in that directory. To update shitty,
simply re-run the command.


Manually installing
---------------------

If something goes wrong or you simply do not want to run the installer, you can
manually download and install |shitty| from the `GitHub releases page
<https://github.com/ungtb10d/shitty/releases>`_. If you are on macOS, download
the :file:`.dmg` and install as normal. If you are on Linux, download the tarball
and extract it into a directory. The |shitty| executable will be in the
:file:`bin` sub-directory.

Desktop integration on Linux
--------------------------------

If you want the shitty icon to appear in the taskbar and an entry for it to be
present in the menus, you will need to install the :file:`shitty.desktop` file.
The details of the following procedure may need to be adjusted for your
particular desktop, but it should work for most major desktop environments.

.. code-block:: sh

    # Create a symbolic link to add shitty to PATH (assuming ~/.local/bin is in
    # your PATH)
    ln -s ~/.local/shitty.app/bin/shitty ~/.local/bin/
    # Place the shitty.desktop file somewhere it can be found by the OS
    cp ~/.local/shitty.app/share/applications/shitty.desktop ~/.local/share/applications/
    # Update the path to the shitty icon in the shitty.desktop file
    sed -i "s|Icon=shitty|Icon=/home/$USER/.local/shitty.app/share/icons/hicolor/256x256/apps/shitty.png|g" ~/.local/share/applications/shitty.desktop

.. note::
    If you use the venerable `stow <https://www.gnu.org/software/stow/>`_
    command to manage your manual installations, the following takes care of the
    above for you (use with :file:`dest=~/.local/stow`)::

        cd ~/.local/stow
        stow -v shitty.app


Customizing the installation
--------------------------------

* You can specify a different install location, with ``dest``:

  .. parsed-literal::
     :class: pre

     |ins| \\
         dest=/some/other/location

* You can tell the installer not to launch |shitty| after installing it with
  ``launch=n``:

  .. parsed-literal::
     :class: pre

     |ins| \\
         launch=n

* You can use a previously downloaded dmg/tarball, with ``installer``:

  .. parsed-literal::
     :class: pre

     |ins| \\
         installer=/path/to/dmg or tarball

Uninstalling
----------------

All the installer does is copy the shitty files into the install directory. To
uninstall, simply delete that directory.


Building from source
------------------------

|shitty| is easy to build from source, follow the :doc:`instructions <build>`.
