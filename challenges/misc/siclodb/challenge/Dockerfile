FROM eqalpha/keydb:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y \ 
    && apt install golang-go socat -y
WORKDIR /home/ctf
RUN useradd ctf
USER ctf
COPY bin/main *.sh ./
ENTRYPOINT ["sh", "entrypoint.sh"]