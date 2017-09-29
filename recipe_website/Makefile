.PHONY: init clean celery assets server db

init:
	pip2 install -r requirements.txt

clean:
	find . -name '*.pyc' -delete

celery:
	python2 runcelery.py -A app.tasks worker

assets:
	cd app/static && bower --allow-root install && cd ..

server:
	python2 manage.py runserver --host 0.0.0.0

db:
	python2 manage.py recreate_db
