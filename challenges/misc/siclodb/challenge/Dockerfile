FROM ubuntu:22.04 as chroot

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt install wget curl git gcc -y \
    && apt install -y software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && apt install software-properties-common -y 
RUN echo "deb http://security.ubuntu.com/ubuntu focal-security main" | tee /etc/apt/sources.list.d/focal-security.list
RUN curl -s --compressed "https://download.keydb.dev/keydb-ppa/KEY.gpg" | apt-key add -
RUN curl -s --compressed -o /etc/apt/sources.list.d/keydb.list https://download.keydb.dev/keydb-ppa/keydb.list
RUN apt-get update -y
RUN apt-get install libssl1.1
RUN apt install keydb-tools -y
RUN echo "deb https://download.keydb.dev/open-source-dist $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/keydb.list
RUN wget -O /etc/apt/trusted.gpg.d/keydb.gpg https://download.keydb.dev/open-source-dist/keyring.gpg
RUN add-apt-repository ppa:longsleep/golang-backports &&\
    add-apt-repository ppa:eqalpha/keydb-server &&\
    apt install golang-go -y


WORKDIR /home/ctf
COPY ynetd .
COPY entrypoint.sh .
COPY keydb.sh .
COPY setkeys.sh .
COPY src ./challenge
RUN chmod +x /home/ctf/*.sh
RUN chmod +x /home/ctf/ynetd
RUN /usr/sbin/useradd -u 1337 ctf \
    && chown -R ctf:ctf .
USER ctf
RUN cd /home/ctf/challenge && go mod init siclodb && go build
WORKDIR /home/ctf
EXPOSE 1337

FROM ubuntu:22.04 as runtime 

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
USER ctf
COPY nsjail.cfg /
ENTRYPOINT ["nsjail", "--config", "/nsjail.cfg","--", "/home/ctf/entrypoint.sh"]
