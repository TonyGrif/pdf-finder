FROM python:3.11-slim

COPY pyproject.toml .
COPY poetry.lock .
COPY finder/ finder/
COPY main.py .

RUN pip install poetry
RUN poetry install --only main

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]
