FROM python:3

COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /var/app/src

RUN git clone https://github.com/szazo/DHT11_Python.git

COPY src /var/app/src

CMD ["python", "./main.py"]
