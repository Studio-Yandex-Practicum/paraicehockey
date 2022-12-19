FROM python:3.10-slim

RUN mkdir /app

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry install

WORKDIR /app

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app

CMD ["python3", "main.py"]