#!/bin/bash

tmux new -A -s 'main' -n 'servers' -d
tmux send-keys -t main:0.0 "cat playerpipe" Enter
tmux splitw -v -t main:0.0
tmux send-keys -t main:0.1 "cat itempipe" Enter
tmux attach-session

