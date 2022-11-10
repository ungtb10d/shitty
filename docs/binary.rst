Install shitty
========================

Binary install
----------------

.. highlight:: sh

You can install pre-built binaries of |shitty| if you are on macOS or Linux using
the following simple command:

.. code-block:: sh

    _shitty_install_cmd


The binaries will be installed in the standard location for your OS,
:file:`/Applications/shitty.app` on macOS and :file:`~/.local/shitty.app` on
Linux. The installer only touches files in that directory. To update shitty,
simply re-run the command.

.. warning::
   **Do not** copy the shitty binary out of the installation folder. If you want
   to add it to your :envvar:`PATH`, create a symlink in :file:`~/.local/bin` or
   :file:`/usr/bin` or wherever.


Manually installing
---------------------

If something goes wrong or you simply do not want to run the installer, you can
manually download and install |shitty| from the `GitHub releases page
<https://github.com/ungtb10d/shitty/releases>`__. If you are on macOS, download
the :file:`.dmg` and install as normal. If you are on Linux, download the
tarball and extract it into a directory. The |shitty| executable will be in the
:file:`bin` sub-directory.


Desktop integration on Linux
--------------------------------

If you want the shitty icon to appear in the taskbar and an entry for it to be
present in the menus, you will need to install the :file:`shitty.desktop` file.
The details of the following procedure may need to be adjusted for your
particular desktop, but it should work for most major desktop environments.

.. code-block:: sh

    # Create a symbolic link to add shitty to PATH (assuming ~/.local/bin is in
    # your system-wide PATH)
    ln -s ~/.local/shitty.app/bin/shitty ~/.local/bin/
    # Place the shitty.desktop file somewhere it can be found by the OS
    cp ~/.local/shitty.app/share/applications/shitty.desktop ~/.local/share/applications/
    # If you want to open text files and images in shitty via your file manager also add the shitty-open.desktop file
    cp ~/.local/shitty.app/share/applications/shitty-open.desktop ~/.local/share/applications/
    # Update the paths to the shitty and its icon in the shitty.desktop file(s)
    sed -i "s|Icon=shitty|Icon=/home/$USER/.local/shitty.app/share/icons/hicolor/256x256/apps/shitty.png|g" ~/.local/share/applications/shitty*.desktop
    sed -i "s|Exec=shitty|Exec=/home/$USER/.local/shitty.app/bin/shitty|g" ~/.local/share/applications/shitty*.desktop

.. note::
    In :file:`shitty-open.desktop`, shitty is registered to handle some supported
    MIME types. This will cause shitty to take precedence on some systems where
    the default apps are not explicitly set. For example, you expect to use
    other GUI file managers to open dir paths when using commands such as
    :program:`xdg-open`, you should configure the default opener for the MIME
    type ``inode/directory``::

        xdg-mime default org.kde.dolphin.desktop inode/directory

.. note::
    If you use the venerable `stow <https://www.gnu.org/software/stow/>`__
    command to manage your manual installations, the following takes care of the
    above for you (use with :code:`dest=~/.local/stow`)::

        cd ~/.local/stow
        stow -v shitty.app


Customizing the installation
--------------------------------

.. _nightly:

* You can install the latest nightly shitty build with ``installer``:

  .. code-block:: sh

     _shitty_install_cmd \
         installer=nightly

  If you want to install it in parallel to the released shitty specify a
  different install locations with ``dest``:

  .. code-block:: sh

     _shitty_install_cmd \
         installer=nightly dest=/some/other/location

* You can specify a different install location, with ``dest``:

  .. code-block:: sh

     _shitty_install_cmd \
         dest=/some/other/location

* You can tell the installer not to launch |shitty| after installing it with
  ``launch=n``:

  .. code-block:: sh

     _shitty_install_cmd \
         launch=n

* You can use a previously downloaded dmg/tarball, with ``installer``:

  .. code-block:: sh

     _shitty_install_cmd \
         installer=/path/to/dmg or tarball


Uninstalling
----------------

All the installer does is copy the shitty files into the install directory. To
uninstall, simply delete that directory.


Building from source
------------------------

|shitty| is easy to build from source, follow the :doc:`instructions <build>`.
