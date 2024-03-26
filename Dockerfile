# Use official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Add standard labels
LABEL maintainer="Joshua Clarke and Antony Bailey <antony.bailey@thepoliceoftheinter.net>"
LABEL description="This is a Docker image for the Hammy McHamilton Discord Bot."
LABEL org.opencontainers.image.created="$BUILD_DATE" 
# docker build --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') -t hammy-mchamilton .

# Run main.py when the container launches
CMD ["python", "main.py"]
