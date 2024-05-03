FROM python:3.9

RUN apt-get update && apt-get install -y socat

WORKDIR /app

COPY chall.py .
COPY Quotes1.txt .
COPY flag.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh
RUN pip install pycryptodome

EXPOSE 1337

CMD /bin/bash /app/entrypoint.sh