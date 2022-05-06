FROM python:3.10.4

WORKDIR /flaskapp
COPY . . 

RUN pip install -r requirements.txt
#RUN apt-get update -y
#RUN apt-get install vim -y


CMD ["python", "app.py"]
