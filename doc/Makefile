all: gendocs upload uploadexamples

gendocs:
	python gendocs.py

# you need to make this your own username,pyjamasgroupname unfortunately.
# sf being stupid.
upload:
	cp -aux pyjs_site/output/* .
	rsync --exclude=examples --delete -rlvz * lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/

uploadsitehtml:
	cp -aux pyjs_site/public/* .
	rsync -rlvz pyjs_site/public/* lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/

uploadexamples:
	rsync -rlvz ../examples lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/

