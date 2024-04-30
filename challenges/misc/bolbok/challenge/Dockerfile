FROM ubuntu:rolling as chroot

RUN /usr/sbin/useradd --no-create-home -u 1001 bolbok

WORKDIR /home/bolbok

RUN mkdir -p /usr/share/misc/bolbok/secrets/youwillneverfindthis/

# COPIES
COPY exec.sh /
COPY  flag.txt /usr/share/misc/bolbok/secrets/youwillneverfindthis/.flag

RUN chmod +x /exec.sh

#nsjail
FROM disconnect3d/nsjail:3.1-6483728

#install packages
RUN apt update -y \ 
    && apt install socat -y

#Copies
COPY --from=chroot / /chroot
COPY nsjail.cfg /home/bolbok/

RUN cd /chroot/dev && \
  touch null zero urandom random full

RUN mkdir -p /usr/bolbok/cmds/

RUN ln -s /usr/bin/ls /usr/bolbok/cmds/ \
    && ln -s /usr/bin/top /usr/bolbok/cmds/ \
    && ln -s /usr/bin/uptime /usr/bolbok/cmds/ \
    && ln -s /usr/bin/grep /usr/bolbok/cmds/ \
    && ln -s /usr/bin/rbash /usr/bolbok/cmds/rbash

CMD ["socat", "TCP-LISTEN:22222,reuseaddr,fork", "EXEC:\"nsjail --port 22222 --config /home/bolbok/nsjail.cfg -- /exec.sh\""]