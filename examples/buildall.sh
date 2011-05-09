#!/bin/sh
options="$@"

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

ls -1 | while read d ; do
	if [ -f $d/build.sh ] ; then
		(cd $d; ./build.sh $options)
	fi
done
