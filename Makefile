default: test

SUBDIRS=$(shell ls -d set*/)

test:
	@for dir in $(SUBDIRS); do make -C $$dir; done

depends:
	@pip3 install iteration_utilities pycryptodome

