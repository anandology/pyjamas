#!/bin/sh
options="$@"

if [ -z "$DOWNLOADS" ] ; then
	if echo $options |grep -- '--downloads-yes'>/dev/null ; then
		DOWNLOADS=yes
		export DOWNLOADS
		options=`echo "$options"|sed 's/--downloads-yes//g'`
	fi
	if echo $options |grep -- '--downloads-no'>/dev/null ; then
		DOWNLOADS=no
		export DOWNLOADS
		options=`echo "$options"|sed 's/--downloads-no//g'`
	fi
fi

if (cd ../employeeadmin;./download.sh) ; then
../../bin/pyjsbuild --library_dir "`pwd`/../employeeadmin/PureMVC_Python_1_1/src" $options TimeSheet
fi
