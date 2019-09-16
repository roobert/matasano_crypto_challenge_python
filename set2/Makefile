default: test

TESTS=$(shell ls test_*.py)

test:
	@for test in $(TESTS); do ./$$test -v; done
