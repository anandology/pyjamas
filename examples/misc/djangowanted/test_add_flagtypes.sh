#!/bin/sh

cat << EOF  | ./manage.py shell
from wanted.forms import test_add_flagtypes
test_add_flagtypes()
EOF
echo

