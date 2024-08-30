# Use the official Python 3.8 slim image as base
FROM python:3.8-slim

# Create a directory for storing client data inside the container
RUN mkdir /clientdata

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the client.py script from the host into the container's /app directory
COPY client.py /app/

# Define the command to run the client script when the container starts
CMD ["python3", "-u", "client.py", "server", "8080"]
