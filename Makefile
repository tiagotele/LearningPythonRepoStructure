unit_test:
	python3 -m pytest -v 

run_example:
	python run.py

code_format:
	black .

code_lint:
	python3 lint.py -p ../src/