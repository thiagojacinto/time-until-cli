clean:
	rm -rfv src/__pycache__ \
	src/*.egg-info \
	tests/__pycache__ \
	coverage \
	.coverage \
	dist

setup: requirements-development.txt
	pip install -r requirements-development.txt

test:
	python -m pytest -v

coverage:
	python -m pytest --cov=src \
		--cov-report html:coverage/html \
		--cov-report xml:coverage/xml/coverage.xml \
		--cov-report term-missing tests/

build: setup
	python -m build