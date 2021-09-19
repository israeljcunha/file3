twine:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository file3 dist/*

build:
	python3 -m pip install --upgrade build
	python3 -m build

build_all: twine build

update:
	python3 -m pip install --upgrade pip
