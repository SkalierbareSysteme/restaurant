FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    postgresql-client

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8005

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8005
