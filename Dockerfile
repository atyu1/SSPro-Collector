FROM python:3

WORKDIR /var/app

COPY src .

ADD https://github.com/szazo/DHT11_Python.git sensors/

RUN pip install -r src/requirements.txt

CMD [python3 /var/app/main.py]
