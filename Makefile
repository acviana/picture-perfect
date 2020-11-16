black:
	black picture_perfect
	black tests

black-diff:
	black picture_perfect --diff
	black tests --diff

test:
	pytest -vvs --cov-report term-missing --cov=picture_perfect tests/
