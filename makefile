update_twine:
	python3 -m pip install --upgrade twine

compile:
	python setup.py sdist
	python3 -m twine check dist/*

upload:
	python3 -m twine upload -u israel.cunha --repository-url https://upload.pypi.org/legacy/ dist/* --verbose

build:
	python3 -m pip install --upgrade build
	python3 -m build

build_all: update_twine compile build upload

update:
	python3 -m pip install --upgrade pip

test_build:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

upload2:
	pip install -U pip setuptools twine
	python setup.py sdist bdist_wheel upload

pre-commit-install:
	pre-commit install
	pre-commit run --all-files

###
# Clean local folder section
###
clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@find . -iname '.benchmarks' -delete
	@find . -iname '.pytest_cache' -exec rm -rf "{}" \+

clean_all: clean-eggs clean-build clean


####
## Tests
####
unit:
	python3 -m unittest -v -f

export_test:
	pip freeze > .requirements.test
