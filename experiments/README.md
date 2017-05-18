Performance tests using Tsung
=============================

## Running the tests
```
tsung -k -f tsung_websocket.xml start
```
This will start the tests, as well as a web dashboard on `localhost:8091`.

## A not for Ubuntu users

The Tsung package that ships with Ubuntu Zesty is broken.
Follow [these](http://tsung.erlang-projects.org/user_manual/installation.html) instructions to download and install Tsung 1.6 or later.

