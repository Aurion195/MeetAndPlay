FROM python:3.7

COPY . /web
WORKDIR /web/src
RUN pip install -r ./requirements.txt

CMD ["python","server.py"]