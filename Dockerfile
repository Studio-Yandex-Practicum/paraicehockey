FROM python:3.10-slim

RUN mkdir /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry && curl -sSL 'https://install.python-poetry.org' | python3 - 

WORKDIR /app

ENV PYTHONPATH="$PYTHONPATH:/app"

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app

CMD ["python3", "./bin/run_bot.py"]