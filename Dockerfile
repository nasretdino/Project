FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry && \
    poetry --version

COPY pyproject.toml poetry.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY src/ ./src/

EXPOSE 8000

CMD ["python", "src/main.py"]