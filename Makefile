LOCAL := poetry run python3 manage.py

install:
		poetry install


start:
		$(LOCAL) runserver 8080

run-gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi --log-file


# service commands
shell:
		$(LOCAL) shell_plus

collectstatic:
		$(LOCAL) collectstatic

secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

createsuperuser:
	python manage.py createsuperuser

export:
# 	poetry export -f requirements.txt -o requirements.txt
	poetry export --without-hashes --format=requirements.txt > requirements.txt


# make translate messages commands
messages:
		django-admin makemessages --ignore="static" --ignore=".env" --ignore="venv" -l ru
mes1:
		django-admin makemessages --ignore="static" --ignore=".env" --ignore="venv"  -a #update all
compilemess:
		django-admin compilemessages



# migrate commands
migrat:
		$(LOCAL) makemigrations
		$(LOCAL) migrate


migrations:
		$(LOCAL) makemigrations
migrate:
		$(LOCAL) migrate


test:
	$(LOCAL) test
# test1:
# 	$(LOCAL) test --with-coverage --cover-xml

test-cov:
	poetry run coverage run ./manage.py test
	poetry run coverage xml


# linter & check commands1
lint:
		poetry run flake8 task_manager users tasks labels statuses


# complex commands
check:
	poetry check
	echo  '!!!!!!!!!!!'
	poetry run flake8 task_manager users tasks labels statuses
	$(LOCAL) test


build: check
		poetry build

lang_check:
		curl http://127.0.0.1:8080 -H "Accept-Language: ru"


PORT ?= 8000
db:
	poetry shell
	python3 manage.py migrate
	poetry run gunicorn -w 3 --bind 0.0.0.0:$(PORT) task_manager.wsgi

setup:
	poetry install
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi
mig:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

.PHONY: install test lint selfcheck check build shell migrate collectstatic secretkey bla
