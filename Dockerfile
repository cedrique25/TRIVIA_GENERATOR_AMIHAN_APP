FROM python:3.10.4

WORKDIR /trivia-page
RUN pip install -r requirements.txt

COPY ..

CMD ["python", "./flaskapp/app.py"]
