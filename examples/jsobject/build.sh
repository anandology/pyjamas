#!/bin/sh
../../bin/pyjsbuild $@ --include-js jsrecttest.js TestRect
../../bin/pyjsbuild $@ --no-compile-inplace TestDict
