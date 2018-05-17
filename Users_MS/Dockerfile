# Use an official Python runtime as a parent image
FROM python:3.6-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV DATABASEADDRESS 10.0.2.15:3306
ENV PYTHONPATH /app/
ENV EUREKA_SERVICE_URL 10.0.2.15:8761
ENV EUREKA_INSTANCE_PORT 5000

# Run app.py when the container launches
CMD ["python", "application.py"]
