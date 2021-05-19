FROM python:3.8

WORKDIR /app

RUN pip install poetry

ADD pyproject.toml poetry.lock hello.py hello2.py just.py projectsheet.txt /app/

COPY static/ /app/static/
COPY templates/ /app/templates/

RUN poetry install
RUN  ls -la /app/templates/*

# ENV FLASK_APP=hello:app  , not justwebsite1 either
ENV FLASK_APP=just:app

EXPOSE 80

CMD [ "/usr/local/bin/poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80" ]

