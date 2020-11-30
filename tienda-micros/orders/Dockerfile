FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 7000
CMD [ "python", "application.py" ]
