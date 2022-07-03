#!/bin/sh
picom &
exec /usr/share/cadence/src/cadence_session_start.py -s &
cadence -s &
/usr/bin/emacs --daemon &
lxsession --noautostart &
ssh-agent -s &
variety &
exec kill 1211 &
dunst &
exec xrandr --output DVI-I-0 --off --output DVI-I-1 --mode 1920x1080 --pos 0x1080 --rotate normal --output HDMI-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output DP-5 --off &
