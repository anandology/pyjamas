all: gendocs upload uploadexamples

gendocs:
	python gendocs.py
	rsync --delete -rlvz api pyjs.org:/var/www/pyjs.org/htdocs/

upload:
	cp -aux pyjs_site/output/* .
	rsync --exclude=pygit --exclude=examples --exclude=api --exclude=wiki \
          --delete -rlvz * pyjs.org:/var/www/pyjs.org/htdocs/

uploadexamples:
	rsync -rlvz ../examples pyjs.org:/var/www/pyjs.org/htdocs/

# use this to _just_ upload the web site, not everything else
uploadsitehtml:
	cp -aux pyjs_site/public/* .
	rsync -rlvz pyjs_site/public/* pyjs.org:/var/www/pyjs.org/htdocs/

