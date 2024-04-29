FROM oowy/opentofu:latest

RUN apk add go socat

WORKDIR /home/ctf

RUN adduser -D ctf

USER ctf

ENV TF_VAR_SECRET="SECRET"

COPY tofu bin/main *.sh ./

RUN tofu init && tofu apply -auto-approve

EXPOSE 13337

ENTRYPOINT ["sh", "entrypoint.sh"]