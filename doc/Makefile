all: gendocs upload

gendocs:
	#python gendocs.py

# you need to make this your own username,pyjamasgroupname unfortunately.
# sf being stupid.
upload:
	rsync -rlvz * lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/

uploadexamples:
	rsync -rlvz ../examples lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/
