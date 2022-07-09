# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
import socket
from libqtile import hook
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/qtilescreens.sh"])


mod = "mod4"
mod1 = "mod1"
browser = "librewolf"
discord = "discord"
file_manager = "dolphin"

myTerm = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Media controls
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc="Lowers volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc="Raises volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer sset Master 1+ toggle"),
        desc="Muutes volume",
    ),
    Key([], "Print", lazy.spawn("spectacle"), desc="print screen"),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause player",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"), desc="Skip to previous"),
    # Switch between screens
    Key([mod1], "1", lazy.to_screen(0), desc="Move focus to screen 0"),
    Key([mod1], "2", lazy.to_screen(1), desc="Move focus to screen 1"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "r", lazy.spawn("dmenu_run -p 'Run: '"), desc="Run Launcher"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "d", lazy.spawn(discord), desc="Launch Discord"),
    Key([mod, "shift"], "f", lazy.spawn(file_manager), desc="Launch Dolphin"),
    Key([mod, "shift"], "b", lazy.spawn(browser), desc="Launch LibreWolf"),
    Key([mod, "shift"], "t", lazy.spawn("thunar"), desc="Launch thunar"),
    Key([mod, "shift"], "e", lazy.spawn("emacs"), desc="Launch Emacs"),
    Key([mod, "shift"], "v", lazy.spawn("vlc"), desc="Launch VLC"),
    Key([mod, "shift"], "m", lazy.spawn("betterbird"), desc="Launch Betterbird"),
    Key([mod, "shift"], "o", lazy.spawn("okular"), desc="Launch Okular"),
    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    KeyChord(["control"],"e", [
        Key([], "e",
            lazy.spawn("emacsclient --eval '(emacs-everywhere)'"),
            desc='Launch Emacs Everywhere! MUWAHAHA'
            ),
        Key([], "b",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
            desc='Launch ibuffer inside Emacs'
            ),
        Key([], "d",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
            desc='Launch dired inside Emacs'
            ),
#        Key([], "i",
#            lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
#            desc='Launch erc inside Emacs'
#            ),
#        Key([], "m",
#            lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
#            desc='Launch mu4e inside Emacs'
#            ),
        Key([], "n",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
            desc='Launch elfeed inside Emacs'
            ),
        Key([], "s",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
            desc='Launch the eshell inside Emacs'
            ),
        Key([], "v",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
            desc='Launch vterm inside Emacs'
            )
    ]),
]


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


keys.extend(
    [
        Key([mod, "shift"], "comma", lazy.function(window_to_next_screen)),
        Key([mod, "shift"], "period", lazy.function(window_to_previous_screen)),
        Key(
            [mod, "control"],
            "comma",
            lazy.function(window_to_next_screen, switch_screen=True),
        ),
        Key(
            [mod, "control"],
            "period",
            lazy.function(window_to_previous_screen, switch_screen=True),
        ),
    ]
)


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "margin": 10,
    "border_focus": "#bd93f9",
    "border_width": 2,
    "font": "FuraCode Nerd Font Mono",
    "fontsize": 12,
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font="FuraCode Nerd Font Mono",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"],
]

dracula = {
    "background": "#282a36",
    "current": "#44475a",
    "foreground": "f8f8f2",
    "comment": "#6272a4",
    "cyan": "#8be9fd",
    "green": "#50fa7b",
    "orange": "#ffb86c",
    "pink": "#ff79c6",
    "purple": "#bd93f9",
    "red": "#ff5555",
    "yellow": "#f1fa8c"
}


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm)},
        ),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="Source Code Pro Black",
            fontsize=11,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=dracula["background"],
            foreground=dracula["comment"],
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=dracula["cyan"],
            background=dracula["background"],
            padding=0,
            scale=0.8,
        ),
        widget.CurrentLayout(
            foreground=dracula["foreground"], background=dracula["background"],
            padding=5, font="Source Code Pro Black"),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=dracula["background"],
            foreground=dracula["comment"],
            padding=2,
            fontsize=15,
        ),
        widget.WindowName(
            foreground=dracula["purple"], background=dracula["background"],
            padding=0, font="Source Code Pro Black",),
        widget.Systray(background=dracula["background"], padding=5, font="Source Code Pro Black",),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[0], background=dracula["background"]),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["background"],
            foreground=dracula["current"],
            padding=0,
            fontsize=40,
        ),
        widget.Net(
            format="歷 {down} ↓↑ {up}",
            foreground=dracula["cyan"],
            background=dracula["current"],
            padding=5,
            update_interval=5,
            font="Source Code Pro Black",
        ),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["current"],
            foreground=dracula["comment"],
            padding=0,
            fontsize=37,
        ),
        widget.ThermalSensor(
            foreground=dracula["orange"],
            background=dracula["comment"],
            threshold=90,
            fmt="﬙ {}",
            padding=5,
            font="Source Code Pro Black",
        ),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["comment"],
            foreground=dracula["current"],
            padding=0,
            fontsize=37,
        ),
#        widget.CheckUpdates(
#            update_interval=1800,
#            distro="Manjaro",
#            display_format="ﮮ {updates} ",
#            foreground=dracula["background"],
#            colour_have_updates=dracula["orange"],
#            colour_no_updates=dracula["orange"],
#            mouse_callbacks={
#                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e sudo pacman -Syu")
#            },
#            padding=5,
#            background=dracula["orange"],
#        ),
#        widget.TextBox(
#            text="",
#            font="Ubuntu Mono",
#            background=dracula["orange"],
#            foreground=dracula["yellow"],
#            padding=0,
#            fontsize=37,
#        ),
        widget.Memory(
            foreground=dracula["purple"],
            background=dracula["current"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            fmt=" {}",
            padding=5,
            font="Source Code Pro Black",
        ),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["current"],
            foreground=dracula["comment"],
            padding=0,
            fontsize=37,
        ),
        widget.Volume(
            foreground=dracula["yellow"],
            background=dracula["comment"], fmt="墳 {}", padding=5,
            font="Source Code Pro Black",
        ),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["comment"],
            foreground=dracula["current"],
            padding=0,
            fontsize=37,
        ),
        widget.OpenWeather(
            foreground=dracula["pink"], background=dracula["current"],
            padding=5, location="Wellington Point, AU",
            format=" {main_temp}{units_temperature} {humidity}%",
            font="Source Code Pro Black",
        ),
        widget.TextBox(
            text="",
            font="Ubuntu Mono",
            background=dracula["current"],
            foreground=dracula["comment"],
            padding=0,
            fontsize=37,
        ),
        widget.Clock(
            foreground=dracula["green"], background=dracula["comment"],
            format=" %A, %B %d - %H:%M ",
            font="Source Code Pro Black",),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[
        9:10
    ]  # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


screens = [
#    Screen(
#        wallpaper="~/Downloads/city2.jpg",
#        wallpaper_mode="stretch",
#        top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.8, size=20),
#   ),
    Screen(
#        wallpaper="~/Downloads/city1.jpg",
#        wallpaper_mode="stretch",
        top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.8, size=20),
    ),
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Spectacle"),
        Match(wm_class="Spectacle"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
