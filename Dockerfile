FROM python:3.12

WORKDIR /app
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]