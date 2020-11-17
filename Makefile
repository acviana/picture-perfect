black:
	black picture_perfect
	black tests

black-diff:
	black picture_perfect --diff
	black tests --diff

pre-commit: black test

test:
	pytest -vvs --cov-report term-missing --cov=picture_perfect tests/
