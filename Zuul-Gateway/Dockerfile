# Use an official Java runtime as a parent image
FROM openjdk:8-jdk-alpine

# Make port 80 available to the world outside this container
EXPOSE 80

ADD /target/ZuulGateway.jar ZuulGateway.jar

# Define environment variable
ENV PORT 4000
ENV LOGSERVERADDRESS 10.0.2.15:4040
ENV EUREKA 10.0.2.15:8761

ENTRYPOINT ["java","-jar","ZuulGateway.jar"]
