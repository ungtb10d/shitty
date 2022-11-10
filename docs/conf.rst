shitty.conf
-----------------------

.. highlight:: conf

|shitty| is highly customizable, everything from keyboard shortcuts, to rendering
frames-per-second. See below for an overview of all customization possibilities.

You can open the config file within shitty by pressing :sc:`edit_config_file`
(:kbd:`⌘+,` on macOS). A :file:`shitty.conf` with commented default
configurations and descriptions will be created if the file does not exist.
You can reload the config file within shitty by pressing :sc:`reload_config_file`
(:kbd:`⌃+⌘+,` on macOS) or sending shitty the ``SIGUSR1`` signal.
You can also display the current configuration by pressing :sc:`debug_config`
(:kbd:`⌥+⌘+,` on macOS).

.. _confloc:

|shitty| looks for a config file in the OS config directories (usually
:file:`~/.config/shitty/shitty.conf`) but you can pass a specific path via the
:option:`shitty --config` option or use the :envvar:`shitty_CONFIG_DIRECTORY`
environment variable. See :option:`shitty --config` for full details.

Comments can be added to the config file as lines starting with the ``#``
character. This works only if the ``#`` character is the first character in the
line.

.. _include:

You can include secondary config files via the :code:`include` directive.  If
you use a relative path for :code:`include`, it is resolved with respect to the
location of the current config file. Note that environment variables are
expanded, so :code:`${USER}.conf` becomes :file:`name.conf` if
:code:`USER=name`. Also, you can use :code:`globinclude` to include files
matching a shell glob pattern and :code:`envinclude` to include configuration
from environment variables. For example::

     include other.conf
     # Include *.conf files from all subdirs of shitty.d inside the shitty config dir
     globinclude shitty.d/**/*.conf
     # Include the *contents* of all env vars starting with shitty_CONF_
     envinclude shitty_CONF_*


.. note:: Syntax highlighting for :file:`shitty.conf` in vim is available via
   `vim-shitty <https://github.com/fladson/vim-shitty>`__.


.. include:: /generated/conf-shitty.rst


Sample shitty.conf
--------------------

.. only:: html

    You can download a sample :file:`shitty.conf` file with all default settings
    and comments describing each setting by clicking: :download:`sample
    shitty.conf </generated/conf/shitty.conf>`.

.. only:: man

   You can edit a fully commented sample shitty.conf by pressing the
   :sc:`edit_config_file` shortcut in shitty. This will generate a config file
   with full documentation and all settings commented out. If you have a
   pre-existing :file:`shitty.conf`, then that will be used instead, delete it to
   see the sample file.


All mappable actions
------------------------

See the :doc:`list of all the things you can make shitty can do </actions>`.

.. toctree::
   :hidden:

   actions
