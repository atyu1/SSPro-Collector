FROM python:3

WORKDIR /var/app

COPY src .

RUN git clone https://github.com/szazo/DHT11_Python.git

#RUN pip install -r src/requirements.txt

CMD ["python /var/app/main.py"]
