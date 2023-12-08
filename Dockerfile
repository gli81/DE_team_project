FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505

WORKDIR /code/server

ENTRYPOINT ["gunicorn", "server:app"]