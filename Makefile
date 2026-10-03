.PHONY: build check release-check

build:
	python pipeline.py

check: build
	python lint.py
	python -m unittest discover -s tests -v
	python schema_check.py
	python validate.py

release-check: check
	node tests/check_explorer.cjs
	python pipeline.py
	python validate.py
	python replay_check.py
