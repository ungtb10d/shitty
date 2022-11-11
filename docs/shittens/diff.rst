shitty-diff - A fast side-by-side diff tool with syntax highlighting and images
================================================================================

.. highlight:: sh

Major Features
-----------------

.. container:: major-features

    * Displays diffs side-by-side in the shitty terminal

    * Does syntax highlighting of the displayed diffs, asynchronously, for maximum
      speed

    * Displays images as well as text diffs, even over SSH

    * Does recursive directory diffing


.. figure:: ../screenshots/diff.png
   :alt: Screenshot, showing a sample diff
   :align: center
   :scale: 100%

   Screenshot, showing a sample diff

.. contents::
   :local:


Installation
---------------

Simply :ref:`install shitty <quickstart>`.  You also need
to have either the `git <https://git-scm.com/>`_ program or the ``diff`` program
installed. Additionally, for syntax highlighting to work,
`pygments <http://pygments.org/>`_ must be installed (note that pygments is
included in the macOS shitty app).


Usage
--------

In the shitty terminal, run::

    shitty +shitten diff file1 file2

to see the diff between file1 and file2.

Create an alias in your shell's startup file to shorten the command, for example:

.. code-block:: sh

    alias d="shitty +shitten diff"

Now all you need to do to diff two files is::

    d file1 file2

You can also pass directories instead of files to see the recursive diff of the
directory contents.


Keyboard controls
----------------------

=========================   ===========================
Action                      Shortcut
=========================   ===========================
Quit                        :kbd:`q, Ctrl+c, Esc`
Scroll line up              :kbd:`k, up`
Scroll line down            :kbd:`j, down`
Scroll page up              :kbd:`PgUp`
Scroll page down            :kbd:`PgDn`
Scroll to top               :kbd:`Home`
Scroll to bottom            :kbd:`End`
Scroll to next page         :kbd:`Space, PgDn`
Scroll to previous page     :kbd:`PgUp`
Scroll to next change       :kbd:`n`
Scroll to previous change   :kbd:`p`
Increase lines of context   :kbd:`+`
Decrease lines of context   :kbd:`-`
All lines of context        :kbd:`a`
Restore default context     :kbd:`=`
Search forwards             :kbd:`/`
Search backwards            :kbd:`?`
Clear search                :kbd:`Esc`
Scroll to next match        :kbd:`>, .`
Scroll to previous match    :kbd:`<, ,`
=========================   ===========================


Integrating with git
-----------------------

Add the following to `~/.gitconfig`:

.. code-block:: ini

    [diff]
        tool = shitty
        guitool = shitty.gui
    [difftool]
        prompt = false
        trustExitCode = true
    [difftool "shitty"]
        cmd = shitty +shitten diff $LOCAL $REMOTE
    [difftool "shitty.gui"]
        cmd = shitty shitty +shitten diff $LOCAL $REMOTE

Now to use shitty-diff to view git diffs, you can simply do::

    git difftool --no-symlinks --dir-diff

Once again, creating an alias for this command is useful.


Why does this work only in shitty?
----------------------------------------

The diff shitten makes use of various features that are :doc:`shitty only
</protocol-extensions>`,  such as the :doc:`shitty graphics protocol
</graphics-protocol>`, the :ref:`extended keyboard protocol
<extended-key-protocol>`, etc. It also leverages terminal program
infrastructure I created for all of shitty's other shittens to reduce the amount
of code needed (the entire implementation is under 2000 lines of code).

And fundamentally, it's shitty only because I wrote it for myself, and I am
highly unlikely to use any other terminals :)



Configuration
------------------------

You can configure the colors used, keyboard shortcuts, the diff implementation,
the default lines of context, etc.  by creating a :file:`diff.conf` file in
your :ref:`shitty config folder <confloc>`. See below for the supported
configuration directives.


.. include:: /generated/conf-shitten-diff.rst


Command Line Interface
-------------------------

.. include:: /generated/cli-shitten-diff.rst



Sample diff.conf
-----------------

You can download a sample :file:`diff.conf` file with all default settings and
comments describing each setting by clicking: :download:`sample diff.conf
</generated/conf/diff.conf>`.
