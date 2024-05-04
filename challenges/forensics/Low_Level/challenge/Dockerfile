FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -yq --no-install-recommends  \
    python3-pip  \
    socat  \
    gcc make golang libgmp3-dev libc-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app.py /app/

CMD socat \
      TCP-LISTEN:9001,reuseaddr,fork \
      EXEC:"python3 /app/app.py"
