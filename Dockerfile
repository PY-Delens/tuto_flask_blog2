FROM python:3.8

WORKDIR /app

RUN pip install poetry

ADD pyproject.toml poetry.lock hello.py hello2.py just.py /app/
ADD cabwill.db cabwill_1.py /app/

COPY helloblog.py schema.sql init_db.py database.db sqlite3 cabwill.db cabwill_1.py /app/
COPY static/ /app/static/
COPY templates/ /app/templates/

ADD test.txt /app/test.txt

RUN poetry install
RUN  ls -la /app/templates/*

RUN echo 1
RUN sleep 3

RUN echo hello world

# ENV FLASK_APP=hello:app  , not justwebsite1 either
# ENV FLASK_APP=helloblog:app
ENV FLASK_APP=cabwill_1:app


EXPOSE 80

CMD [ "/usr/local/bin/poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80" ]

