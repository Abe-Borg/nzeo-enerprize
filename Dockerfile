FROM python:3.12.1
WORKDIR /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput
CMD gunicorn nzeo-enerprize.wsgi:application --bind 0.0.0.0:$PORT
