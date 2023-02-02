### Hexlet tests and linter status:
[![Actions Status](https://github.com/Gas159/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Gas159/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/25bbcce7f38df198f52d/maintainability)](https://codeclimate.com/github/Gas159/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/25bbcce7f38df198f52d/test_coverage)](https://codeclimate.com/github/Gas159/python-project-52/test_coverage)
[![Linter](https://github.com/Gas159/python-project-52/actions/workflows/test.yml/badge.svg)](https://github.com/Gas159/python-project-52/actions/workflows/test.yml)
[![CI](https://github.com/Gas159/python-project-52/actions/workflows/test1.yml/badge.svg)](https://github.com/Gas159/python-project-52/actions/workflows/test1.yml)


# Task Manager
https://python-project-52-production-b3b8.up.railway.app/

_Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks._

A simple web application for task management. Implemented in the [Django 4.1.5](https://www.djangoproject.com/) framework using built-in class-based views (CBV) and a [PostgreSql](https://www.postgresql.org/) database. Website design - [Bootstrap v5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Demo
Just click and try to use **[DEMO on Railway](https://python-project-52-production-b3b8.up.railway.app/)**

<hr> <hr/>

## Installation
```
$ git clone https://github.com/Gas159/python-project-52.git
```

Go to the project folder:
```
$ cd python-project-52`
```

```
$ make setup
```
For details look Makefile
## Settings:
Create an ".env" file in the root project directory: 
```
$ touch .env 
```


оr rename and edit existing ".env.example" file.

Write following constants to the .env file:

1. `SECRET_KEY='your_Django_secret_key'` 

You can generate one with `make secretkey` command.

2. `DATABASE_URL='your_database_url_path'` 

To use simple sqlite database use this record: 

`DATABASE_URL='sqlite:///db.sqlite3'`

## Database preparation

`make migrations`

`make migrate`

`make createsuperuser`

## Start project

`make start`

Use this app in browser on http://localhost:8080
<hr/>
<hr>
