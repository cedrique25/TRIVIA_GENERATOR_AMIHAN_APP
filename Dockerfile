FROM python:3.10.4

WORKDIR /trivia-page
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./flaskapp ./flaskapplication

CMD ["python", "./flaskapp/app.py"]
