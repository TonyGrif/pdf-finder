FROM python:3.12-slim

COPY pyproject.toml .
COPY poetry.lock .
COPY finder/ finder/

RUN pip install "poetry>=1.8,<2.0"
RUN poetry install --only main

ENTRYPOINT [ "poetry", "run", "python", "__main__.py" ]
