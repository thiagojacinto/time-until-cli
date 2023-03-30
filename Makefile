clean:
	rm -rf src/__pycache__ src/*.egg-info tests/__pycache__ dist

setup: requirements-development.txt
	pip install -r requirements-development.txt

test:
	python -m pytest -v

build: setup
	python -m build