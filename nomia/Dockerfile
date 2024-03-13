FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn

EXPOSE 8000

CMD ["python", "manage.py", "migrate", "--noinput"]
CMD ["gunicorn", "nomia.wsgi:application", "--bind", "0:8000"]
