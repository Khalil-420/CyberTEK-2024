FROM alpine:latest AS first
WORKDIR /home/heimer
RUN mkdir -p personal/images
COPY 01946.jpg personal/images/

FROM alpine:latest AS second
COPY ae98f70d /tmp
COPY f087c9d6s /etc/secrets/

FROM alpine:latest
WORKDIR /home/heimer
RUN adduser -D heimer
COPY fr49u0cas .fr49u0cas
COPY --from=first /home/heimer/ .
COPY --from=second /tmp /tmp
COPY --from=second /etc/secrets /etc/secrets
RUN rm -rf /tmp \
	&& rm -rf /etc/secrets \
	&& rm -rf /home/heimer

