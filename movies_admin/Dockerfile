FROM python:3.8-alpine
WORKDIR /app

RUN apk update
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev linux-headers libffi-dev jpeg-dev zlib-dev

COPY requirements/requirements.txt .
RUN pip install -r requirements.txt

RUN addgroup -S movies_user
RUN adduser -S -H -G movies_user movies_user

COPY . .
RUN chown -R movies_user:movies_user /app

USER movies_user