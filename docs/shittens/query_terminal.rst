Query terminal
=================

Used to query shitty from terminal programs about version, values of various
runtime options controlling its features, etc.

The querying is done using the (*semi*) standard XTGETTCAP escape sequence
pioneered by XTerm, so it works over SSH as well. The downside is that it
is slow, since it requires a roundtrip to the terminal emulator and back.

If you want to do some of the same querying in your terminal program without
depending on the shitten, you can do so, by processing the same escape codes.
Search `this page <https://invisible-island.net/xterm/ctlseqs/ctlseqs.html>`_
for *XTGETTCAP* to see the syntax for the escape code and read the source
of this shitten to find the values of the keys for the various queries.


Command Line Interface
-------------------------

.. include:: ../generated/cli-shitten-query_terminal.rst
