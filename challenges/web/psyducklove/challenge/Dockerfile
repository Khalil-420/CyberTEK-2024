FROM python:3.8-slim-buster as chroot

RUN /usr/sbin/useradd --no-create-home -u 1000 user

COPY nsjail.cfg /home/user/nsjail.cfg

WORKDIR /home/user/app
COPY ./app .

RUN chmod +x /home/user/app/cleanup.sh
RUN chmod +x /home/user/app/start.sh
RUN chown -R user:user .
RUN chown -R root:user /home/user/app/static/imgs/internal/*.jpg
RUN chown -R root:user /home/user/app/static/imgs/internal/*.png

RUN pip install -r requirements.txt

RUN mv flag.txt /flag_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1`

FROM python:3.8-slim-buster as runtime

WORKDIR /home/user/

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

RUN /usr/sbin/useradd -u 1000 user \
    && chown -R user:user .
USER user

COPY --from=chroot / /chroot
ENTRYPOINT ["nsjail", "--config", "/chroot/home/user/nsjail.cfg", "--", "/home/user/app/start.sh"]
