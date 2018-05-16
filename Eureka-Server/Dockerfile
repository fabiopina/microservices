# Use an official Java runtime as a parent image
FROM openjdk:8-jdk-alpine

# Make port 80 available to the world outside this container
EXPOSE 80

ADD /target/EurekaServer.jar EurekaServer.jar

ENTRYPOINT ["java","-jar","EurekaServer.jar"]
