# web service


## Quick set up
Clone the project and run the following commands:
```
make setup
make run
```
`make setup` will install the required packages to run the web service application.
`make run` will start the web service on the default port 8080.

To test the web service, please use the browser to open the url [http://localhost:8080](http://localhost:8080). Alternatively, `curl` or `Postman` could be used to query the service instead of the browser.

To run the application on a different port (e.g. 5000), use the following command:
```
python3 webservice.py -p 5000
```

Or using the Makefile:
```
make WEBSERVICE_PORT=5000 run
```

To execute the test suite, execute the following command:

```
python3 unit_tests.py
```
Or using the Makefile:
```
make test
```

To clean the project, run `make clean`
