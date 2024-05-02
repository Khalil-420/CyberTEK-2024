FROM eqalpha/keydb:latest as chroot

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y \ 
    && apt install golang-go socat -y
WORKDIR /home/ctf

COPY ynetd /home/ctf/
COPY *.sh /home/ctf/
COPY src /home/ctf/challenge

RUN chmod +x /home/ctf/*
RUN /usr/sbin/useradd -u 1337 ctf \
    && chown -R ctf:ctf .
USER ctf
RUN cd /home/ctf/challenge && go mod init siclodb && go build

FROM eqalpha/keydb:latest as runtime 
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install -y \
    autoconf \
    bison \
    flex \
    gcc \
    g++ \
    git \
    libprotobuf-dev \
    libnl-route-3-dev \
    libtool \
    make \
    pkg-config \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/google/nsjail.git /nsjail \
    && cd /nsjail \
    && make \
    && mv /nsjail/nsjail /usr/bin \
    && rm -rf /nsjail \
    && apt-get autoremove -y \
    && apt-get remove --purge -y  \
    autoconf \
    bison \
    flex \
    gcc \
    g++ \
    git \
    libprotobuf-dev \
    libnl-route-3-dev \
    libtool \
    make \
    pkg-config \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

COPY --from=chroot / /chroot
RUN /usr/sbin/useradd -u 1337 ctf
COPY nsjail.cfg /
USER ctf
ENTRYPOINT ["nsjail", "--config", "/nsjail.cfg","--", "/home/ctf/entrypoint.sh"]
