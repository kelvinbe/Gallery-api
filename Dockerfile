FROM python:3.6.9


COPY requirements.txt requirements.txt


WORKDIR /app


COPY . .


RUN pip install -r requirements.txt


CMD ['python', 'app.py']