FROM python:3.12-slim

WORKDIR /

COPY ../pyproject.toml ../poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root


COPY . .

CMD ["uvicorn", "cdn.main:cdn", "--host", "0.0.0.0", "--port", "9000"]