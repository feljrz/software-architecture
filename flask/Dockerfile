FROM python
RUN apt-get update && apt-get install python-pip -y && apt-get install python-dev -y 
WORKDIR /app
ADD . /app
ENV DATABASE_URL="postgresql://postgres:12345678@172.20.0.6:5432/students_db"\
    POSTGRES_PASSWORD="12345678"
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
