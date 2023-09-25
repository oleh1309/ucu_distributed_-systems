# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the local app files into the container
COPY Application.py /app/Application.py

# Install any needed packages specified in requirements.txt
RUN pip install Flask requests

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "Application.py"]
