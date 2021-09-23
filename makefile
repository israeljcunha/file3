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
