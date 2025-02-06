FROM alpine:latest

RUN apk update && apk upgrade

RUN apk add --no-cache sqlite bash

CMD ["tail", "-f", "/dev/null"]
