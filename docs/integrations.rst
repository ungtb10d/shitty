:tocdepth: 2

Integrations with other tools
================================

shitty provides extremely powerful interfaces such as :doc:`remote-control` and
:doc:`shittens/custom` and :doc:`shittens/icat` that allow it to be integrated
with other tools seamlessly.


Image and document viewers
----------------------------

Powered by shitty's :doc:`graphics-protocol` there exist many tools for viewing
images and other types of documents directly in your terminal, even over SSH.

.. _tool_termpdf:

`termpdf.py <https://github.com/dsanson/termpdf.py>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A terminal PDF/DJVU/CBR viewer

.. _tool_mdcat:

`mdcat <https://github.com/lunaryorn/mdcat>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Display markdown files nicely formatted with images in the terminal

.. _tool_ranger:

`ranger <https://github.com/ranger/ranger>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A terminal file manager, with previews of file contents powered by shitty's
graphics protocol.

.. _tool_nnn:

`nnn <https://github.com/jarun/nnn/>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Another terminal file manager, with previews of file contents powered by shitty's
graphics protocol.

.. _tool_hunter:

`hunter <https://github.com/rabite0/hunter>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Another terminal file manager, with previews of file contents powered by shitty's
graphics protocol.

.. _tool_term_image:

`term-image <https://github.com/AnonymouX47/term-image>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Tool to browse images in a terminal using shitty's graphics protocol.

.. _tool_koneko:

`koneko <https://github.com/twenty5151/koneko>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Browse images from the pixiv artist community directly in shitty.

.. _tool_viu:

`viu <https://github.com/atanunq/viu>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
View images in the terminal, similar to shitty's icat.

.. _tool_nb:


`nb <https://github.com/xwmx/nb>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Command line and local web note-taking, bookmarking, archiving, and knowledge
base application that uses shitty's graphics protocol for images.

.. _tool_w3m:

`w3m <https://github.com/tats/w3m>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A text mode WWW browser that supports shitty's graphics protocol to display
images.

.. _tool_timg:

`timg <https://github.com/hzeller/timg>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A terminal image and video viewer, that displays static and animated images or
plays videos. Fast multi-threaded loading, JPEG exif rotation, grid view and
connecting to the webcam make it a versatile terminal utility.


System and data visualisation tools
---------------------------------------

.. _tool_neofetch:

`neofetch <https://github.com/dylanaraps/neofetch>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A command line system information tool that shows images using shitty's graphics
protocol

.. _tool_matplotlib:

`matplotlib <https://github.com/jktr/matplotlib-backend-shitty>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Show matplotlib plots directly in shitty

.. _tool_shittyTerminalImage:

`shittyTerminalImages.jl <https://github.com/simonschoelly/shittyTerminalImages.jl>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Show images from Julia directly in shitty

.. _tool_euporie:

`euporie <https://github.com/joouha/euporie>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A text-based user interface for running and editing Jupyter notebooks, powered
by shitty's graphics protocol for displaying plots

.. _tool_gnuplot:

`gnuplot <http://www.gnuplot.info/>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A graphing and data visualization tool that can be made to display its output in
shitty with the following bash snippet:

.. code-block:: sh

    function iplot {
        cat <<EOF | gnuplot
        set terminal pngcairo enhanced font 'Fira Sans,10'
        set autoscale
        set samples 1000
        set output '|shitty +shitten icat --stdin yes'
        set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#fdf6e3" behind
        plot $@
        set output '/dev/null'
        EOF
    }

Add this to bashrc and then to plot a function, simply do:

.. code-block:: sh

    iplot 'sin(x*3)*exp(x*.2)'

.. tool_onefetch:

`onefetch <https://github.com/o2sh/onefetch>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A tool to fetch information about your git repositories

.. tool_patat:

`patat <https://github.com/jaspervdj/patat>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Terminal based presentations using pandoc and shitty's image protocol for
images

.. tool_wttr:

`wttr.in <https://github.com/chubin/wttr.in>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A tool to display weather information in your terminal with curl

.. tool_wl_clipboard:

`wl-clipboard-manager <https://github.com/maximbaz/wl-clipboard-manager>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
View and manage the system clipboard under Wayland in your shitty terminal

.. tool_dmenu_term:

`dmenu-term <https://github.com/maximbaz/dmenu-term>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run applications on your system with fuzzy find inside a shitty window


Editor integration
-----------------------

|shitty| can be integrated into many different terminal based text editors to add
features such a split windows, previews, REPLs etc.

.. tool_kakoune:

`kakoune <https://kakoune.org/>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Integrates with shitty to use native shitty windows for its windows/panels and
REPLs.

.. tool_vim_slime:

`vim-slime <https://github.com/jpalardy/vim-slime#shitty>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Uses shitty remote control for a Lisp REPL.

.. tool_vim_shitty_navigator:

`vim-shitty-navigator <https://github.com/knubie/vim-shitty-navigator>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Allows you to navigate seamlessly between vim and shitty splits using a
consistent set of hotkeys.

.. tool_vim_test:

`vim-test <https://github.com/vim-test/vim-test>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Allows easily running tests in a terminal window

.. tool_hologram:

`hologram.nvim <https://github.com/edluffy/hologram.nvim>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Terminal image viewer for Neovim


Scrollback manipulation
-------------------------

.. tool_shitty_search:

`shitty-search <https://github.com/trygveaa/shitty-shitten-search>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Live incremental search of the scrollback buffer.

.. tool_shitty_grab:

`shitty-grab <https://github.com/yurikhan/shitty_grab>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Keyboard based text selection for the shitty scrollback buffer.


Miscellaneous
------------------

.. tool_shitty_smart_tab:

`shitty-smart-tab <https://github.com/yurikhan/shitty-smart-tab>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use keys to either control tabs or pass them onto running applications if no
tabs are present

.. tool_shitty_smart_scroll:

`shitty-smart-scroll <https://github.com/yurikhan/shitty-smart-scroll>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use keys to either scroll or pass them onto running applications if no
scrollback buffer is present

.. tool_kitti3:

`kitti3 <https://github.com/LandingEllipse/kitti3>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Allow using shitty as a drop-down terminal under the i3 window manager

.. tool_weechat_hints:

`weechat-hints <https://github.com/GermainZ/shitty-weechat-hints>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
URL hints shitten for WeeChat that works without having to use WeeChat's
raw-mode.

.. tool_glshitty:

`glshitty <https://github.com/michaeljclark/glshitty>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C library to draw OpenGL shaders in the terminal with a glgears demo
