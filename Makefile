.PHONY: compile install lint type run setup test

setup:
	$(shell which python3.7) -m venv venv ; pip install pip-tools

compile:
	. venv/bin/activate; pip-compile --output-file requirements.txt requirements.in

install: compile
	. venv/bin/activate; pip install -r requirements.txt

type:
	. venv/bin/activate; mypy --ignore-missing-imports **/*.py

lint: type
	. venv/bin/activate; flake8 pharaoh

test: type
	. venv/bin/activate; PYTHONPATH=./pharaoh python -m pytest pharaoh/tests

run: lint
	. venv/bin/activate; venv/bin/python $(shell pwd)/pharaoh/__main__.py


