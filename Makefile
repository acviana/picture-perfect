black:
	black picture_perfect
	black tests

black-diff:
	black picture_perfect --diff
	black tests --diff

build:
	docker build -f Dockerfile --tag picture-perfect:latest .

export-requirements:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

flake8:
	flake8 picture_perfect/ tests/ --statistics

pre-commit: black flake8 test build

run-container: build
	docker container run -p 8501:8501 -d picture-perfect:latest

run-server:
	streamlit run picture_perfect/app.py

test:
	pytest -vvs --cov-report term-missing --cov=picture_perfect tests/

_update:
	poetry update

update: _update export-requirements pre-commit

update-diff:
	poetry update --dry-run | grep -i updat
