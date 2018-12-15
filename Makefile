.PHONY: compile install type run setup

setup:
	$(shell which python3.7) -m venv venv ; pip install pip-tools

compile:
	. venv/bin/activate; pip-compile --output-file requirements.txt requirements.in

install: compile
	. venv/bin/activate; pip install -r requirements.txt

type:
	. venv/bin/activate; mypy --ignore-missing-imports .

run: type
	. venv/bin/activate; venv/bin/python $(shell pwd)/__main__.py

