#!/bin/bash

# run gunicorn
exec gunicorn \
    -b "localhost:5004" \
    -t 300 \
    -w 5 \
    server:app
