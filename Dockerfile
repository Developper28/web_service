FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "make", "run"]

# docker build --tag webservice . 
# docker run --publish 5000:8080 webservice
