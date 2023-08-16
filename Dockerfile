FROM python:3.9

WORKDIR /code

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py collectstatic

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD gunicorn coffe_test.wsgi:application --bind 0.0.0.0:8000
