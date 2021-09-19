compile:
	python setup.py sdist
	twine check dist/*

upload:
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

build:
	python3 -m pip install --upgrade build
	python3 -m build

build_all: compile build upload

update:
	python3 -m pip install --upgrade pip

test_build:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*