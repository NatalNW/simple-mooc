.PHONY: install format lint test sec migrate runserver
install:
	poetry install
	poetry shell
format:
	isort .
	blue .
lint:
	prospector --with-tool pep257 --doc-warning

# test:
sec:
	pip-audit
migrate:
	python manage.py makemigrations
	python manage.py migrate
runserver:
	python manage.py runserver 0.0.0.0:8000