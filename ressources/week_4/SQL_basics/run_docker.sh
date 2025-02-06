#! /bin/bash

docker build -t my-alpine-sqlite .

docker run -d --name sqlite3_ctn my-alpine-sqlite

docker exec -it sqlite3_ctn sh

docker run -d --name my-sqlite3_ctn -v "$(pwd)/flights.sql:/data/flights.sql" my-alpine-sqlite


