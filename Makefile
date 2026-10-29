.PHONY: build check research-check release-check demo workflow-check render-check recipe-check geometry-check benefit-check rer-check

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

research-check:
	python scripts/check_research.py

# Integrated slice; use a fresh directory for each demo.
demo:
	python -m housing_workflow demo --out runs/first-demo

workflow-check:
	python -m housing_workflow verify --run examples/parcel-investigation
	python -m unittest discover -s housing_workflow/tests -v

render-check:
	python -m housing_render verify --run examples/site-concept/with-analysis
	python -m housing_render verify --run examples/site-concept/standalone
	python -m unittest discover -s housing_render/tests -v

recipe-check:
	python -m unittest discover -s housing_recipe/tests -v

geometry-check:
	python -m unittest discover -s housing_geometry/tests -v

benefit-check:
	python -m unittest discover -s housing_benefit/tests -v

rer-check:
	python -m unittest discover -s housing_rer/tests -v
