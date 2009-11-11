#!/bin/bash

./build.sh

python2.5 LibTest.py

./pyv8test.sh --strict | grep 'failed'

./check_js_lint.sh

./check_coverage.sh

