Integrations with other tools
================================

shitty provides extremely powerful interfaces such as :doc:`remote-control` and
:doc:`shittens/custom` and :doc:`shittens/icat`
that allow it to be integrated with other tools seamlessly.


Image and document viewers
----------------------------

Powered by shitty's :doc:`graphics-protocol` there exist many tools for viewing
images and other types of documents directly in your terminal, even over SSH.

`termpdf.py <https://github.com/dsanson/termpdf.py>`_
    a terminal PDF/DJVU/CBR viewer

`mdcat <https://github.com/lunaryorn/mdcat>`_
    Display markdown files nicely formatted with images in the terminal

`ranger <https://github.com/ranger/ranger>`_
    a terminal file manager, with previews of file contents powered by shitty's graphics protocol.

`nnn <https://github.com/jarun/nnn/>`_
    another terminal file manager, with previews of file contents powered by shitty's graphics protocol.

`hunter <https://github.com/rabite0/hunter>`_
    another terminal file manager, with previews of file contents powered by shitty's graphics protocol.

`koneko <https://github.com/twenty5151/koneko>`_
    browse images from the pixiv artist community directly in shitty.

`viu <https://github.com/atanunq/viu>`_
    view images in the terminal, similar to shitty's icat.

`nb <https://github.com/xwmx/nb>`_
    command line and local web note-taking, bookmarking, archiving, and
    knowledge base application that uses shitty's graphics protocol for images.

`w3m <https://github.com/tats/w3m>`_
    A text mode WWW browser that supports shitty's graphics protocol to display
    images.

`timg <https://github.com/hzeller/timg>`_
    A terminal image and video viewer, that displays static and animated
    images or plays videos. Fast multi-threaded loading, JPEG exif rotation,
    grid view and connecting to the webcam make it a versatile terminal utility.


System and data visualisation tools
---------------------------------------

`neofetch <https://github.com/dylanaraps/neofetch>`_
    A command line system information tool that shows images using shitty's graphics protocol

`matplotlib <https://github.com/jktr/matplotlib-backend-shitty>`_
    show matplotlib plots directly in shitty

`shittyTerminalImages.jl <https://github.com/simonschoelly/shittyTerminalImages.jl>`_
    show images from Julia directly in shitty

`euporie <https://github.com/joouha/euporie>`_
    a text-based user interface for running and editing Jupyter notebooks,
    powered by shitty's graphics protocol for displaying plots

`gnuplot <http://www.gnuplot.info/>`_
    a graphing and data visualization tool that can be made to display its
    output in shitty with the following bash snippet::

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

   Add this to bashrc and then to plot a function, simply do::

        iplot 'sin(x*3)*exp(x*.2)'

`onefetch <https://github.com/o2sh/onefetch>`_
    a tool to fetch information about your git repositories

`patat <https://github.com/jaspervdj/patat>`_
    terminal based presentations using pandoc and shitty's image protocol for
    images

`wttr.in <https://github.com/chubin/wttr.in>`_
    a tool to display weather information in your terminal with curl

`wl-clipboard-manager <https://github.com/maximbaz/wl-clipboard-manager>`_
    view and manage the system clipboard under Wayland in your shitty terminal

`dmenu-term <https://github.com/maximbaz/dmenu-term>`_
    run applications on your system with fuzzy find inside a shitty window


Editor integration
-----------------------

shitty can be integrated into many different terminal editors to add features
such a split windows, previews, REPLs etc.


`kakoune <https://kakoune.org/>`_
    integrates with shitty to use native shitty windows for its windows/panels and REPLs.

`vim-slime <https://github.com/jpalardy/vim-slime#shitty>`_
    uses shitty remote control for a Lisp REPL.

`vim-shitty-navigator <https://github.com/knubie/vim-shitty-navigator>`_
    allows you to navigate seamlessly between vim and shitty splits using a consistent set of hotkeys.

`vim-test <https://github.com/vim-test/vim-test>`_
    allows easily running tests in a terminal window

`hologram.nvim <https://github.com/edluffy/hologram.nvim>`_
    terminal image viewer for nvim


Scrollback manipulation
-------------------------

`shitty-search <https://github.com/trygveaa/shitty-shitten-search>`_
    Live incremental search of the scrollback buffer.

`shitty-grab <https://github.com/yurikhan/shitty_grab>`_
    keyboard based text selection for the shitty scrollback buffer.



Miscellaneous
------------------

`shitty-smart-tab <https://github.com/yurikhan/shitty-smart-tab>`_
    use keys to either control tabs or pass them onto running applications if
    no tabs are present

`shitty-smart-scroll <https://github.com/yurikhan/shitty-smart-scroll>`_
    use keys to either scroll or pass them onto running applications if
    no scrollback buffer is present

`reload keybindings <https://github.com/ungtb10d/shitty/issues/1292#issuecomment-582388769>`_
    reload key bindings from :file:`shitty.conf` without needing to restart
    shitty

`kitti3 <https://github.com/LandingEllipse/kitti3>`_
    allow using shitty as a drop-down terminal under the i3 window manager

`weechat-hints <https://github.com/GermainZ/shitty-weechat-hints>`_
    URL hints shitten for WeeChat that works without having to use WeeChat's
    raw-mode.

`glshitty <https://github.com/michaeljclark/glshitty>`_
    C library to draw OpenGL shaders in the terminal with a glgears demo
