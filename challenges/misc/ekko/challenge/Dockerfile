FROM python:3.8-slim-buster as chroot

RUN /usr/sbin/useradd -M -u 1000 ekko

COPY nsjail.cfg /home/ekko/nsjail.cfg

WORKDIR /home/ekko/app

COPY app/requirements.txt app/start.sh app/main.py ./

COPY app/.git .git

RUN chmod +x /home/ekko/app/start.sh

RUN pip install -r requirements.txt



FROM python:3.8-slim-buster as runtime

WORKDIR /home/ekko/

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

RUN /usr/sbin/useradd -u 1000 ekko \
    && chown -R ekko:ekko .

USER ekko

COPY --from=chroot / /chroot

ENTRYPOINT ["nsjail", "--config", "/chroot/home/ekko/nsjail.cfg", "--", "/home/ekko/app/start.sh"]