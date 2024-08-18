#!/bin/sh

if ! [ -f "./manifest.scm" ]; then
    echo "ERR - must call from project root"
    exit 1
fi

guix shell -m manifest.scm -- guile -s src/examples/poc-render.scm || echo "ERR - unknown error"
