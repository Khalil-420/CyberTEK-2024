FROM pwn.red/jail
COPY --from=ubuntu@sha256:5a828e28de105c3d7821c4442f0f5d1c52dc16acf4999d5f31a3bc0f03f06edd / /srv
COPY main /srv/app/run
COPY flag.txt /srv/app/
ENV JAIL_POW=0 JAIL_PORT=1337 JAIL_TIME=50

WORKDIR /srv/app
RUN chmod +x run