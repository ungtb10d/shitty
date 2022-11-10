.. _shittens:

Extend with shittens
-----------------------

.. toctree::
   :hidden:
   :glob:

   shittens/icat
   shittens/diff
   shittens/unicode_input
   shittens/themes
   shittens/hints
   shittens/remote_file
   shittens/hyperlinked_grep
   shittens/transfer
   shittens/ssh
   shittens/custom
   shittens/*

|shitty| has a framework for easily creating terminal programs that make use of
its advanced features. These programs are called shittens. They are used both to
add features to |shitty| itself and to create useful standalone programs.
Some prominent shittens:

:doc:`icat <shittens/icat>`
    Display images in the terminal


:doc:`diff <shittens/diff>`
    A fast, side-by-side diff for the terminal with syntax highlighting and
    images


:doc:`Unicode input <shittens/unicode_input>`
    Easily input arbitrary Unicode characters in |shitty| by name or hex code.


:doc:`Hints <shittens/hints>`
    Select and open/paste/insert arbitrary text snippets such as URLs,
    filenames, words, lines, etc. from the terminal screen.


:doc:`Remote file <shittens/remote_file>`
    Edit, open, or download remote files over SSH easily, by simply clicking on
    the filename.


:doc:`Transfer files <shittens/transfer>`
    Transfer files and directories seamlessly and easily from remote machines
    over your existing SSH sessions with a simple command.


:doc:`Hyperlinked grep <shittens/hyperlinked_grep>`
    Search your files using `ripgrep <https://github.com/BurntSushi/ripgrep>`__
    and open the results directly in your favorite editor in the terminal,
    at the line containing the search result, simply by clicking on the result
    you want.


:doc:`Broadcast <shittens/broadcast>`
    Type in one :term:`shitty window <window>` and have it broadcast to all (or a
    subset) of other :term:`shitty windows <window>`.


:doc:`SSH <shittens/ssh>`
    SSH with automatic :ref:`shell integration <shell_integration>`, connection
    re-use for low latency and easy cloning of local shell and editor
    configuration to the remote host.


:doc:`Panel <shittens/panel>`
    Draw a GPU accelerated dock panel on your desktop showing the output from an
    arbitrary terminal program.


:doc:`Clipboard <shittens/clipboard>`
    Copy/paste to the clipboard from shell scripts, even over SSH.

You can also :doc:`Learn to create your own shittens <shittens/custom>`.
