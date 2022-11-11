Changelog
==============

|shitty| is a feature-rich, cross-platform, *fast*, GPU based terminal.
To update |shitty|, :doc:`follow the instructions <binary>`.

0.21.2 [2021-06-28]
----------------------

- A new :opt:`adjust_baseline` option to adjust the vertical alignment of text
  inside a line (:pull:`3734`)

- A new :opt:`url_excluded_characters` option to exclude additional characters
  when detecting URLs under the mouse (:pull:`3738`)

- Fix a regression in 0.21.0 that broke rendering of private use Unicode symbols followed
  by spaces, when they also exist not followed by spaces (:iss:`3729`)

- ssh shitten: Support systems where the login shell is a non-POSIX shell
  (:iss:`3405`)

- ssh shitten: Add completion (:iss:`3760`)

- ssh shitten: Fix "Connection closed" message being printed by ssh when running
  remote commands

- Add support for the XTVERSION escape code

- macOS: Fix a regression in 0.21.0 that broke middle-click to paste from clipboard (:iss:`3730`)

- macOS: Fix shortcuts in the global menu bar responding slowly when cursor blink
  is disabled/timed out (:iss:`3693`)

- When displaying scrollback ensure that the window does not quit if the amount
  of scrollback is less than a screen and the user has the ``--quit-if-one-screen``
  option enabled for less (:iss:`3740`)

- Linux: Fix Emoji/bitmapped fonts not use able in symbol_map

- query terminal shitten: Allow querying font face and size information
  (:iss:`3756`)

- hyperlinked grep shitten: Fix context options not generating contextual output (:iss:`3759`)

- Allow using superscripts in tab titles (:iss:`3763`)

- Unicode input shitten: Fix searching when a word has more than 1024 matches (:iss:`3773`)


0.21.1 [2021-06-14]
----------------------

- macOS: Fix a regression in the previous release that broke rendering of
  strikeout (:iss:`3717`)

- macOS: Fix a crash when rendering ligatures larger than 128 characters
  (:iss:`3724`)

- Fix a regression in the previous release that could cause a crash when
  changing layouts and mousing (:iss:`3713`)


0.21.0 [2021-06-12]
----------------------

- Allow reloading the :file:`shitty.conf` config file by pressing
  :sc:`reload_config_file`. (:iss:`1292`)

- Allow clicking URLs to open them without needing to also hold
  :kbd:`ctrl+shift`

- Allow remapping all mouse button press/release events to perform arbitrary
  actions. :ref:`See details <conf-shitty-mouse.mousemap>` (:iss:`1033`)

- Support infinite length ligatures (:iss:`3504`)

- **Backward incompatibility**: The options to control which modifiers keys to
  press for various mouse actions have been removed, if you used these options,
  you will need to replace them with configuration using the new
  :ref:`mouse actions framework <conf-shitty-mouse.mousemap>` as they will be
  ignored. The options were: ``terminal_select_modifiers``,
  ``rectangle_select_modifiers`` and ``open_url_modifiers``.

- Add a configurable mouse action (:kbd:`ctrl+alt+triplepress` to select from the
  clicked point to the end of the line. (:iss:`3585`)

- Add the ability to un-scroll the screen to the ``shitty @ scroll-window``
  remote control command (:iss:`3604`)

- A new option, :opt:`tab_bar_margin_height` to add margins around the
  top and bottom edges of the tab bar (:iss:`3247`)

- Unicode input shitten: Fix a regression in 0.20.0 that broke keyboard handling
  when the NumLock or CapsLock modifiers were engaged. (:iss:`3587`)

- Fix a regression in 0.20.0 that sent incorrect bytes for the :kbd:`F1-F4` keys
  in rmkx mode (:iss:`3586`)

- macOS: When the Apple Color Emoji font lacks an emoji glyph search for it in other
  installed fonts (:iss:`3591`)

- macOS: Fix rendering getting stuck on some machines after sleep/screensaver
  (:iss:`2016`)

- macOS: Add a new ``Shell`` menu to the global menubar with some commonly used
  actions (:pull:`3653`)

- macOS: Fix the baseline for text not matching other CoreText based
  applications for some fonts (:iss:`2022`)

- Add a few more special commandline arguments for the launch command. Now all
  ``shitty_PIPE_DATA`` is also available via command line argument substitution
  (:iss:`3593`)

- Fix dynamically changing the background color in a window causing rendering
  artifacts in the tab bar (:iss:`3595`)

- Fix passing STDIN to launched background processes causing them to not inherit
  environment variables (:pull:`3603`)

- Fix deleting windows that are not the last window via remote control leaving
  no window focused (:iss:`3619`)

- Add an option :option:`shitty @ get-text --add-cursor` to also get the current
  cursor position and state as ANSI escape codes (:iss:`3625`)

- Add an option :option:`shitty @ get-text --add-wrap-markers` to add line wrap
  markers to the output (:pull:`3633`)

- Improve rendering of curly underlines on HiDPI screens (:pull:`3637`)

- ssh shitten: Mimic behavior of ssh command line client more closely by
  executing any command specified on the command line via the users' shell
  just as ssh does (:iss:`3638`)

- Fix trailing parentheses in URLs not being detected (:iss:`3688`)

- Tab bar: Use a lower contrast color for tab separators (:pull:`3666`)

- Fix a regression that caused using the ``title`` command in session files
  to stop working (:iss:`3676`)

- macOS: Fix a rare crash on exit (:iss:`3686`)

- Fix ligatures not working with the `Iosevka
  <https://github.com/be5invis/Iosevka>`_ font (requires Iosevka >= 7.0.4)
  (:iss:`297`)

- Remote control: Allow matching tabs by index number in currently active OS
  Window (:iss:`3708`)

- ssh shitten: Fix non-standard properties in terminfo such as the ones used for
  true color not being copied (:iss:`312`)


0.20.3 [2021-05-06]
----------------------

- macOS: Distribute universal binaries with both ARM and Intel architectures

- A new ``show_key`` shitten to easily see the bytes generated by the terminal
  for key presses in the various keyboard modes (:pull:`3556`)

- Linux: Fix keyboard layout change keys defined via compose rules not being
  ignored

- macOS: Fix Spotlight search of global menu not working in non-English locales
  (:pull:`3567`)

- Fix tab activity symbol not appearing if no other changes happen in tab bar even when
  there is activity in a tab (:iss:`3571`)

- Fix focus changes not being sent to windows when focused window changes
  because of the previously focused window being closed (:iss:`3571`)


0.20.2 [2021-04-28]
----------------------

- A new protocol extension to :ref:`unscroll <unscroll>` text from the
  scrollback buffer onto the screen. Useful, for example, to restore
  the screen after showing completions below the shell prompt.

- A new remote control command :ref:`at_env` to change the default
  environment passed to newly created windows (:iss:`3529`)

- Linux: Fix binary shitty builds not able to load fonts in WOFF2 format
  (:iss:`3506`)

- macOS: Prevent :kbd:`option` based shortcuts for being used for global menu
  actions (:iss:`3515`)

- Fix ``shitty @ close-tab`` not working with pipe based remote control
  (:iss:`3510`)

- Fix removal of inactive tab that is before the currently active tab causing
  the highlighted tab to be incorrect (:iss:`3516`)

- icat shitten: Respect EXIF orientation when displaying JPEG images
  (:iss:`3518`)

- GNOME: Fix maximize state not being remembered when focus changes and window
  decorations are hidden (:iss:`3507`)

- GNOME: Add a new :opt:`wayland_titlebar_color` option to control the color of the
  shitty window title bar

- Fix reading :option:`shitty --session` from ``STDIN`` not working when the
  :option:`shitty --detach` option is used (:iss:`3523`)

- Special case rendering of the few remaining Powerline box drawing chars
  (:iss:`3535`)

- Fix ``shitty @ set-colors`` not working for the :opt:`active_tab_foreground`.


0.20.1 [2021-04-19]
----------------------

- icat: Fix some broken GIF images with no frame delays not being animated
  (:iss:`3498`)

- hints shitten: Fix sending hyperlinks to their default handler not working
  (:pull:`3500`)

- Wayland: Fix regression in previous release causing window decorations to
  be drawn even when compositor supports server side decorations (:iss:`3501`)


0.20.0 [2021-04-19]
----------------------

- Support display of animated images ``shitty +shitten icat animation.gif``. See
  :ref:`animation_protocol` for details on animation support in the shitty
  graphics protocol.

- A new keyboard reporting protocol with various advanced features that can be
  used by full screen terminal programs and even games, see
  :doc:`keyboard-protocol` (:iss:`3248`)

- **Backward incompatibility**: Session files now use the full :doc:`launch <launch>`
  command with all its capabilities. However, the syntax of the command is
  slightly different from before. In particular watchers are now specified
  directly on launch and environment variables are set using ``--env``.

- Allow setting colors when creating windows using the :doc:`launch <launch>` command.

- A new option :opt:`tab_powerline_style` to control the appearance of the tab
  bar when using the powerline tab bar style.

- A new option :opt:`scrollback_fill_enlarged_window` to fill extra lines in
  the window when the window is expanded with lines from the scrollback
  (:pull:`3371`)

- diff shitten: Implement recursive diff over SSH (:iss:`3268`)

- ssh shitten: Allow using python instead of the shell on the server, useful if
  the shell used is a non-POSIX compliant one, such as fish (:iss:`3277`)

- Add support for the color settings stack that XTerm copied from us without
  acknowledgement and decided to use incompatible escape codes for.

- Add entries to the terminfo file for some user capabilities that are shared
  with XTerm (:pull:`3193`)

- The launch command now does more sophisticated resolving of executables to
  run. The system-wide PATH is used first, then system specific default paths,
  and finally the PATH inside the shell.

- Double clicking on empty tab bar area now opens a new tab (:iss:`3201`)

- shitty @ ls: Show only environment variables that are different for each
  window, by default.

- When passing a directory or a non-executable file as the program to run to
  shitty opens it with the shell or by parsing the shebang, instead of just failing.

- Linux: Fix rendering of emoji followed by the graphics variation selector not
  being colored with some fonts (:iss:`3211`)

- Unicode input: Fix using index in select by name mode not working for indices
  larger than 16. Also using an index does not filter the list of matches. (:pull:`3219`)

- Wayland: Add support for the text input protocol (:iss:`3410`)

- Wayland: Fix mouse handling when using client side decorations

- Wayland: Fix un-maximizing a window not restoring its size to what it was
  before being maximized

- GNOME/Wayland: Improve window decorations the titlebar now shows the window
  title. Allow running under Wayland on GNOME by default. (:iss:`3284`)

- Panel shitten: Allow setting WM_CLASS (:iss:`3233`)

- macOS: Add menu items to close the OS window and the current tab (:pull:`3240`, :iss:`3246`)

- macOS: Allow opening script and command files with shitty (:iss:`3366`)

- Also detect ``gemini://`` URLs when hovering with the mouse (:iss:`3370`)

- When using a non-US keyboard layout and pressing :kbd:`ctrl+key` when
  the key matches an English key, send that to the program running in the
  terminal automatically (:iss:`2000`)

- When matching shortcuts, also match on shifted keys, so a shortcut defined as
  :kbd:`ctrl+plus` will match a keyboard where you have to press
  :kbd:`shift+equal` to get the plus key (:iss:`2000`)

- Fix extra space at bottom of OS window when using the fat layout with the tab bar at the
  top (:iss:`3258`)

- Fix window icon not working on X11 with 64bits (:iss:`3260`)

- Fix OS window sizes under 100px resulting in scaled display (:iss:`3307`)

- Fix rendering of ligatures in the latest release of Cascadia code, which for
  some reason puts empty glyphs after the ligature glyph rather than before it
  (:iss:`3313`)

- Improve handling of infinite length ligatures in newer versions of FiraCode
  and CascadiaCode. Now such ligatures are detected based on glyph naming
  convention. This removes the gap in the ligatures at cell boundaries (:iss:`2695`)

- macOS: Disable the native operating system tabs as they are non-functional
  and can be confusing (:iss:`3325`)

- hints shitten: When using the linenumber action with a background action,
  preserve the working directory (:iss:`3352`)

- Graphics protocol: Fix suppression of responses not working for chunked
  transmission (:iss:`3375`)

- Fix inactive tab closing causing active tab to change (:iss:`3398`)

- Fix a crash on systems using musl as libc (:iss:`3395`)

- Improve rendering of rounded corners by using a rectircle equation rather
  than a cubic bezier (:iss:`3409`)

- Graphics protocol: Add a control to allow clients to specify that the cursor
  should not move when displaying an image (:iss:`3411`)

- Fix marking of text not working on lines that contain zero cells
  (:iss:`3403`)

- Fix the selection getting changed if the screen contents scroll while
  the selection is in progress (:iss:`3431`)

- X11: Fix :opt:`resize_in_steps` being applied even when window is maximized
  (:iss:`3473`)


0.19.3 [2020-12-19]
-------------------

- Happy holidays to all shitty users!

- A new :doc:`broadcast <shittens/broadcast>` shitten to type in all shitty windows
  simultaneously (:iss:`1569`)

- Add a new mappable `select_tab` action to choose a tab to switch to even
  when the tab bar is hidden (:iss:`3115`)

- Allow specifying text formatting in :opt:`tab_title_template` (:iss:`3146`)

- Linux: Read :opt:`font_features` from the FontConfig database as well, so
  that they can be configured in a single, central location (:pull:`3174`)

- Graphics protocol: Add support for giving individual image placements their
  own ids and for asking the terminal emulator to assign ids for images. Also
  allow suppressing responses from the terminal to commands.
  These are backwards compatible protocol extensions. (:iss:`3133`,
  :iss:`3163`)

- Distribute extra pixels among all eight-blocks rather than adding them
  all to the last block (:iss:`3097`)

- Fix drawing of a few sextant characters incorrect (:pull:`3105`)

- macOS: Fix minimize not working for chromeless windows (:iss:`3112`)

- Preserve lines in the scrollback if a scrolling region is defined that
  is contiguous with the top of the screen (:iss:`3113`)

- Wayland: Fix key repeat being stopped by the release of an unrelated key
  (:iss:`2191`)

- Add an option, :opt:`detect_urls` to control whether shitty will detect URLs
  when the mouse moves over them (:pull:`3118`)

- Graphics protocol: Dont return filename in the error message when opening file
  fails, since filenames can contain control characters (:iss:`3128`)

- macOS: Partial fix for traditional fullscreen not working on Big Sur
  (:iss:`3100`)

- Fix one ANSI formatting escape code not being removed from the pager history
  buffer when piping it as plain text (:iss:`3132`)

- Match the save/restore cursor behavior of other terminals, for the sake of
  interoperability. This means that doing a DECRC without a prior DECSC is now
  undefined (:iss:`1264`)

- Fix mapping ``remote_control send-text`` not working (:iss:`3147`)

- Add a ``right`` option for :opt:`tab_switch_strategy` (:pull:`3155`)

- Fix a regression in 0.19.0 that caused a rare crash when using the optional
  :opt:`scrollback_pager_history_size` (:iss:`3049`)

- Full screen shittens: Fix incorrect cursor position after shitten quits
  (:iss:`3176`)


0.19.2 [2020-11-13]
-------------------

- A new :doc:`shittens/query_terminal` shitten to easily query the running shitty
  via escape codes to detect its version, and the values of
  configuration options that enable or disable terminal features.

- Options to control mouse pointer shape, :opt:`default_pointer_shape`, and
  :opt:`pointer_shape_when_dragging` (:pull:`3041`)

- Font independent rendering for braille characters, which ensures they are properly
  aligned at all font sizes.

- Fix a regression in 0.19.0 that caused borders not to be drawn when setting
  :opt:`window_margin_width` and keeping :opt:`draw_minimal_borders` on
  (:iss:`3017`)

- Fix a regression in 0.19.0 that broke rendering of one-eight bar unicode
  characters at very small font sizes (:iss:`3025`)

- Wayland: Fix a crash under GNOME when using multiple OS windows
  (:pull:`3066`)

- Fix selections created by dragging upwards not being auto-cleared when
  screen contents change (:pull:`3028`)

- macOS: Fix shitty not being added to PATH automatically when using pre-built
  binaries (:iss:`3063`)

- Allow adding MIME definitions to shitty by placing a ``mime.types`` file in
  the shitty config directory (:iss:`3056`)

- Dont ignore :option:`--title` when using a session file that defines no
  windows (:iss:`3055`)

- Fix the send_text action not working in URL handlers (:iss:`3081`)

- Fix last character of URL not being detected if it is the only character on a
  new line (:iss:`3088`)

- Don't restrict the ICH,DCH,REP control codes to only the current scroll region  (:iss:`3090`, :iss:`3096`)


0.19.1 [2020-10-06]
-------------------

- hints shitten: Add an ``ip`` type for easy selection of IP addresses
  (:pull:`3009`)

- Fix a regression that caused a segfault when using
  :opt:`scrollback_pager_history_size` and it needs to be expanded (:iss:`3011`)

- Fix update available notifications repeating (:pull:`3006`)


0.19.0 [2020-10-04]
-------------------

- Add support for `hyperlinks from terminal programs
  <https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda>`_.
  Controlled via :opt:`allow_hyperlinks` (:iss:`68`)

- Add support for easily editing or downloading files over SSH sessions
  without the need for any special software, see :doc:`shittens/remote_file`

- A new :doc:`shittens/hyperlinked_grep` shitten to easily search files and open
  the results at the matched line by clicking on them.

- Allow customizing the :doc:`actions shitty takes <open_actions>` when clicking on URLs

- Improve rendering of borders when using minimal borders. Use less space and
  do not display a box around active windows

- Add a new extensible escape code to allow terminal programs to trigger
  desktop notifications. See :ref:`desktop_notifications` (:iss:`1474`)

- Implement special rendering for various characters from the set of "Symbols
  for Legacy Computing" from the Unicode 13 standard

- Unicode input shitten: Allow choosing symbols from the NERD font as well.
  These are mostly Private Use symbols not in any standard, however are common. (:iss:`2972`)

- Allow specifying border sizes in either pts or pixels. Change the default to
  0.5pt borders as this works best with the new minimal border style

- Add support for displaying correct colors with non-sRGB PNG files (Adds a
  dependency on liblcms2)

- hints shitten: Add a new :option:`shitty +shitten hints --type` of ``hyperlink`` useful
  for activating hyperlinks using just the keyboard

- Allow tracking focus change events in watchers (:iss:`2918`)

- Allow specifying watchers in session files and via a command line argument
  (:iss:`2933`)

- Add a setting :opt:`tab_activity_symbol` to show a symbol in the tab title
  if one of the windows has some activity after it was last focused
  (:iss:`2515`)

- macOS: Switch to using the User Notifications framework for notifications.
  The current notifications framework has been deprecated in Big Sur. The new
  framework only allows notifications from signed and notarized applications,
  so people using shitty from homebrew/source are out of luck. Complain to
  Apple.

- When in the main screen and a program grabs the mouse, do not use the scroll
  wheel events to scroll the scrollback buffer, instead send them to the
  program (:iss:`2939`)

- Fix unfocused windows in which a bell occurs not changing their border color
  to red until a relayout

- Linux: Fix automatic detection of bold/italic faces for fonts such as IBM
  Plex Mono that have the regular face with a full name that is the same as the
  family name (:iss:`2951`)

- Fix a regression that broke :opt:`shitten_alias` (:iss:`2952`)

- Fix a regression that broke the ``move_window_to_top`` action (:pull:`2953`)

- Fix a memory leak when changing font sizes

- Fix some lines in the scrollback buffer not being properly rendered after a
  window resize/font size change (:iss:`2619`)


0.18.3 [2020-08-11]
-------------------

- hints shitten: Allow customizing hint colors (:pull:`2894`)

- Wayland: Fix a typo in the previous release that broke reading mouse cursor size (:iss:`2895`)

- Fix a regression in the previous release that could cause an exception during
  startup in rare circumstances (:iss:`2896`)

- Fix image leaving behind a black rectangle when switch away and back to
  alternate screen (:iss:`2901`)

- Fix one pixel mis-alignment of rounded corners when either the cell
  dimensions or the thickness of the line is an odd number of pixels
  (:iss:`2907`)

- Fix a regression that broke specifying OS window size in the session file
  (:iss:`2908`)


0.18.2 [2020-07-28]
--------------------

- X11: Improve handling of multiple keyboards. Now pressing a modifier key in
  one keyboard and a normal key in another works (:iss:`2362`). Don't rebuild
  keymaps on new keyboard events that only change geometry (:iss:`2787`).
  Better handling of multiple keyboards with incompatible layouts (:iss:`2726`)

- Improve anti-aliasing of triangular box drawing characters, noticeable on
  low-resolution screens (:iss:`2844`)

- Fix ``shitty @ send-text`` not working reliably when using a socket for remote
  control (:iss:`2852`)

- Implement support for box drawing rounded-corners characters (:iss:`2240`)

- Allow setting the class for new OS windows in a session file

- When a character from the Unicode Dingbat block is followed by a space, use
  the extra space to render a larger version of the character (:iss:`2850`)

- macOS: Fix the LC_CTYPE env var being set to UTF-8 on systems in which the
  language and country code do not form a valid locale (:iss:`1233`)

- macOS: Fix :kbd:`cmd+plus` not changing font size (:iss:`2839`)

- Make neighboring window selection in grid and splits layouts more intelligent
  (:pull:`2840`)

- Allow passing the current selection to shittens (:iss:`2796`)

- Fix pre-edit text not always being cleared with ibus input (:iss:`2862`)

- Allow setting the :opt:`background_opacity` of new OS windows created via
  :option:`shitty --single-instance` using the :option:`shitty --override` command line
  argument (:iss:`2806`)

- Fix the CSI J (Erase in display ED) escape code not removing line continued
  markers (:iss:`2809`)

- hints shitten: In linenumber mode expand paths that starts with ~
  (:iss:`2822`)

- Fix ``launch --location=last`` not working (:iss:`2841`)

- Fix incorrect centering when a PUA or symbol glyph is followed by more than one space

- Have the :opt:`confirm_os_window_close` option also apply when closing tabs
  with multiple windows (:iss:`2857`)

- Add support for legacy DECSET codes 47, 1047 and 1048 (:pull:`2871`)

- macOS: no longer render emoji 20% below the baseline. This caused some emoji
  to be cut-off and also look misaligned with very high cells (:iss:`2873`)

- macOS: Make the window id of OS windows available in the ``WINDOWID``
  environment variable (:pull:`2877`)

- Wayland: Fix a regression in 0.18.0 that could cause crashes related to mouse
  cursors in some rare circumstances (:iss:`2810`)

- Fix change in window size that does not change number of cells not being
  reported to the kernel (:iss:`2880`)


0.18.1 [2020-06-23]
--------------------

- macOS: Fix for diff shitten not working with python 3.8 (:iss:`2780`)


0.18.0 [2020-06-20]
--------------------

- Allow multiple overlay windows per normal window

- Add an option :opt:`confirm_os_window_close` to ask for confirmation
  when closing an OS window with multiple shitty windows.

- Tall and Fat layouts: Add a ``mirrored`` option to put the full size window
  on the opposite edge of the screen (:iss:`2654`)

- Tall and Fat layouts: Add mappable actions to increase or decrease the number
  of full size windows (:iss:`2688`)

- Allow sending arbitrary signals to the current foreground process in a window
  using either a mapping in shitty.conf or via remote control (:iss:`2778`)

- Allow sending the back and forward mouse buttons to terminal applications
  (:pull:`2742`)

- **Backwards incompatibility**: The numbers used to encode mouse buttons
  for the ``send_mouse_event`` function that can be used in shittens have
  been changed (see :ref:`send_mouse_event`).

- Add a new mappable ``quit`` action to quit shitty completely.

- Fix marks using different colors with regexes using only a single color
  (:pull:`2663`)

- Linux: Workaround for broken Nvidia drivers for old cards (:iss:`456`)

- Wayland: Fix shitty being killed on some Wayland compositors if a hidden window
  has a lot of output (:iss:`2329`)

- BSD: Fix controlling terminal not being established (:pull:`2686`)

- Add support for the CSI REP escape code (:pull:`2702`)

- Wayland: Fix mouse cursor rendering on HiDPI screens (:pull:`2709`)

- X11: Recompile keymaps on XkbNewKeyboardNotify events (:iss:`2726`)

- X11: Reduce startup time by ~25% by only querying GLX for framebuffer
  configurations once (:iss:`2754`)

- macOS: Notarize the shitty application bundle (:iss:`2040`)

- Fix the shitty shell launched via a mapping needlessly requiring
  :opt:`allow_remote_control` to be turned on.


0.17.4 [2020-05-09]
--------------------

- Allow showing the name of the current layout and the number of windows
  in tab titles (:iss:`2634`)

- macOS: Fix a regression in the previous release that caused ligatures to be
  not be centered horizontally (:iss:`2591`)

- By default, double clicking no longer considers the : as part of words, see
  :opt:`select_by_word_characters` (:iss:`2602`)

- Fix a regression that caused clicking in the padding/margins of windows in
  the stack layout to switch the window to the first window (:iss:`2604`)

- macOS: Fix a regression that broke drag and drop (:iss:`2605`)

- Report modifier key state when sending wheel events to the terminal program

- Fix shitty @ send-text not working with text larger than 1024 bytes when using
  :option:`shitty --listen-on` (:iss:`2607`)

- Wayland: Fix OS window title not updating for hidden windows (:iss:`2629`)

- Fix :opt:`background_tint` making the window semi-transparent (:iss:`2618`)


0.17.3 [2020-04-23]
--------------------

- Allow individually setting margins and padding for each edge (left, right,
  top, bottom). Margins can also be controlled per window via remote control
  (:iss:`2546`)

- Fix reverse video not being rendered correctly when using transparency or a
  background image (:iss:`2419`)

- Allow mapping arbitrary remote control commands to key presses in
  :file:`shitty.conf`

- X11: Fix crash when doing drag and drop from some applications (:iss:`2505`)

- Fix :option:`launch --stdin-add-formatting` not working (:iss:`2512`)

- Update to Unicode 13.0 (:iss:`2513`)

- Render country flags designated by a pair of unicode codepoints
  in two cells instead of four.

- diff shitten: New option to control the background color for filler lines in
  the margin (:iss:`2518`)

- Fix specifying options for layouts in the startup session file not working
  (:iss:`2520`)

- macOS: Fix incorrect horizontal positioning of some full-width East Asian characters
  (:iss:`1457`)

- macOS: Render multi-cell PUA characters centered, matching behavior on other
  platforms

- Linux: Ignore keys if they are designated as layout/group/mode switch keys
  (:iss:`2519`)

- Marks: Fix marks not handling wide characters and tab characters correctly
  (:iss:`2534`)

- Add a new :opt:`listen_on` option in shitty.conf to set :option:`shitty --listen-on`
  globally. Also allow using environment variables in this option (:iss:`2569`).

- Allow sending mouse events in shittens (:pull:`2538`)

- icat shitten: Fix display of 16-bit depth images (:iss:`2542`)

- Add ncurses specific terminfo definitions for strikethrough (:pull:`2567`)

- Fix a regression in 0.17 that broke displaying graphics over SSH
  (:iss:`2568`)

- Fix :option:`--title` not being applied at window creation time (:iss:`2570`)

0.17.2 [2020-03-29]
--------------------

- Add a :option:`launch --watcher` option that allows defining callbacks
  that are called for various events in the window's life-cycle (:iss:`2440`)

- Fix a regression in 0.17 that broke drawing of borders with non-minimal
  borders (:iss:`2474`)

- Hints shitten: Allow copying to primary selection as well as clipboard
  (:pull:`2487`)

- Add a new mappable action ``close_other_windows_in_tab`` to close all but the
  active window (:iss:`2484`)

- Hints shitten: Adjust the default regex used to detect line numbers to handle
  line+column numbers (:iss:`2268`)

- Fix blank space at the start of tab bar in the powerline style when first tab is
  inactive (:iss:`2478`)

- Fix regression causing incorrect rendering of separators in tab bar when
  defining a tab bar background color (:pull:`2480`)

- Fix a regression in 0.17 that broke the shitty @ launch remote command and
  also broke the --tab-title option when creating a new tab. (:iss:`2488`)

- Linux: Fix selection of fonts with multiple width variants not preferring
  the normal width faces (:iss:`2491`)


0.17.1 [2020-03-24]
--------------------

- Fix :opt:`cursor_underline_thickness` not working (:iss:`2465`)

- Fix a regression in 0.17 that caused tab bar background to be rendered after
  the last tab as well (:iss:`2464`)

- macOS: Fix a regression in 0.17 that caused incorrect variants to be
  automatically selected for some fonts (:iss:`2462`)

- Fix a regression in 0.17 that caused shitty @ set-colors to require setting
  cursor_text_color (:iss:`2470`)


0.17.0 [2020-03-24]
--------------------

- :ref:`splits_layout` to arrange windows in arbitrary splits
  (:iss:`2308`)

- Add support for specifying a background image, see :opt:`background_image`
  (:iss:`163` and :pull:`2326`; thanks to Fredrick Brennan.)

- A new :opt:`background_tint` option to darken the background under the text
  area when using background images and/or transparent windows.

- Allow selection of single cells with the mouse. Also improve mouse selection
  to follow semantics common to most programs (:iss:`945`)

- New options :opt:`cursor_beam_thickness` and :opt:`cursor_underline_thickness` to control the thickness of the
  beam and underline cursors (:iss:`2337` and :pull:`2342`)

- When the application running in the terminal grabs the mouse, pass middle
  clicks to the application unless `terminal_select_modifiers` are
  pressed (:iss:`2368`)

- A new ``copy_and_clear_or_interrupt`` function (:iss:`2403`)

- X11: Fix arrow mouse cursor using right pointing instead of the default left
  pointing arrow (:iss:`2341`)

- Allow passing the currently active shitty window id in the launch command
  (:iss:`2391`)

- unicode input shitten: Allow pressing :kbd:`ctrl+tab` to change the input mode
  (:iss:`2343`)

- Fix a bug that prevented using custom functions with the new marks feature
  (:iss:`2344`)

- Make the set of URL prefixes that are recognized while hovering with the
  mouse configurable (:iss:`2416`)

- Fix border/margin/padding sizes not being recalculated on DPI change
  (:iss:`2346`)

- diff shitten: Fix directory diffing with removed binary files failing
  (:iss:`2378`)

- macOS: Fix menubar title not updating on OS Window focus change (:iss:`2350`)

- Fix rendering of combining characters with fonts that have glyphs for
  precomposed characters but not decomposed versions (:iss:`2365`)

- Fix incorrect rendering of selection when using rectangular select and
  scrolling (:iss:`2351`)

- Allow setting WM_CLASS and WM_NAME when creating new OS windows with the
  launch command (:option:`launch --os-window-class`)

- macOS: When switching input method while a pending multi-key input is in
  progress, clear the pending input (:iss:`2358`)

- Fix a regression in the previous release that broke switching to neighboring windows
  in the Grid layout when there are less than four windows (:iss:`2377`)

- Fix colors in scrollback pager off if the window has redefined terminal
  colors using escape codes (:iss:`2381`)

- Fix selection not updating properly while scrolling (:iss:`2442`)

- Allow extending selections by dragging with right button pressed
  (:iss:`2445`)

- Workaround for bug in less that causes colors to reset at wrapped lines
  (:iss:`2381`)

- X11/Wayland: Allow drag and drop of text/plain in addition to text/uri-list
  (:iss:`2441`)

- Dont strip :code:`&` and :code:`-` from the end of URLs (:iss:`2436`)

- Fix ``@selection`` placeholder not working with launch command (:iss:`2417`)

- Drop support for python 3.5

- Wayland: Fix a crash when drag and dropping into shitty (:iss:`2432`)

- diff shitten: Fix images lingering as blank rectangles after the shitten quits
  (:iss:`2449`)

- diff shitten: Fix images losing position when scrolling using mouse
  wheel/touchpad


0.16.0 [2020-01-28]
--------------------

- A new :doc:`marks` feature that allows highlighting and scrolling to arbitrary
  text in the terminal window.

- hints shitten: Allow pressing :sc:`goto_file_line` to quickly open
  the selected file at the selected line in vim or a configurable editor (:iss:`2268`)

- Allow having more than one full height window in the :code:`tall` layout
  (:iss:`2276`)

- Allow choosing OpenType features for individual fonts via the
  :opt:`font_features` option. (:pull:`2248`)

- Wayland: Fix a freeze in rare circumstances when having multiple OS Windows
  (:iss:`2307` and :iss:`1722`)

- Wayland: Fix window titles being set to very long strings on the order of 8KB
  causing a crash (:iss:`1526`)

- Add an option :opt:`force_ltr` to turn off the display of text in RTL scripts
  in right-to-left order (:pull:`2293`)

- Allow opening new tabs/windows before the current tab/window as well as after
  it with the :option:`launch --location` option.

- Add a :opt:`resize_in_steps` option that can be used to resize the OS window
  in steps as large as character cells (:pull:`2131`)

- When triple-click+dragging to select multiple lines, extend the selection
  of the first line to match the rest on the left (:pull:`2284`)

- macOS: Add a :code:`titlebar-only` setting to
  :opt:`hide_window_decorations` to only hide the title bar (:pull:`2286`)

- Fix a segfault when using ``--debug-config`` with maps (:iss:`2270`)

- ``goto_tab`` now maps numbers larger than the last tab to the last tab
  (:iss:`2291`)

- Fix URL detection not working for urls of the form scheme:///url
  (:iss:`2292`)

- When windows are semi-transparent and all contain graphics, correctly render
  them. (:iss:`2310`)

0.15.1 [2019-12-21]
--------------------

- Fix a crash/incorrect rendering when detaching a window in some circumstances
  (:iss:`2173`)

- hints shitten: Add an option :option:`shitty +shitten hints --ascending` to
  control if the hints numbers increase or decrease from top to bottom

- Fix :opt:`background_opacity` incorrectly applying to selected text and
  reverse video text (:iss:`2177`)

- Add a new option :opt:`tab_bar_background` to specify a different color
  for the tab bar (:iss:`2198`)

- Add a new option :opt:`active_tab_title_template` to specify a different
  template for active tab titles (:iss:`2198`)

- Fix lines at the edge of the window at certain windows sizes when drawing
  images on a transparent window (:iss:`2079`)

- Fix window not being rendered for the first time until some input has been
  received from child process (:iss:`2216`)


0.15.0 [2019-11-27]
--------------------

- Add a new action :ref:`detach_window <detach_window>` that can be used to move the current
  window into a different tab (:iss:`1310`)

- Add a new action :doc:`launch <launch>` that unifies launching of processes
  in new shitty windows/tabs.

- Add a new style ``powerline`` for tab bar rendering, see :opt:`tab_bar_style` (:pull:`2021`)

- Allow changing colors by mapping a keyboard shortcut to read a shitty config
  file with color definitions. See the :doc:`FAQ <faq>` for details
  (:iss:`2083`)

- hints shitten: Allow completely customizing the matching and actions performed
  by the shitten using your own script (:iss:`2124`)

- Wayland: Fix key repeat not being stopped when focus leaves window. This is
  expected behavior on Wayland, apparently (:iss:`2014`)

- When drawing unicode symbols that are followed by spaces, use multiple cells
  to avoid resized or cut-off glyphs (:iss:`1452`)

- diff shitten: Allow diffing remote files easily via ssh (:iss:`727`)

- unicode input shitten: Add an option :option:`shitty +shitten unicode_input
  --emoji-variation` to control the presentation variant of selected emojis
  (:iss:`2139`)

- Add specialised rendering for a few more box powerline and unicode symbols
  (:pull:`2074` and :pull:`2021`)

- Add a new socket only mode for :opt:`allow_remote_control`. This makes
  it possible for programs running on the local machine to control shitty
  but not programs running over ssh.

- hints shitten: Allow using named groups in the regular expression. The named
  groups are passed to the invoked program for further processing.

- Fix a regression in 0.14.5 that caused rendering of private use glyphs
  with and without spaces to be identical (:iss:`2117`)

- Wayland: Fix incorrect scale used when first creating an OS window
  (:iss:`2133`)

- macOS: Disable mouse hiding by default as getting it to work robustly
  on Cocoa is too much effort (:iss:`2158`)


0.14.6 [2019-09-25]
---------------------

- macOS: Fix a regression in the previous release that caused a crash when
  pressing a unprintable key, such as the POWER key (:iss:`1997`)

- Fix a regression in the previous release that caused shitty to not always
  respond to DPI changes (:pull:`1999`)


0.14.5 [2019-09-23]
---------------------

- Implement a hack to (mostly) preserve tabs when cat-ting a file with them and then
  copying the text or passing screen contents to another program (:iss:`1829`)

- When all visible windows have the same background color, use that as the
  color for the global padding, instead of the configured background color
  (:iss:`1957`)

- When resetting the terminal, also reset parser state, this allows easy
  recovery from incomplete escape codes (:iss:`1961`)

- Allow mapping keys commonly found on European keyboards (:pull:`1928`)

- Fix incorrect rendering of some symbols when followed by a space while using
  the PowerLine font which does not have a space glyph (:iss:`1225`)

- Linux: Allow using fonts with spacing=90 in addition to fonts with
  spacing=100 (:iss:`1968`)

- Use selection foreground color for underlines as well (:iss:`1982`)

0.14.4 [2019-08-31]
---------------------

- hints shitten: Add a :option:`shitty +shitten hints --alphabet` option to
  control what alphabets are used for hints (:iss:`1879`)

- hints shitten: Allow specifying :option:`shitty +shitten hints --program`
  multiple times to run multiple programs  (:iss:`1879`)

- Add a :opt:`shitten_alias` option that can be used to alias shitten invocation
  for brevity and to change shitten option defaults globally (:iss:`1879`)

- macOS: Add an option :opt:`macos_show_window_title_in` to control
  showing the window title in the menubar/titlebar (:pull:`1837`)

- macOS: Allow drag and drop of text from other applications into shitty
  (:pull:`1921`)

- When running shittens, use the colorscheme of the current window
  rather than the configured colorscheme (:iss:`1906`)

- Don't fail to start if running the shell to read the EDITOR env var fails
  (:iss:`1869`)

- Disable the ``liga`` and ``dlig`` OpenType features for broken fonts
  such as Nimbus Mono.

- Fix a regression that broke setting background_opacity via remote control
  (:iss:`1895`)

- Fix piping PNG images into the icat shitten not working (:iss:`1920`)

- When the OS returns a fallback font that does not actually contain glyphs
  for the text, do not exhaust the list of fallback fonts (:iss:`1918`)

- Fix formatting attributes not reset across line boundaries when passing
  buffer as ANSI (:iss:`1924`)


0.14.3 [2019-07-29]
---------------------

- Remote control: Add a command `shitty @ scroll-window` to scroll windows

- Allow passing a ``!neighbor`` argument to the new_window mapping to open a
  new window next to the active window (:iss:`1746`)

- Document the shitty remote control protocol (:iss:`1646`)

- Add a new option :opt:`pointer_shape_when_grabbed` that allows you to control
  the mouse pointer shape when the terminal programs grabs the pointer
  (:iss:`1808`)

- Add an option `terminal_select_modifiers` to control which modifiers
  are used to override mouse selection even when a terminal application has
  grabbed the mouse (:iss:`1774`)

- When piping data to a child in the pipe command do it in a thread so as not
  to block the UI (:iss:`1708`)

- unicode_input shitten: Fix a regression that broke using indices to select
  recently used symbols.

- Fix a regression that caused closing an overlay window to focus
  the previously focused window rather than the underlying window (:iss:`1720`)

- macOS: Reduce energy consumption when idle by shutting down Apple's display
  link thread after 30 second of inactivity (:iss:`1763`)

- Linux: Fix incorrect scaling for fallback fonts when the font has an
  underscore that renders out of bounds (:iss:`1713`)

- macOS: Fix finding fallback font for private use unicode symbols not working
  reliably (:iss:`1650`)

- Fix an out of bounds read causing a crash when selecting text with the mouse
  in the alternate screen mode (:iss:`1578`)

- Linux: Use the system "bell" sound for the terminal bell. Adds libcanberra
  as a new dependency to play the system sound.

- macOS: Fix a rare deadlock causing shitty to hang (:iss:`1779`)

- Linux: Fix a regression in 0.14.0 that caused the event loop to tick
  continuously, wasting CPU even when idle (:iss:`1782`)

- ssh shitten: Make argument parsing more like ssh (:iss:`1787`)

- When using :opt:`strip_trailing_spaces` do not remove empty lines
  (:iss:`1802`)

- Fix a crash when displaying very large number of images (:iss:`1825`)


0.14.2 [2019-06-09]
---------------------

- Add an option :opt:`placement_strategy` to control how the cell area is
  aligned inside the window when the window size is not an exact multiple
  of the cell size (:pull:`1670`)

- hints shitten: Add a :option:`shitty +shitten hints --multiple-joiner` option to
  control how multiple selections are serialized when copying to clipboard
  or inserting into the terminal. You can have them on separate lines,
  separated by arbitrary characters, or even serialized as JSON (:iss:`1665`)

- macOS: Fix a regression in the previous release that broke using
  :kbd:`ctrl+shift+tab` (:iss:`1671`)

- panel shitten: Fix the contents of the panel shitten not being positioned
  correctly on the vertical axis

- icat shitten: Fix a regression that broke passing directories to icat
  (:iss:`1683`)

- clipboard shitten: Add a :option:`shitty +shitten clipboard --wait-for-completion`
  option to have the shitten wait till copying to clipboard is complete
  (:iss:`1693`)

- Allow using the :doc:`pipe <pipe>` command to send screen and scrollback
  contents directly to the clipboard (:iss:`1693`)

- Linux: Disable the Wayland backend on GNOME by default as GNOME has no
  support for server side decorations. Can be controlled by
  :opt:`linux_display_server`.

- Add an option to control the default :opt:`update_check_interval` when
  building shitty packages

- Wayland: Fix resizing the window on a compositor that does not provide
  server side window decorations, such a GNOME or Weston not working
  correctly (:iss:`1659`)

- Wayland: Fix crash when enabling disabling monitors on sway (:iss:`1696`)


0.14.1 [2019-05-29]
---------------------

- Add an option :opt:`command_on_bell` to run an arbitrary command when
  a bell occurs (:iss:`1660`)

- Add a shortcut to toggle maximized window state :sc:`toggle_maximized`

- Add support for the underscore key found in some keyboard layouts
  (:iss:`1639`)

- Fix a missing newline when using the pipe command between the
  scrollback and screen contents (:iss:`1642`)

- Fix colors not being preserved when using the pipe command with
  the pager history buffer (:pull:`1657`)

- macOS: Fix a regression that could cause rendering of a shitty window
  to occasionally freeze in certain situations, such as moving it between
  monitors or transitioning from/to fullscreen (:iss:`1641`)

- macOS: Fix a regression that caused :kbd:`cmd+v` to double up in the dvorak
  keyboard layout (:iss:`1652`)

- When resizing and only a single window is present in the current layout,
  use that window's background color to fill in the blank areas.

- Linux: Automatically increase cell height if the font being used is broken
  and draws the underscore outside the bounding box (:iss:`690`)

- Wayland: Fix maximizing the window on a compositor that does not provide
  server side window decorations, such a GNOME or Weston not working
  (:iss:`1662`)


0.14.0 [2019-05-24]
---------------------

- macOS: The default behavior of the Option key has changed. It now generates
  unicode characters rather than acting as the :kbd:`Alt` modifier. See
  :opt:`macos_option_as_alt`.

- Support for an arbitrary number of internal clipboard buffers to copy/paste
  from, see (:ref:`cpbuf`)

- Allow using the new private internal clipboard buffers with the
  :opt:`copy_on_select` option (:iss:`1390`)

- macOS: Allow opening new shitty tabs/top-level windows from Finder
  (:pull:`1350`)

- Add an option :opt:`disable_ligatures` to disable
  multi-character ligatures under the cursor to make editing easier
  or disable them completely (:iss:`461`)

- Allow creating new OS windows in session files (:iss:`1514`)

- Allow setting OS window size in session files

- Add an option :opt:`tab_switch_strategy` to control which
  tab becomes active when the current tab is closed (:pull:`1524`)

- Allow specifying a value of ``none`` for the :opt:`selection_foreground`
  which will cause shitty to not change text color in selections (:iss:`1358`)

- Make live resizing of OS windows smoother and add an option
  :opt:`resize_draw_strategy` to control what is drawn while a
  resize is in progress.

- macOS: Improve handling of IME extended input. Compose characters
  are now highlighted and the IME panel moves along with the text
  (:pull:`1586`). Also fixes handling of delete key in Chinese IME
  (:iss:`1461`)

- When a window is closed, switch focus to the previously active window (if
  any) instead of picking the previous window in the layout (:iss:`1450`)

- icat shitten: Add support for displaying images at http(s) URLs (:iss:`1340`)

- A new option :opt:`strip_trailing_spaces` to optionally remove trailing
  spaces from lines when copying to clipboard.

- A new option :opt:`tab_bar_min_tabs` to control how many tabs must be
  present before the tab-bar is shown (:iss:`1382`)

- Automatically check for new releases and notify when an update is available,
  via the system notification facilities. Can be controlled by
  :opt:`update_check_interval` (:iss:`1342`)

- macOS: Fix :kbd:`cmd+period` key not working (:iss:`1318`)

- macOS: Add an option `macos_show_window_title_in_menubar` to not
  show the current window title in the menu-bar (:iss:`1066`)

- macOS: Workaround for cocoa bug that could cause the mouse cursor to become
  hidden in other applications in rare circumstances (:iss:`1218`)

- macOS: Allow assigning only the left or right :kbd:`Option` key to work as the
  :kbd:`Alt` key. See :opt:`macos_option_as_alt` for details (:iss:`1022`)

- Fix using remote control to set cursor text color causing errors when
  creating new windows (:iss:`1326`)

- Fix window title for minimized windows not being updated (:iss:`1332`)

- macOS: Fix using multi-key sequences to input text ignoring the
  first few key presses if the sequence is aborted (:iss:`1311`)

- macOS: Add a number of common macOS keyboard shortcuts

- macOS: Reduce energy consumption by not rendering occluded windows

- Fix scrollback pager history not being cleared when clearing the
  main scrollback buffer (:iss:`1387`)

- macOS: When closing a top-level window only switch focus to the previous shitty
  window if it is on the same workspace (:iss:`1379`)

- macOS: Fix :opt:`sync_to_monitor` not working on Mojave.

- macOS: Use the system cursor blink interval by default
  :opt:`cursor_blink_interval`.

- Wayland: Use the shitty Wayland backend by default. Can be switched back
  to using XWayland by setting the environment variable:
  ``shitty_DISABLE_WAYLAND=1``

- Add a ``no-append`` setting to :opt:`clipboard_control` to disable
  the shitty copy concatenation protocol extension for OSC 52.

- Update to using the Unicode 12 standard

- Unicode input shitten: Allow using the arrow keys in code mode to go to next
  and previous unicode symbol.

- macOS: Fix specifying initial window size in cells not working correctly on
  Retina screens (:iss:`1444`)

- Fix a regression in version 0.13.0 that caused background colors of space
  characters after private use unicode characters to not be respected
  (:iss:`1455`)

- Only update the selected text to clipboard when the selection is finished,
  not continuously as it is updated. (:iss:`1460`)

- Allow setting :opt:`active_border_color` to ``none`` to not draw a border
  around the active window (:iss:`805`)

- Use negative values for :opt:`mouse_hide_wait` to hide the mouse cursor
  immediately when pressing a key (:iss:`1534`)

- When encountering errors in :file:`shitty.conf` report them to the user
  instead of failing to start.

- Allow the user to control the resize debounce time via
  :opt:`resize_debounce_time`.

- Remote control: Make the :ref:`at_set-font-size` command more capable.
  It can now increment font size and reset it. It also only acts on the
  active top-level window, by default (:iss:`1581`)

- When launching child processes set the :code:`PWD` environment variable
  (:iss:`1595`)

- X11: use the window manager's native full-screen implementation when
  making windows full-screen (:iss:`1605`)

- Mouse selection: When extending by word, fix extending selection to non-word
  characters not working well (:iss:`1616`)

0.13.3 [2019-01-19]
------------------------------

- icat shitten: Add a ``--stdin`` option to control if image data is read from
  STDIN (:iss:`1308`)

- hints shitten: Start hints numbering at one instead of zero by default. Added
  an option ``--hints-offset`` to control it. (:iss:`1289`)

- Fix a regression in the previous release that broke using ``background`` for
  :opt:`cursor_text_color` (:iss:`1288`)

- macOS: Fix dragging shitty window tabs in traditional full screen mode causing
  crashes (:iss:`1296`)

- macOS: Ensure that when running from a bundle, the bundle shitty exe is
  preferred over any shitty in PATH (:iss:`1280`)

- macOS: Fix a regression that broke mapping of :kbd:`ctrl+tab` (:iss:`1304`)

- Add a list of user-created shittens to the docs

- Fix a regression that broke changing mouse wheel scroll direction with
  negative :opt:`wheel_scroll_multiplier` values in full-screen applications
  like vim (:iss:`1299`)

- Fix :opt:`background_opacity` not working with pure white backgrounds
  (:iss:`1285`)

- macOS: Fix "New OS Window" dock action not working when shitty is not focused
  (:iss:`1312`)

- macOS: Add aliases for close window and new tab actions that conform to common
  Apple shortcuts for these actions (:iss:`1313`)

- macOS: Fix some shittens causing 100% CPU usage


0.13.2 [2019-01-04]
------------------------------

- Add a new option :opt:`tab_title_template` to control how tab titles
  are formatted. In particular the template can be used to display
  the tab number next to the title (:iss:`1223`)

- Report the current foreground processes as well as the original child process,
  when using `shitty @ ls`

- Use the current working directory of the foreground process for the
  `*_with_cwd` actions that open a new window with the current working
  directory.

- Add a new ``copy_or_interrupt`` action that can be mapped to kbd:`ctrl+c`. It
  will copy if there is a selection and interrupt otherwise (:iss:`1286`)

- Fix setting :opt:`background_opacity` causing window margins/padding to be slightly
  different shade from background (:iss:`1221`)

- Handle keyboards with a "+" key (:iss:`1224`)

- Fix Private use Unicode area characters followed by spaces at the end of text
  not being rendered correctly (:iss:`1210`)

- macOS: Add an entry to the dock menu to open a new OS window (:iss:`1242`)

- macOS: Fix scrolling very slowly with wheel mice not working (:iss:`1238`)

- Fix changing :opt:`cursor_text_color` via remote control not working
  (:iss:`1229`)

- Add an action to resize windows that can be mapped to shortcuts in :file:`shitty.conf`
  (:pull:`1245`)

- Fix using the ``new_tab !neighbor`` action changing the order of the
  non-neighboring tabs (:iss:`1256`)

- macOS: Fix momentum scrolling continuing when changing the active window/tab
  (:iss:`1267`)


0.13.1 [2018-12-06]
------------------------------

- Fix passing input via the pipe action to a program without a window not
  working.

- Linux: Fix a regression in the previous release that caused automatic
  selection of bold/italic fonts when using aliases such as "monospace" to not
  work (:iss:`1209`)

- Fix resizing window smaller and then restoring causing some wrapped lines to not
  be properly unwrapped (:iss:`1206`)

0.13.0 [2018-12-05]
------------------------------

- Add an option :opt:`scrollback_pager_history_size` to tell shitty to store
  extended scrollback to use when viewing the scrollback buffer in a pager
  (:iss:`970`)

- Modify the shittens sub-system to allow creating custom shittens without any
  user interface. This is useful for creating more complex actions that can
  be bound to key presses in :file:`shitty.conf`. See
  doc:`shittens/custom`. (:iss:`870`)

- Add a new ``nth_window`` action that can be used to go to the nth window and
  also previously active windows, using negative numbers. Similarly,
  ``goto_tab`` now accepts negative numbers to go to previously active tabs
  (:iss:`1040`)

- Allow hiding the tab bar completely, by setting :opt:`tab_bar_style` to
  ``hidden``. (:iss:`1014`)

- Allow private use unicode characters to stretch over more than a single
  neighboring space (:pull:`1036`)

- Add a new :opt:`touch_scroll_multiplier` option to modify the amount
  scrolled by high precision scrolling devices such as touchpads (:pull:`1129`)

- icat shitten: Implement reading image data from STDIN, if STDIN is not
  connected to a terminal (:iss:`1130`)

- hints shitten: Insert trailing spaces after matches when using the
  ``--multiple`` option. Also add a separate ``--add-trailing-space``
  option to control this behavior (:pull:`1132`)

- Fix the ``*_with_cwd`` actions using the cwd of the overlay window rather
  than the underlying window's cwd (:iss:`1045`)

- Fix incorrect key repeat rate on wayland (:pull:`1055`)

- macOS: Fix drag and drop of files not working on Mojave (:iss:`1058`)

- macOS: Fix IME input for East Asian languages (:iss:`910`)

- macOS: Fix rendering frames-per-second very low when processing
  large amounts of input in small chunks (:pull:`1082`)

- macOS: Fix incorrect text sizes calculated when using an external display
  that is set to mirror the main display (:iss:`1056`)

- macOS: Use the system default double click interval (:pull:`1090`)

- macOS: Fix touch scrolling sensitivity low on retina screens (:iss:`1112`)

- Linux: Fix incorrect rendering of some fonts when hinting is disabled at
  small sizes (:iss:`1173`)

- Linux: Fix match rules used as aliases in Fontconfig configuration not being
  respected (:iss:`1085`)

- Linux: Fix a crash when using the GNU Unifont as a fallback font
  (:iss:`1087`)

- Wayland: Fix copying from hidden shitty windows hanging (:iss:`1051`)

- Wayland: Add support for the primary selection protocol
  implemented by some compositors (:pull:`1095`)

- Fix expansion of env vars not working in the :opt:`env` directive
  (:iss:`1075`)

- Fix :opt:`mouse_hide_wait` only taking effect after an event such as cursor
  blink or key press (:iss:`1073`)

- Fix the ``set_background_opacity`` action not working correctly
  (:pull:`1147`)

- Fix second cell of emoji created using variation selectors not having
  the same attributes as the first cell (:iss:`1109`)

- Fix focusing neighboring windows in the grid layout with less than 4 windows
  not working (:iss:`1115`)

- Fix :kbd:`ctrl+shift+special` key not working in normal and application keyboard
  modes (:iss:`1114`)

- Add a terminfo entry for full keyboard mode.

- Fix incorrect text-antialiasing when using very low background opacity
  (:iss:`1005`)

- When double or triple clicking ignore clicks if they are "far" from each
  other (:iss:`1093`)

- Follow xterm's behavior for the menu key (:iss:`597`)

- Fix hover detection of URLs not working when hovering over the first colon
  and slash characters in short URLs (:iss:`1201`)

0.12.3 [2018-09-29]
------------------------------

- macOS: Fix shitty window not being rendered on macOS Mojave until the window is
  moved or resized at least once (:iss:`887`)

- Unicode input: Fix an error when searching for the string 'fir' (:iss:`1035`)


0.12.2 [2018-09-24]
------------------------------

- A new ``last_used_layout`` function that can be mapped to a shortcut to
  switch to the previously used window layout (:iss:`870`)

- New ``neighboring_window`` and ``move_window`` functions to switch to
  neighboring windows in the current layout, and move them around, similar to
  window movement in vim (:iss:`916`)

- A new ``pipe`` function that can be used to pipe the contents of the screen
  and scrollback buffer to any desired program running in a new window, tab or
  overlay window. (:iss:`933`)

- Add a new :option:`shitty --start-as` command line flag to start shitty
  full-screen/maximized/minimized. This replaces the ``--start-in-fullscreen``
  flag introduced in the previous release (:iss:`935`)

- When mapping the ``new_tab`` action allow specifying that the tab should open
  next to the current tab instead of at the end of the tabs list (:iss:`979`)

- macOS: Add a new :opt:`macos_thicken_font` to make text rendering
  on macs thicker, which makes it similar to the result of
  sub-pixel antialiasing (:pull:`950`)

- macOS: Add an option :opt:`macos_traditional_fullscreen` to make
  full-screening of shitty windows much faster, but less pretty. (:iss:`911`)

- Fix a bug causing incorrect line ordering when viewing the scrollback buffer
  if the scrollback buffer is full (:iss:`960`)

- Fix drag-scrolling not working when the mouse leaves the window confines
  (:iss:`917`)

- Workaround for broken editors like nano that cannot handle newlines in pasted text
  (:iss:`994`)

- Linux: Ensure that the python embedded in the shitty binary build uses
  UTF-8 mode to process command-line arguments (:iss:`924`)

- Linux: Handle fonts that contain monochrome bitmaps (such as the Terminus TTF
  font) (:pull:`934`)

- Have the :option:`shitty --title` flag apply to all windows created
  using :option:`shitty --session` (:iss:`921`)

- Revert change for backspacing of wide characters in the previous release,
  as it breaks backspacing in some wide character aware programs (:iss:`875`)

- Fix shitty @set-colors not working for tab backgrounds when using the `fade` tabbar style
  (:iss:`937`)

- macOS: Fix resizing semi-transparent windows causing the windows to be
  invisible during the resize (:iss:`941`)

- Linux: Fix window icon not set on X11 for the first OS window (:iss:`961`)

- macOS: Add an :opt:`macos_custom_beam_cursor` option to use a special
  mouse cursor image that can be seen on both light and dark backgrounds
  (:iss:`359`)

- Remote control: Fix the ``focus_window`` command not focusing the
  top-level OS window of the specified shitty window (:iss:`1003`)

- Fix using :opt:`focus_follows_mouse` causing text selection with the
  mouse to malfunction when using multiple shitty windows (:iss:`1002`)

0.12.1 [2018-09-08]
------------------------------

- Add a new ``--start-in-fullscreen`` command line flag to start
  shitty in full screen mode (:iss:`856`)

- macOS: Fix a character that cannot be rendered in any font causing
  font fallback for all subsequent characters that cannot be rendered in the
  main font to fail (:iss:`799`)

- Linux: Do not enable IME input via ibus unless the ``GLFW_IM_MODULE=ibus``
  environment variable is set. IME causes key processing latency and even
  missed keystrokes for many people, so it is now off by default.

- Fix backspacing of wide characters in wide-character unaware programs not working (:iss:`875`)

- Linux: Fix number pad arrow keys not working when Numlock is off (:iss:`857`)

- Wayland: Implement support for clipboard copy/paste (:iss:`855`)

- Allow mapping shortcuts using the raw key code from the OS (:iss:`848`)

- Allow mapping of individual key-presses without modifiers as shortcuts

- Fix legacy invocation of icat as `shitty icat` not working (:iss:`850`)

- Improve rendering of wavy underline at small font sizes (:iss:`853`)

- Fix a regression in 0.12.0 that broke dynamic resizing of layouts (:iss:`860`)

- Wayland: Allow using the :option:`shitty --class` command line flag
  to set the app id (:iss:`862`)

- Add completion of the shitty command for the fish shell (:pull:`829`)

- Linux: Fix XCompose rules with no defined symbol not working (:iss:`880`)

- Linux: Fix crash with some Nvidia drivers when creating tabs in the first
  top level-window after creating a second top-level window. (:iss:`873`)

- macOS: Diff shitten: Fix syntax highlighting not working because of
  a bug in the 0.12.0 macOS package

0.12.0 [2018-09-01]
------------------------------

- Preserve the mouse selection even when the contents of the screen are
  scrolled or overwritten provided the new text does not intersect the
  selected lines.

- Linux: Implement support for Input Method Extensions (multilingual input
  using standard keyboards) via `IBus
  <https://github.com/ibus/ibus/wiki/ReadMe>`_ (:iss:`469`)

- Implement completion for the shitty command in bash and zsh. See
  :ref:`completion`.

- Render the text under the cursor in a fixed color, configurable via
  the option :opt:`cursor_text_color` (:iss:`126`)

- Add an option :opt:`env` to set environment variables in child processes
  from shitty.conf

- Add an action to the ``clear_terminal`` function to scroll the screen
  contents into the scrollback buffer (:iss:`1113`)

- Implement high precision scrolling with the trackpad on platforms such as
  macOS and Wayland that implement it. (:pull:`819`)

- macOS: Allow scrolling window contents using mouse wheel/trackpad even when the
  window is not the active window (:iss:`729`)

- Remote control: Allow changing the current window layout with a new
  :ref:`at_goto-layout` command (:iss:`845`)

- Remote control: Allow matching windows by the environment variables of their
  child process as well

- Allow running shittens via the remote control system (:iss:`738`)

- Allow enabling remote control in only some shitty windows

- Add a keyboard shortcut to reset the terminal (:sc:`reset_terminal`). It
  takes parameters so you can define your own shortcuts to clear the
  screen/scrollback also (:iss:`747`)

- Fix one-pixel line appearing at window edges at some window sizes when
  displaying images with background opacity enabled (:iss:`741`)

- diff shitten: Fix error when right hand side file is binary and left hand side
  file is text (:pull:`752`)

- shitty @ new-window: Add a new option :option:`shitty @ new-window --window-type`
  to create top-level OS windows (:iss:`770`)

- macOS: The :opt:`focus_follows_mouse` option now also works across top-level shitty OS windows
  (:iss:`754`)

- Fix detection of URLs in HTML source code (URLs inside quotes) (:iss:`785`)

- Implement support for emoji skin tone modifiers (:iss:`787`)

- Round-trip the zwj unicode character. Rendering of sequences containing zwj
  is still not implemented, since it can cause the collapse of an unbounded
  number of characters into a single cell. However, shitty at least preserves
  the zwj by storing it as a combining character.

- macOS: Disable the custom mouse cursor. Using a custom cursor fails on dual
  GPU machines. I give up, Apple users will just have to live with the
  limitations of their choice of OS. (:iss:`794`)

- macOS: Fix control+tab key combination not working (:iss:`801`)

- Linux: Fix slow startup on some systems caused by GLFW searching for
  joysticks. Since shitty does not use joysticks, disable joystick support.
  (:iss:`830`)


0.11.3 [2018-07-10]
------------------------------

- Draw only the minimum borders needed for inactive windows. That is only the borders
  that separate the inactive window from a neighbor. Note that setting
  a non-zero window margin overrides this and causes all borders to be drawn.
  The old behavior of drawing all borders can be restored via the
  :opt:`draw_minimal_borders` setting in shitty.conf. (:iss:`699`)

- macOS: Add an option :opt:`macos_window_resizable` to control if shitty
  top-level windows are resizable using the mouse or not (:iss:`698`)

- macOS: Use a custom mouse cursor that shows up well on both light and dark backgrounds
  (:iss:`359`)

- macOS: Workaround for switching from fullscreen to windowed mode with the
  titlebar hidden causing window resizing to not work. (:iss:`711`)

- Fix triple-click to select line not working when the entire line is filled
  (:iss:`703`)

- When dragging to select with the mouse "grab" the mouse so that if it strays
  into neighboring windows, the selection is still updated (:pull:`624`)

- When clicking in the margin/border area of a window, map the click to the
  nearest cell in the window. Avoids selection with the mouse failing when
  starting the selection just outside the window.

- When drag-scrolling stop the scroll when the mouse button is released.

- Fix a regression in the previous release that caused pasting large amounts
  of text to be duplicated (:iss:`709`)


0.11.2 [2018-07-01]
------------------------------

- Linux: Allow using XKB key names to bind shortcuts to keys not supported by GLFW (:pull:`665`)

- shitty shell: Ignore failure to read readline history file. Happens if the
  user migrates their shitty cache directory between systems with incompatible
  readline implementations.

- macOS: Fix an error in remote control when using --listen-on (:iss:`679`)

- hints shitten: Add a :option:`shitty +shitten hints --multiple` option to select
  multiple items (:iss:`687`)

- Fix pasting large amounts of text very slow (:iss:`682`)

- Add an option :opt:`single_window_margin_width` to allow different margins
  when only a single window is visible in the layout (:iss:`688`)

- Add a :option:`shitty --hold` command line option to stay open after the child process exits (:iss:`667`)

- diff shitten: When triggering a search scroll to the first match automatically

- :option:`shitty --debug-font-fallback` also prints out what basic fonts were matched

- When closing a shitty window reset the mouse cursor to its default shape and ensure it is visible (:iss:`655`).

- Remote control: Speed-up reading of command responses

- Linux installer: Fix installer failing on systems with python < 3.5

- Support "-T" as an alias for "--title" (:pull:`659`)

- Fix a regression in the previous release that broke using
  ``--debug-config`` with custom key mappings (:iss:`695`)


0.11.1 [2018-06-17]
------------------------------

- diff shitten: Implement searching for text in the diff (:iss:`574`)

- Add an option :opt:`startup_session` to :file:`shitty.conf` to specify a
  default startup session (:iss:`641`)

- Add a command line option :option:`shitty --wait-for-single-instance-window-close`
  to make :option:`shitty --single-instance` wait for the closing of the newly opened
  window before quitting (:iss:`630`)

- diff shitten: Allow theming the selection background/foreground as well

- diff shitten: Display CRLF line endings using the unicode return symbol
  instead of <d> as it is less intrusive (:iss:`638`)

- diff shitten: Fix default foreground/background colors not being restored when
  shitten quits (:iss:`637`)

- Fix :option:`shitty @ set-colors --all` not working when more than one window
  present (:iss:`632`)

- Fix a regression that broke the legacy increase/decrease_font_size actions

- Clear scrollback on reset (:iss:`631`)


0.11.0 [2018-06-12]
------------------------------

- A new tab bar style "fade" in which each tab's edges fade into the background.
  See :opt:`tab_bar_style` and :opt:`tab_fade` for details. The old look can be
  restored by setting :opt:`tab_bar_style` to :code:`separator`.

- :doc:`Pre-compiled binaries <binary>` with all bundled dependencies for Linux
  (:iss:`595`)

- A :doc:`new shitten <shittens/panel>` to create dock panels on X11 desktops
  showing the output from arbitrary terminal programs.

- Reduce data sent to the GPU per render by 30% (:commit:`8dea5b3`)

- Implement changing the font size for individual top level (OS) windows
  (:iss:`408`)

- When viewing the scrollback in less using :sc:`show_scrollback` and shitty
  is currently scrolled, position the scrollback in less to match shitty's
  scroll position. (:iss:`148`)

- ssh shitten: Support all SSH options. It can now be aliased directly to ssh
  for convenience. (:pull:`591`)

- icat shitten: Add :option:`shitty +shitten icat --print-window-size` to easily
  detect the window size in pixels from scripting languages (:iss:`581`)

- hints shitten: Allow selecting hashes from the terminal with
  :sc:`insert_selected_hash` useful for git commits. (:pull:`604`)

- Allow specifying initial window size in number of cells in addition to pixels
  (:iss:`436`)

- Add a setting to control the margins to the left and right of the tab-bar
  (:iss:`584`)

- When closing a tab switch to the last active tab instead of the right-most
  tab (:iss:`585`)

- Wayland: Fix shitty not starting when using wl_roots based compositors
  (:iss:`157`)

- Wayland: Fix mouse wheel/touchpad scrolling in opposite direction to other apps (:iss:`594`)

- macOS: Fix the new OS window keyboard shortcut (:sc:`new_os_window`) not
  working if no shitty window currently has focus. (:iss:`524`)

- macOS: Keep shitty running even when the last window is closed. This is in
  line with how applications are supposed to behave on macOS (:iss:`543`).
  There is a new option (:opt:`macos_quit_when_last_window_closed`) to control
  this.

- macOS: Add macOS standard shortcuts for copy, paste and new OS window
  (⌘+C, ⌘+V, ⌘+N)

- Add a config option (:opt:`editor`) to set the EDITOR shitty uses (:iss:`580`)

- Add a config option (``x11_hide_window_decorations``) to hide window
  decorations under X11/Wayland (:iss:`607`)

- Add an option to @set-window-title to make the title change non-permanent
  (:iss:`592`)

- Add support for the CSI t escape code to query window and cell sizes
  (:iss:`581`)

- Linux: When using layouts that map the keys to non-ascii characters,
  map shortcuts using the ascii equivalents, from the default layout.
  (:iss:`606`)

- Linux: Fix fonts not being correctly read from TrueType Collection
  (.ttc) files (:iss:`577`)

- Fix :opt:`inactive_text_alpha` also applying to the tab bar (:iss:`612`)

- :doc:`hints shitten <shittens/hints>`: Fix a regression that caused some blank lines to be not
  be displayed.

- Linux: Include a man page and the HTML docs when building the linux-package

- Remote control: Fix shitty @ sometimes failing to read the response from
  shitty. (:iss:`614`)

- Fix `shitty @ set-colors` not working with the window border colors.
  (:iss:`623`)

- Fix a regression in 0.10 that caused incorrect rendering of the status bar in
  irssi when used inside screen. (:iss:`621`)


0.10.1 [2018-05-24]
------------------------------

- Add a shitten to easily ssh into servers that automatically copies the
  terminfo files over. ``shitty +shitten ssh myserver``.

- diff shitten: Make the keyboard shortcuts configurable (:iss:`563`)

- Allow controlling *background_opacity* via either keyboard shortcuts or
  remote control. Note that you must set *dynamic_background_opacity yes* in
  shitty.conf first. (:iss:`569`)

- diff shitten: Add keybindings to scroll by page

- diff shitten: Fix incorrect syntax highlighting for a few file formats such as
  yaml

- macOS: Fix regression that caused the *macos_option_as_alt* setting to always
  be disabled for all OS windows in a shitty instance after the first window
  (:iss:`571`)

- Fix Ctrl+Alt+Space not working in normal and application keyboard modes
  (:iss:`562`)


0.10.0 [2018-05-21]
------------------------------

- A diff shitten to show side-by-side diffs with syntax highlighting and support
  for images. See :doc:`diff shitten <shittens/diff>`.

- Make windows in the various shitty layouts manually resizable. See
  :ref:`layouts` for details.

- Implement support for the SGR *faint* escape code to make text blend
  into the background (:iss:`446`).

- Make the hints shitten a little smarter (:commit:`ad1109b`)
  so that URLs that stretch over multiple lines are detected. Also improve
  detection of surrounding brackets/quotes.

- Make the shitty window id available as the environment variable
  ``shitty_WINDOW_ID`` (:iss:`532`).

- Add a "fat" layout that is similar to the "tall" layout but vertically
  oriented.

- Expand environment variables in config file include directives

- Allow programs running in shitty to read/write from the clipboard (:commit:`889ca77`).
  By default only writing is allowed. This feature is supported in many
  terminals, search for `OSC 52 clipboard` to find out more about using it.

- Fix moving cursor outside a defined page area incorrectly causing the cursor
  to be placed inside the page area. Caused incorrect rendering in neovim, in
  some situations (:iss:`542`).

- Render a couple more powerline symbols directly, bypassing the font
  (:iss:`550`).

- Fix ctrl+alt+<special> not working in normal and application keyboard (:iss:`548`).

- Partial fix for rendering Right-to-left languages like Arabic. Rendering of
  Arabic is never going to be perfect, but now it is at least readable.

- Fix Ctrl+backspace acting as plain backspace in normal and application
  keyboard modes (:iss:`538`).

- Have the paste_from_selection action paste from the clipboard on platforms
  that do not have a primary selection such as Wayland and macOS
  (:iss:`529`)

- Fix cursor_stop_blinking_after=0 not working (:iss:`530`)


0.9.1 [2018-05-05]
------------------------------

- Show a bell symbol on the tab if a bell occurs in one of the windows in the tab and
  the window is not the currently focused window

- Change the window border color if a bell occurs in an unfocused window. Can
  be disabled by setting the bell_border_color to be the same as the
  inactive_border_color.

- macOS: Add support for dead keys

- Unicode input: When searching by name search for prefix matches as well as
  whole word matches

- Dynamically allocate the memory used for the scrollback history buffer.
  Reduces startup memory consumption when using very large scrollback
  buffer sizes.

- Add an option to not request window attention on bell.

- Remote control: Allow matching windows by number (visible position).

- macOS: Fix changing tab title and shitty shell not working

- When triple-clicking select all wrapped lines belonging to a single logical line.

- hints shitten: Detect bracketed URLs and don't include the closing bracket in the URL.

- When calling pass_selection_to_program use the current directory of the child
  process as the cwd of the program.

- Add macos_hide_from_tasks option to hide shitty from the macOS task switcher

- macOS: When the macos_titlebar_color is set to background change the titlebar
  colors to match the current background color of the active shitty window

- Add a setting to clear all shortcuts defined up to that point in the config
  file(s)

- Add a setting (shitty_mod) to change the modifier used by all the default
  shitty shortcuts, globally

- Fix Shift+function key not working

- Support the F13 to F25 function keys

- Don't fail to start if the user deletes the hintstyle key from their
  fontconfig configuration.

- When rendering a private use unicode codepoint and a space as a two cell
  ligature, set the foreground colors of the space cell to match the colors of
  the first cell. Works around applications like powerline that use different
  colors for the two cells.

- Fix passing @text to other programs such as when viewing the scrollback
  buffer not working correctly if shitty is itself scrolled up.

- Fix window focus gained/lost events not being reported to child programs when
  switching windows/tabs using the various keyboard shortcuts.

- Fix tab title not changing to reflect the window title when switching between different windows in a tab

- Ignore -e if it is specified on the command line. This is for compatibility
  with broken software that assumes terminals should run with an -e option to
  execute commands instead of just passing the commands as arguments.


0.9.0 [2018-04-15]
------------------------------

- A new shitty command shell to allow controlling shitty via commands. Press
  `ctrl+shift+escape` to run the shell.

- The hints shitten has become much more powerful. Now in addition to URLs you
  can use it to select word, paths, filenames, lines, etc. from the screen.
  These can be inserted into the terminal, copied to clipboard or sent to
  external programs.

- Linux: Switch to libxkbcommon for keyboard handling. It allows shitty to
  support XCompose and dead keys and also react to keyboard remapping/layout
  change without needing a restart.

- Add support for multiple-key-sequence shortcuts

- A new remote control command `set-colors` to change the current and/or
  configured colors.

- When double-clicking to select a word, select words that continue onto the
  next/prev line as well.

- Add an `include` directive for the config files to read multiple config files

- Improve mouse selection for windows with padding. Moving the mouse into the
  padding area now acts as if the mouse is over the nearest cell.

- Allow setting all 256 terminal colors in the config file

- Fix using `shitty --single-instance` to open a new window in a running shitty
  instance, not respecting the `--directory` flag

- URL hints: Exclude trailing punctuation from URLs

- URL hints: Launch the browser from the shitty parent process rather than the
  hints shitten. Fixes launching on some systems where xdg-open doesn't like
  being run from a shitten.

- Allow using rectangle select mode by pressing shift in addition to the
  rectangle select modifiers even when the terminal program has grabbed the
  mouse.


0.8.4 [2018-03-31]
-----------------------------

- Fix presence of XDG_CONFIG_DIRS and absence of XDG_CONFIG_HOME preventing
  shitty from starting

- Revert change in last release to cell width calculation. Instead just clip
  the right edges of characters that overflow the cell by at most two pixels


0.8.3 [2018-03-29]
-----------------------------

- Fix a regression that broke the visual bell and invert screen colors escape
  code

- Allow double-click and triple-click + drag to extend selections word at a
  time or line at a time

- Add a keyboard shortcut to set the tab title

- Fix setting window title to empty via OSC escape code not working correctly

- Linux: Fix cell width calculation incorrect for some fonts (cell widths are
  now calculated by actually rendering bitmaps, which is slower but more
  accurate)

- Allow specifying a system wide shitty config file, for all users

- Add a --debug-config command line flag to output data about the system and
  shitty configuration.

- Wayland: Fix auto-repeat of keys not working


0.8.2 [2018-03-17]
-----------------------------

- Allow extending existing selections by right clicking

- Add a configurable keyboard shortcut and remote command to set the font size to a specific value

- Add an option to have shitty close the window when the main processes running in it exits, even if there are still background processes writing to that terminal

- Add configurable keyboard shortcuts to switch to a specific layout

- Add a keyboard shortcut to edit the shitty config file easily

- macOS: Fix restoring of window size not correct on Retina screens

- macOS: Add a facility to specify command line arguments when running shitty from the GUI

- Add a focus-tab remote command

- Fix screen not being refreshed immediately after moving a window.

- Fix a crash when getting the contents of the scrollback buffer as text

0.8.1 [2018-03-09]
-----------------------------

- Extend shitty's remote control feature to work over both UNIX and TCP sockets,
  so now you can control shitty from across the internet, if you want to.

- Render private use unicode characters that are followed by a space as a two
  character ligature. This fixes rendering for applications that misuse
  private-use characters to display square symbols.

- Fix Unicode emoji presentation variant selector causing new a fallback font
  instance to be created

- Fix a rare error that prevented the Unicode input shitten from working
  sometimes

- Allow using Ctrl+Alt+letter in legacy keyboard modes by outputting them as Ctrl+letter and Alt+letter.
  This matches other terminals' behavior.

- Fix cursor position off-by-one on horizontal axis when resizing the terminal

- Wayland: Fix auto-repeat of keys not working

- Wayland: Add support for window decorations provided by the Wayland shell

- macOS: Fix URL hints not working

- macOS: Fix shell not starting in login mode on some computers

- macOS: Output errors into console.app when running as a bundle


0.8.0 [2018-02-24]
-----------------------------

- A framework for shittens, that is, small terminal programs designed to run
  inside shitty and extend its capabilities. Examples include unicode input and
  selecting URLs with the keyboard.

- Input arbitrary unicode characters by pressing Ctrl+Shift+u. You can choose
  characters by name, by hex code, by recently used, etc. There is even and
  editable Favorites list.

- Open URLs using only the keyboard. shitty has a new "hints mode". Press
  Ctrl+Shift+e and all detected URLs on the screen are highlighted with a key
  to press to open them. The facility is customizable so you can change
  what is detected as a URL and which program is used to open it.

- Add an option to change the titlebar color of shitty windows on macOS

- Only consider Emoji characters with default Emoji presentation to be two
  cells wide. This matches the standard. Also add support for the Unicode Emoji
  variation presentation selector.

- Prevent video tearing during high speed scrolling by syncing draws
  to the monitor's refresh rate. There is a new configuration option to
  control this ``sync_to_monitor``.

- When displaying only a single window, use the default background color of the
  window (which can be changed via escape codes) as the color for the margin
  and padding of the window.

- Add some non standard terminfo capabilities used by neovim and tmux.

- Fix large drop in performance when using multiple top-level windows on macOS

- Fix save/restore of window sizes not working correctly.

- Remove option to use system wcwidth(). Now always use a wcwidth() based on
  the Unicode standard. Only sane way.

- Fix a regression that caused a few ligature glyphs to not render correctly in
  rare circumstances.

- Browsing the scrollback buffer now happens in an overlay window instead of a
  new window/tab.

0.7.1 [2018-01-31]
---------------------------

- Add an option to adjust the width of character cells

- Fix selecting text with the mouse in the scrollback buffer selecting text
  from the line above the actually selected line

- Fix some italic fonts having the right edge of characters cut-off,
  unnecessarily


0.7.0 [2018-01-24]
---------------------------

- Allow controlling shitty from the shell prompt/scripts. You can
  open/close/rename windows and tabs and even send input to specific windows.
  See the README for details.

- Add option to put tab bar at the top instead of the bottom

- Add option to override the default shell

- Add "Horizontal" and "Vertical" window layouts

- Sessions: Allow setting titles and working directories for individual windows

- Option to copy to clipboard on mouse select

- Fix incorrect reporting of mouse move events when using the SGR protocol

- Make alt+backspace delete the previous word

- Take the mouse wheel multiplier option in to account when generating fake key
  scroll events

- macOS: Fix closing top-level window does not transfer focus to other
  top-level windows.

- macOS: Fix alt+arrow keys not working when disabling the macos_option_as_alt
  config option.

- shitty icat: Workaround for bug in ImageMagick that would cause some images
  to fail to display at certain sizes.

- Fix rendering of text with ligature fonts that do not use dummy glyphs

- Fix a regression that caused copying of the selection to clipboard to only
  copy the visible part of the selection

- Fix incorrect handling of some unicode combining marks that are not re-ordered

- Fix handling on non-BMP combining characters

- Drop the dependency on libunistring


0.6.1 [2017-12-28]
---------------------------

- Add an option to fade the text in inactive windows

- Add new actions to open windows/tabs/etc. with the working directory set to
  the working directory of the current window.

- Automatically adjust cell size when DPI changes, for example when shitty is
  moved from one monitor to another with a different DPI

- Ensure underlines are rendered even for fonts with very poor metrics

- Fix some emoji glyphs not colored on Linux

- Internal wcwidth() implementation is now auto-generated from the unicode
  standard database

- Allow configuring the modifiers to use for rectangular selection with the
  mouse.

- Fix incorrect minimum wayland version in the build script

- Fix a crash when detecting a URL that ends at the end of the line

- Fix regression that broke drawing of hollow cursor when window loses focus


0.6.0 [2017-12-18]
---------------------------

- Support background transparency via the background_opacity option. Provided
  that your OS/window manager supports transparency, you can now have shitty
  render pixels that have only the default background color as
  semi-transparent.

- Support multiple top level (OS) windows. These windows all share the sprite
  texture cache on the GPU, further reducing overall resource usage. Use
  the shortcut `ctrl+shift+n` to open a new top-level window.

- Add support for a *daemon* mode using the `--single-instance` command line
  option. With this option you can have only a single shitty instance running.
  All future invocations simply open new top-level windows in the existing
  instance.

- Support colored emoji

- Use CoreText instead of FreeType to render text on macOS

- Support running on the "low power" GPU on dual GPU macOS machines

- Add a new "grid" window layout

- Drop the dependency on glfw (shitty now uses a modified, bundled copy of glfw)

- Add an option to control the audio bell volume on X11 systems

- Add a command line switch to set the name part of the WM_CLASS window
  property independently.

- Add a command line switch to set the window title.

- Add more options to customize the tab-bar's appearance (font styles and
  separator)

- Allow drag and drop of files into shitty. On drop shitty will paste the
  file path to the running program.

- Add an option to control the underline style for URL highlighting on hover

- X11: Set the WINDOWID environment variable

- Fix middle and right buttons swapped when sending mouse events to child
  processes

- Allow selecting in a rectangle by holding down Ctrl+Alt while dragging with
  the mouse.


0.5.1 [2017-12-01]
---------------------------

- Add an option to control the thickness of lines in box drawing characters

- Increase max. allowed ligature length to nine characters

- Fix text not vertically centered when adjusting line height

- Fix unicode block characters not being rendered properly

- Fix shift+up/down not generating correct escape codes

- Image display: Fix displaying images taller than two screen heights not
  scrolling properly


0.5.0 [2017-11-19]
---------------------------

- Add support for ligature fonts such as Fira Code, Hasklig, etc. shitty now
  uses harfbuzz for text shaping which allow it to support advanced OpenType
  features such as contextual alternates/ligatures/combining glyphs/etc.

- Make it easy to select fonts by allowing listing of monospace fonts using:
  shitty list-fonts

- Add an option to have window focus follow mouse

- Add a keyboard shortcut (ctrl+shift+f11) to toggle fullscreen mode

- macOS: Fix handling of option key. It now behaves just like the alt key on
  Linux. There is an option to make it type unicode characters instead.

- Linux: Add support for startup notification on X11 desktops. shitty will
  now inform the window manager when its startup is complete.

- Fix shell prompt being duplicated when window is resized

- Fix crash when displaying more than 64 images in the same session

- Add support for colons in SGR color codes. These are generated by some
  applications such as neovim when they mistakenly identify shitty as a libvte
  based terminal.

- Fix mouse interaction not working in apps using obsolete mouse interaction
  protocols

- Linux: no longer require glew as a dependency


0.4.2 [2017-10-23]
---------------------------

- Fix a regression in 0.4.0 that broke custom key mappings

- Fix a regression in 0.4.0 that broke support for non-QWERTY keyboard layouts

- Avoid using threads to reap zombie child processes. Also prevent shitty from
  hanging if the open program hangs when clicking on a URL.


0.4.0 [2017-10-22]
---------------------------

- Support for drawing arbitrary raster graphics (images) in the terminal via a
  new graphics protocol. shitty can draw images with full 32-bit color using both
  ssh connections and files/shared memory (when available) for better
  performance. The drawing primitives support alpha blending and z-index.
  Images can be drawn both above and below text. See :doc:`graphics-protocol`.
  for details.

- Refactor shitty's internals to make it even faster and more efficient. The CPU
  usage of shitty + X server while doing intensive tasks such as scrolling a
  file continuously in less has been reduced by 50%. There are now two
  configuration options ``repaint_delay`` and ``input_delay`` you can use to
  fine tune shitty's performance vs CPU usage profile. The CPU usage of shitty +
  X when scrolling in less is now significantly better than most (all?) other
  terminals. See :doc:`performance`.

- Hovering over URLs with the mouse now underlines them to indicate they
  can be clicked. Hold down Ctrl+Shift while clicking to open the URL.

- Selection using the mouse is now more intelligent. It does not add
  blank cells (i.e. cells that have no content) after the end of text in a
  line to the selection.

- The block cursor in now fully opaque but renders the character under it in
  the background color, for enhanced visibility.

- Allow combining multiple independent actions into a single shortcut

- Add a new shortcut to pass the current selection to an external program

- Allow creating shortcuts to open new windows running arbitrary commands. You
  can also pass the current selection to the command as an arguments and the
  contents of the screen + scrollback buffer as stdin to the command.
