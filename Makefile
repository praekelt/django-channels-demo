virtualenv: ./venv
	./venv/bin/pip install -r requirements.txt

./venv:
	virtualenv venv --always-copy --python=python3

run: virtualenv
	./venv/bin/python manage.py runserver
	# Alternatively the worker can be run independently, e.g.
	# python manage.py runserver --noworker
	# python manage.py runworker

tsung:
	tsung -k -f experiments/tsung_websocket.xml start
