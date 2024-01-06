FROM python:3.12.1
RUN mkdir /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
