#!/bin/sh
options="$@"

if [ -z "$DOWNLOADS" ] ; then
	if echo $options |grep -- '--downloads-ok'>/dev/null ; then
		DOWNLOADS=yes
		export DOWNLOADS
		options=`echo "$options"|sed 's/--downloads-ok//g'`
	fi
fi

if ./download.sh ; then
	../../bin/pyjsbuild --library_dir "`pwd`/PureMVC_Python_1_0/src" $options EmployeeAdmin
fi
