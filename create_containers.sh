#!/bin/bash

# Delete containers
docker rm microservices_aggr_1
docker rm microservices_playlists_1
docker rm microservices_auth_1
docker rm microservices_users_1
docker rm microservices_songs_1
docker rm microservices_zuul_1
docker rm microservices_eureka_1

# Delete images
docker rmi users-ms
docker rmi songs-ms
docker rmi playlists-ms
docker rmi aggr-ms
docker rmi auth-ms
docker rmi eureka-server
docker rmi zuul-gateway

# Zuul
cd Zuul-Gateway
mvn clean
mvn install
docker build -t zuul-gateway .
cd ..

# Eureka
cd Eureka-Server
mvn clean
mvn install
docker build -t eureka-server .
cd ..

# Aggregator
cd Aggregator_MS
docker build -t aggr-ms .
cd ..

# Authentication
cd Authentication_MS
docker build -t auth-ms .
cd ..

# Playlists
cd Playlists_MS
docker build -t playlists-ms .
cd ..

# Songs
cd Songs_MS
docker build -t songs-ms .
cd ..

# Users
cd Users_MS
docker build -t users-ms .
cd ..



