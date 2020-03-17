.PHONY: clean tests cov release-tag

VERSION = $(shell python -c "print(__import__('didadata').__version__)")

clean:
	rm -fr docs/_build build/ dist/

tests:
	py.test --cov

cov: tests
	coverage html
	@echo open htmlcov/index.html

release-tag:
	@echo About to release ${VERSION}
	@echo [ENTER] to continue; read
	git tag -a "v${VERSION}" -m "Version v${VERSION}" && git push --follow-tags
