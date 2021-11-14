#!/bin/sh
docker run --rm -it --name opencv_python -v $PWD:/home -w /home opencv_python:latest python3 main.py
