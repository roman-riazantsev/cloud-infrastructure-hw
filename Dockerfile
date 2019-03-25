FROM python:3.6

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "Mersenne.py"]
