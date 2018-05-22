FROM python:3

#MAINTAINER

EXPOSE 5000

WORKDIR /app

ENV FLASK_APP cocktail.py
CMD [ "flask", "run", "-h", "::" ]

COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
