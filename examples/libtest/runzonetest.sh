#!/bin/sh

usage ( ) {
	echo "Usage: $0 [ python | v8 ] MODULE" >&2
	echo "(Do not add the extension .py)"
	exit 1;
}

if [ -z $2 ] ; then
	usage
fi
if [ ! -f $2.py ] ; then
	echo "File not found: $2.py" >&2
	usage
fi

case "$1" in 
	v8)
		CMD="python ../../pyv8/pyv8run.py --strict $2"
		;;
	python)
		CMD="python $2.py"
		;;
	*)
		usage
		;;
esac

for TZ in 'Europe/London' 'Europe/Amsterdam' 'America/New_York' 'America/Sao_Paulo' 'Australia/Brisbane' ; do
	export TZ
	echo "Timezone: $TZ (`date`)"
	$CMD
done
