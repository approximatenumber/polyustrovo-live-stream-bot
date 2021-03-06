#!/bin/bash

export PATH="$PATH:/usr/local/bin"
if ./capture.py; then
    for image in *.png; do
	date=$(date -r $image "+%d.%m.%Y, %H:%M")
	telegram-send --image "$image" --caption "$date"
    done
fi
