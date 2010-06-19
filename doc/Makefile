all: gendocs upload uploadexamples

gendocs:
	python gendocs.py

# you need to make this your own username,pyjamasgroupname unfortunately.
# sf being stupid.
upload:
	cp -aux pyjs_site/output/* .
	#rsync --exclude=examples --delete -rlvz * lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/
	rsync --exclude=examples --delete -rlvz * 10.8.0.1:/var/www/pyjs.org/htdocs/

uploadsitehtml:
	cp -aux pyjs_site/public/* .
	#rsync -rlvz pyjs_site/public/* lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/
	rsync -rlvz pyjs_site/public/* 10.8.0.1:/var/www/pyjs.org/htdocs/

uploadexamples:
	#rsync -rlvz ../examples lkcl,pyjamas@web.sf.net:/home/groups/p/py/pyjamas/htdocs/
	rsync -rlvz ../examples 10.8.0.1:/var/www/pyjs.org/htdocs/

