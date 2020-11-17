black:
	black picture_perfect
	black tests

black-diff:
	black picture_perfect --diff
	black tests --diff

export:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

pre-commit: black test

test:
	pytest -vvs --cov-report term-missing --cov=picture_perfect tests/

_update:
	poetry update

update: _update export pre-commit

update-diff:
	poetry update --dry-run | grep -i updat
