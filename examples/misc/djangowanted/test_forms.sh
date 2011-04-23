#!/bin/sh

cat << EOF  | ./manage.py shell
from wanted.forms import test_item_form
test_item_form()
EOF
echo

