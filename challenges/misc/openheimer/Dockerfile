FROM oowy/opentofu:latest

RUN apk add go socat

WORKDIR /home/ctf

RUN adduser -D ctf

USER ctf

ENV TF_VAR_SECRET="Securinets{aLl_7h3_wAYS_l3Ad5_70_0n3_s3CR37}"

COPY tofu bin/main *.sh ./

RUN tofu init && tofu apply -auto-approve

ENTRYPOINT ["sh", "entrypoint.sh"]