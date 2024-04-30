FROM python:3.9

RUN apt-get update && apt-get install -y socat

WORKDIR /app

COPY chall.py .

COPY Quotes1.txt .

COPY flag.txt .


RUN pip install pycryptodome


EXPOSE 8001


COPY entrypoint.sh .


RUN chmod +x entrypoint.sh


ENTRYPOINT ["./entrypoint.sh"]