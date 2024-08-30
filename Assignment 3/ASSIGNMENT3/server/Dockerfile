# Dockerfile for server
FROM python:3.8-slim

# Create directory for server data
RUN mkdir /serverdata

# Set working directory
WORKDIR /app

# Copy server.py into the container
COPY server.py /app/

# Specify the command to run the server script
CMD ["python3", "server.py", "8080"]
