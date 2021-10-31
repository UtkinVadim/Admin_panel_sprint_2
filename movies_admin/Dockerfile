FROM python:3.9.7-alpine
WORKDIR /app

RUN apk update
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev linux-headers libffi-dev jpeg-dev zlib-dev

COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir "static"

COPY . .

RUN addgroup -S movies_user && \
    adduser -S -H -G movies_user movies_user && \
    chown -R movies_user:movies_user /app

USER movies_user

CMD ["gunicorn", "config.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]