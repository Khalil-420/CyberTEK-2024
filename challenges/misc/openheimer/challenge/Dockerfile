FROM oowy/opentofu:latest
RUN apk add go socat
WORKDIR /app
COPY tofu .
COPY src ./challenge
COPY entrypoint.sh .
COPY openheimer.sh .
RUN chmod +x entrypoint.sh
RUN chmod +x openheimer.sh
ENV TF_VAR_SECRET="83;101;99;117;114;105;110;101;116;115;123;111;80;51;78;55;79;102;85;95;73;53;95;52;119;51;53;79;109;51;95;56;85;55;95;56;51;99;52;82;51;70;117;76;95;87;72;51;110;95;87;79;82;107;105;110;57;95;87;105;55;104;95;53;51;67;114;51;84;115;125"
RUN cd challenge && go mod init openheimer && go build
RUN cd /app && tofu init && tofu apply -auto-approve
EXPOSE 1337
ENTRYPOINT ["sh", "entrypoint.sh"]