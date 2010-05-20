#!/bin/sh

case "$1" in 
	v8)
		CMD='python ../../pyv8/pyv8run.py --strict TimeModuleTest'
		;;
	python)
		CMD='python TimeModuleTest.py'
		;;
	*)
		echo "Usage: $0 [ python | v8 ]" >&2
		exit 1
		;;
esac

for TZ in 'Europe/London' 'Europe/Amsterdam' 'America/New_York' 'America/Sao_Paulo' 'Australia/Brisbane' ; do
	export TZ
	echo "Timezone: $TZ (`date`)"
	$CMD
done
