.PHONY: all setup clean_dist distro clean install

NAME=vcs2l
VERSION=`./setup.py --version`

all:
	echo "noop for debbuild"

setup:
	echo "building version ${VERSION}"

clean_dist:
	-rm -rf deb_dist
	-rm -rf dist
	-rm -rf vcs2l.egg-info

distro: setup clean_dist
	python setup.py sdist

clean: clean_dist
	echo "clean"

install: distro
	sudo checkinstall python setup.py install
