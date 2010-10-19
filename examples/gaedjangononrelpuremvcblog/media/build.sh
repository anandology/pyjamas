#!/bin/sh
options="$@"


../../../code/pyjamas/bin/pyjsbuild --library_dir "`pwd`/PureMVC_Python_1_1/src" $options Blog
