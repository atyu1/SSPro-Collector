FROM python:3

COPY requirements.txt

RUN pip3 install -requirements.txt

WORKDIR /var/app

COPY src .

RUN git clone https://github.com/szazo/DHT11_Python.git

CMD ["python /var/app/main.py"]
