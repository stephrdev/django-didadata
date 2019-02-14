.PHONY: clean tests cov release

VERSION = $(shell pipenv run python -c "print(__import__('didadata').__version__)")

clean:
	rm -fr docs/_build build/ dist/

tests:
	pipenv run py.test --cov

cov: tests
	pipenv run coverage html
	@echo open htmlcov/index.html

release:
	@echo About to release ${VERSION}
	@echo [ENTER] to continue; read
	rm -fr docs/_build build/ dist/
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	git tag -a "${VERSION}" -m "Version ${VERSION}" && git push --follow-tags
