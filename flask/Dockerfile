FROM python:3.6-stretch
COPY . /app
WORKDIR /app

RUN pip install flask && \
    pip install SQLAlchemy && \
    pip install Flask-SQLAlchemy

EXPOSE 5000
ENTRYPOINT ["python"]

CMD ["main.py"]
