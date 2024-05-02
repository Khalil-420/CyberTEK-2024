FROM python:3.8-slim-buster as chroot

RUN /usr/sbin/useradd --no-create-home -u 1000 user

WORKDIR /home/user/app
COPY ./app .

RUN chmod +x /home/user/app/cleanup.sh
RUN chmod +x /home/user/app/start.sh
RUN chown -R user:user .
RUN chown -R root:user /home/user/app/static/imgs/internal/*.jpg
RUN chown -R root:user /home/user/app/static/imgs/internal/*.png

RUN pip install -r requirements.txt

RUN mv flag.txt /flag_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1`

CMD ["/bin/bash","/home/user/app/start.sh"]
