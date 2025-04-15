FROM python:3.11.11

COPY python_requirements.txt /opt
RUN pip install -r /opt/python_requirements.txt 

RUN mkdir /app
COPY app.py /app 
WORKDIR /app