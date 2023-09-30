FROM python:3.11

ENV DJANGO_SETTINGS_MODULE=course_project.settings
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
