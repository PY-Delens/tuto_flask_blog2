FROM python:3.8

WORKDIR /app

RUN pip install poetry

ADD pyproject.toml poetry.lock hello.py hello2.py just.py projectsheet.txt /app/

RUN poetry install

# ENV FLASK_APP=hello:app
ENV FLASK_APP=justwebsite1:app

EXPOSE 80

CMD [ "/usr/local/bin/poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80" ]
