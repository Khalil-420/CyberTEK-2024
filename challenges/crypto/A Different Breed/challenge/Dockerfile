FROM python:3.9

RUN apt-get update && apt-get install -y socat

WORKDIR /app

COPY task.py .

COPY Quotes1.txt .

COPY flag.txt .


RUN pip install pycryptodome


EXPOSE 12345


COPY entrypoint.sh .


RUN chmod +x entrypoint.sh


ENTRYPOINT ["./entrypoint.sh"]