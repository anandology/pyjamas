#!/bin/sh
options="$*"
if [ -z "$options" ] ; then options="-O";fi

get_puremvc ( ) {
	URL="http://puremvc.org/pages/downloads/Python/PureMVC_Python.zip"
	if which wget >/dev/null ; then
		wget -O PureMVC_Python.zip "$URL"
	elif which curl >/dev/null ; then
		curl -o PureMVC_Python.zip "$URL"
	else
		echo "No wget/curl found" >&2
		exit 1
	fi
}
if [ ! -f PureMVC_Python_1_0/src/puremvc/__init__.py ] ; then
	get_puremvc
	if ! unzip PureMVC_Python.zip ; then
		echo "Cannot unzip PureMVC_Python.zip" >&2
		exit 1
	fi
	if [ ! -f PureMVC_Python_1_0/src/puremvc/__init__.py ] ; then
		echo "Something went wrong...."
		exit 1
	fi
fi
../../bin/pyjsbuild --library_dir "`pwd`/PureMVC_Python_1_0/src" $options EmployeeAdmin.py
