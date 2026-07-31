outdir = $(shell pwd)
version = $(shell git describe --tags --abbrev=0 | tr -d v)

srpm:
	git archive --prefix=vm-curator-$(version)/ HEAD \
		-o $(outdir)/vm-curator-$(version).tar.gz
	rpmbuild -bs vm-curator.spec \
		--define "_sourcedir $(outdir)" \
		--define "_srcrpmdir $(outdir)"
