#!/bin/sh

if ! [ -f "./manifest.scm" ]; then
    echo "ERR - must call from project root"
    exit 1
fi

guix shell --container \
    --network \
    -m manifest.scm \
    guile-colorized \
    guile-readline \
    --expose="$HOME/.guile" \
    -- guile || echo "ERR - unknown error"
