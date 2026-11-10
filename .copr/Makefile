outdir = $(shell pwd)
version = $(shell awk '/^Version:/ {print $$2}' packaging/lgl-vm-curator.spec)

srpm:
	dnf install -y git-core
	git archive --prefix=lgl-vm-curator-$(version)/ HEAD \
		-o $(outdir)/lgl-vm-curator-$(version).tar.gz
	rpmbuild -bs packaging/lgl-vm-curator.spec \
		--define "_sourcedir $(outdir)" \
		--define "_srcrpmdir $(outdir)"
