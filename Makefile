DESTDIR=
PREFIX=/usr
NAME=cloudinstancecredentials
dirs = lib
files = Makefile README.md LICENSE set-http-basic-credentials set-http-basic-credentials.service setup.py requirements-dev.txt requirements.txt

verSpec = $(shell rpm -q --specfile --qf '%{VERSION}' *.spec)
verSrc = $(shell cat lib/cloudinstancecredentials/VERSION)

ifneq "$(verSpec)" "$(verSrc)"
$(error "Version mismatch, will not take any action")
endif

clean:
	@find . -name "*.pyc" | xargs rm -f
	@find . -name "__pycache__" | xargs rm -rf
	@find . -name "*.cache" | xargs rm -rf
	@find . -name "*.egg-info" | xargs rm -rf

pep8: clean
	@pep8 -v --statistics lib/cloudinstancecredentials/*
	@pep8 -v --statistics --ignore=E402 tests/*.py

tar: clean
	rm -rf $(NAME)-$(verSrc)
	mkdir $(NAME)-$(verSrc)
	cp -r $(dirs) $(files) "$(NAME)-$(verSrc)"
	tar -cjf "$(NAME)-$(verSrc).tar.bz2" "$(NAME)-$(verSrc)"
	rm -rf "$(NAME)-$(verSrc)"

test:
	py.test tests/cloudinstancecredentials.py

install:
	python3 setup.py install --prefix="$(PREFIX)" --root="$(DESTDIR)"
