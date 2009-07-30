VERSION=0.6pre2
DEBSUBVERSION=1

help:
	@echo
	@echo choose one of the following:
	@echo "    make local-build"
	@echo "    make system-install"
	@echo "    make debian-build"
	@echo

# 'sandbox' build - can be used locally.
# e.g. building examples with ../../bin/pyjsbuild
local-build:
	python bootstrap.py

# must be done as root, duh.
system-install:
	python bootstrap.py /usr/share/pyjamas /usr
	python run_bootstrap_first_then_setup.py install

# stoopid stoopid debianism requires a diff file, otherwise
# lintian complains.  put everything here to make builds be
# happy, by creating a .orig.tar.gz that _doesn't_ have
# the debian/ directory in it, then manually copy it
# over, to build it.  much joy.
debian-build: 
	mkdir -p deb/pyjamas-${VERSION}
	tar -cvzf deb/pyjamas_$(VERSION).orig.tar.gz \
	         --exclude=debian \
	         --exclude=./deb \
	         --exclude=output \
	         --exclude=build \
	         --exclude=./bin \
	         --exclude=fckeditor \
	         --exclude=*.pyc \
	         --exclude=.git* \
	         --exclude=.*.sw? \
			 --exclude=deb \
			 .
	tar -C deb/pyjamas-${VERSION} -xvzf deb/pyjamas_$(VERSION).orig.tar.gz
	cp -aux debian deb/pyjamas-${VERSION}
	cd deb/pyjamas-${VERSION} && dpkg-buildpackage -rfakeroot
	cd deb && lintian pyjamas_${VERSION}-${DEBSUBVERSION}_all.deb
	cd deb && lintian pyjamas_${VERSION}-${DEBSUBVERSION}.dsc

