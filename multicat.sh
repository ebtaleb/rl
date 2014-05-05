#!/bin/bash

tmux new -A -s 'main' -n 'servers' -d
tmux send-keys -t main:1.1 "cat playerpipe" Enter
tmux splitw -v -t main:1.1
tmux send-keys -t main:1.2 "cat itempipe" Enter
tmux attach-session

