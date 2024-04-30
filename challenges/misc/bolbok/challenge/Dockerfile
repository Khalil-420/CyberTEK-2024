FROM ubuntu:22.04 as chroot
RUN /usr/sbin/useradd --no-create-home -u 1001 bolbok
WORKDIR /home/bolbok
RUN mkdir -p /usr/share/misc/bolbok/secrets/youwillneverfindthis/
COPY exec.sh /
COPY  flag.txt /usr/share/misc/bolbok/secrets/youwillneverfindthis/.flag
RUN chmod +x /exec.sh

FROM disconnect3d/nsjail:3.1-6483728
RUN apt update -y \ 
    && apt install socat -y
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
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"nsjail --port 1337 --config /home/bolbok/nsjail.cfg -- /exec.sh\""]