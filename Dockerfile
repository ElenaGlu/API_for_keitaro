FROM python:3.12

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /code
WORKDIR code/

RUN python -m pip install --upgrade pip
RUN pip install --upgrade poetry && poetry --version
RUN poetry install

WORKDIR app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]