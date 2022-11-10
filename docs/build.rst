Build from source
==================

.. image:: https://github.com/ungtb10d/shitty/workflows/CI/badge.svg
  :alt: Build status
  :target: https://github.com/ungtb10d/shitty/actions?query=workflow%3ACI

.. highlight:: sh

|shitty| is designed to run from source, for easy hack-ability. Make sure the
following dependencies are installed first.

.. note::
   If you just want to test the latest changes to shitty, you don't need to build
   from source. Instead install the :ref:`latest nightly build <nightly>`.

.. note::
   If you are making small changes only to the Python parts of shitty, there is
   no need to build shitty at all, instead, assuming you have installed the
   official shitty binaries, you can simply set the :envvar:`shitty_DEVELOP_FROM`
   enviroment variable to point to the directory into which you have checked out
   the shitty source code. shitty will then load its Python code from there. You
   should use a version of the source that matches the binary version as closely
   as possible, since the two are tightly coupled.


Dependencies
----------------

Run-time dependencies:

* ``python`` >= 3.8
* ``harfbuzz`` >= 2.2.0
* ``zlib``
* ``libpng``
* ``liblcms2``
* ``librsync``
* ``openssl``
* ``freetype`` (not needed on macOS)
* ``fontconfig`` (not needed on macOS)
* ``libcanberra`` (not needed on macOS)
* ``ImageMagick`` (optional, needed to use the ``shitty +shitten icat`` tool to display images in the terminal)
* ``pygments`` (optional, needed for syntax highlighting in ``shitty +shitten diff``)


Build-time dependencies:

* ``gcc`` or ``clang``
* ``pkg-config``
* For building on Linux in addition to the above dependencies you might also
  need to install the following packages, if they are not already installed by
  your distro:

  - ``libdbus-1-dev``
  - ``libxcursor-dev``
  - ``libxrandr-dev``
  - ``libxi-dev``
  - ``libxinerama-dev``
  - ``libgl1-mesa-dev``
  - ``libxkbcommon-x11-dev``
  - ``libfontconfig-dev``
  - ``libx11-xcb-dev``
  - ``liblcms2-dev``
  - ``libpython3-dev``
  - ``librsync-dev``


Install and run from source
------------------------------

.. code-block:: sh

    git clone https://github.com/ungtb10d/shitty && cd shitty

Now build the native code parts of |shitty| with the following command::

    make

You can run |shitty|, as::

    ./shitty/launcher/shitty

If that works, you can create a symlink to the launcher in :file:`~/bin` or some
other directory on your PATH so that you can run |shitty| using just ``shitty``.

To have the shitty documentation available locally, run::

    python3 -m pip install -r docs/requirements.txt && make docs


Building shitty.app on macOS from source
-------------------------------------------

Run::

    python3 -m pip install -r docs/requirements.txt && make docs
    make app

Building the docs needs to be done only once.

This :file:`shitty.app` unlike the released one does not include its own copy of
Python and the other dependencies. So if you ever un-install/upgrade those
dependencies you might have to rebuild the app.

.. note::
   The released :file:`shitty.dmg` includes all dependencies, unlike the
   :file:`shitty.app` built above and is built automatically by using the
   `bypy framework <https://github.com/ungtb10d/bypy>`__ however, that is
   designed to run on Linux and is not for the faint of heart.

.. note::
   Apple disallows certain functionality, such as notifications for unsigned
   applications. If you need this functionality, you can try signing the built
   :file:`shitty.app` with a self signed certificate, see for example, `here
   <https://stackoverflow.com/questions/27474751/how-can-i-codesign-an-app-without-being-in-the-mac-developer-program/27474942>`__.

.. note::
   If you are facing issues with ``linker`` while building, try with a ``brew``
   installed Python instead, see :iss:`289` for more discussion.


Build and run from source with Nix
-------------------------------------------

On NixOS or any other Linux or macOS system with the Nix package manager
installed, execute `nix-shell
<https://nixos.org/guides/nix-pills/developing-with-nix-shell.html>`__ to create
the correct environment to build shitty or use ``nix-shell --pure`` instead to
eliminate most of the influence of the outside system, e.g. globally installed
packages. ``nix-shell`` will automatically fetch all required dependencies and
make them available in the newly spawned shell.

Then proceed with ``make`` or ``make app`` according to the platform specific
instructions above.


Debug builds
--------------

A basic debug build can be done with::

    make debug

This includes debug info in the binary for better traces. To build with address
sanitizer, use::

    make asan

Which will result in a debug binary that uses the address sanitizer as well.

.. _packagers:

Notes for Linux/macOS packagers
----------------------------------

The released |shitty| source code is available as a `tarball`_ from
`the GitHub releases page <https://github.com/ungtb10d/shitty/releases>`__.

While |shitty| does use Python, it is not a traditional Python package, so please
do not install it in site-packages.
Instead run::

    make linux-package

This will install |shitty| into the directory :file:`linux-package`. You can run
|shitty| with :file:`linux-package/bin/shitty`. All the files needed to run shitty
will be in :file:`linux-package/lib/shitty`. The terminfo file will be installed
into :file:`linux-package/share/terminfo`. Simply copy these files into
:file:`/usr` to install |shitty|. In other words, :file:`linux-package` is the
staging area into which |shitty| is installed. You can choose a different staging
area, by passing the ``--prefix`` argument to :file:`setup.py`.

You should probably split |shitty| into three packages:

:code:`shitty-terminfo`
    Installs the terminfo file

:code:`shitty-shell-integration`
    Installs the shell integration scripts (the contents of the
    shell-integration directory in the shitty source code), probably to
    :file:`/usr/share/shitty/shell-integration`

:code:`shitty`
    Installs the main program

This allows users to install the terminfo and shell integration files on
servers into which they ssh, without needing to install all of |shitty|. The
shell integration files **must** still be present in
:file:`lib/shitty/shell-integration` when installing the shitty main package as
the shitty program expects to find them there.

.. note::
   You need a couple of extra dependencies to build linux-package. :file:`tic`
   to compile terminfo files, usually found in the development package of
   :file:`ncurses`. Also, if you are building from a git checkout instead of the
   released source code tarball, you will need to install the dependencies from
   :file:`docs/requirements.txt` to build the shitty documentation. They can be
   installed most easily with ``python -m pip -r docs/requirements.txt``.

This applies to creating packages for |shitty| for macOS package managers such as
Homebrew or MacPorts as well.
