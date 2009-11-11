#!/bin/bash

# prerequisities: python-coverage

OUTPUT=coverage_report

if [ ! -d $OUTPUT ]; then mkdir $OUTPUT; fi
rm $OUTPUT/*,cover
python-coverage -x compile_only.py
python-coverage -a -o /usr -d coverage_report

