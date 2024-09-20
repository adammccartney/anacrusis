#!/bin/sh

if ! [ -f "./manifest.scm" ]; then
    echo "ERR - must call from project root"
    exit 1
fi

SCRIPT="$1"
if [ -z $SCRIPT ]; then
    echo "ERR -- please specify a script";
    exit 1
fi

guix shell -m manifest.scm -- guile -s $SCRIPT || echo "ERR - unknown error"
