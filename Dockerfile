FROM python:3.13

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

