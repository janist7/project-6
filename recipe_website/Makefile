.PHONY: init clean celery assets server db

init:
	pip3 install -r requirements.txt

clean:
	find . -name '*.pyc' -delete

celery:
	python3 runcelery.py -A app.tasks worker

assets:
	cd app/static && bower --allow-root install && cd ..

server:
	python3 manage.py runserver --host 0.0.0.0

db:
	python3 manage.py recreate_db
