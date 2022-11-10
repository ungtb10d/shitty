Hyperlinked grep
=================

This shitten allows you to search your files using `ripgrep
<https://github.com/BurntSushi/ripgrep>`__ and open the results directly in your
favorite editor in the terminal, at the line containing the search result,
simply by clicking on the result you want.

.. versionadded:: 0.19.0

To set it up, first create :file:`~/.config/shitty/open-actions.conf` with the
following contents:

.. code:: conf

    # Open any file with a fragment in vim, fragments are generated
    # by the hyperlink_grep shitten and nothing else so far.
    protocol file
    fragment_matches [0-9]+
    action launch --type=overlay --cwd=current vim +${FRAGMENT} ${FILE_PATH}

    # Open text files without fragments in the editor
    protocol file
    mime text/*
    action launch --type=overlay --cwd=current ${EDITOR} ${FILE_PATH}

Now, run a search with::

    shitty +shitten hyperlinked_grep something

Hold down the :kbd:`Ctrl+Shift` keys and click on any of the result lines, to
open the file in :program:`vim` at the matching line. If you use some editor
other than :program:`vim`, you should adjust the :file:`open-actions.conf` file
accordingly.

Finally, add an alias to your shell's rc files to invoke the shitten as
:command:`hg`::

    alias hg="shitty +shitten hyperlinked_grep"


You can now run searches with::

    hg some-search-term

If you want to enable completion, for the shitten, you can delegate completion
to :program:`rg`. How to do that varies based on the shell:


.. tab:: zsh

    Instead of using an alias, create a simple wrapper script named
    :program:`hg` somewhere in your :envvar:`PATH`:

    .. code-block:: sh

        #!/bin/sh
        exec shitty +shitten hyperlinked_grep "$@"

    Then, add the following to :file:`.zshrc`::

        compdef _rg hg

.. tab:: fish

    You can combine both the aliasing/wrapping and pointing fish to ripgrep's
    autocompletion with a fish wrapper function in your :file:`config.fish`
    or :file:`~/.config/fish/functions/hg.fish`:

    .. code-block:: fish

        function hg --wraps rg; shitty +shitten hyperlinked_grep $argv; end

To learn more about shitty's powerful framework for customizing URL click
actions, see :doc:`here </open_actions>`.

By default, this shitten adds hyperlinks for several parts of ripgrep output:
the per-file header, match context lines, and match lines. You can control
which items are linked with a :command:`--shitten hyperlink` flag. For example,
:command:`--shitten hyperlink=matching_lines` will only add hyperlinks to the
match lines. :command:`--shitten hyperlink=file_headers,context_lines` will link
file headers and context lines but not match lines. :command:`--shitten
hyperlink=none` will cause the command line to be passed to directly to
:command:`rg` so no hyperlinking will be performed. :command:`--shitten
hyperlink` may be specified multiple times.

Hopefully, someday this functionality will make it into some `upstream grep
<https://github.com/BurntSushi/ripgrep/issues/665>`__ program directly removing
the need for this shitten.


.. note::
   While you can pass any of ripgrep's comand line options to the shitten and
   they will be forwarded to :program:`rg`, do not use options that change the
   output formatting as the shitten works by parsing the output from ripgrep.
