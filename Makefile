run: webservice.py
	export WEBSERVICE_PORT
	python3 webservice.py

setup: requirements.txt
	pip install -r requirements.txt

test: unit_tests.py
	python3 unit_tests.py -v

clean:
	rm -rf __pycache__
