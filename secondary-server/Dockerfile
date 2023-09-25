# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the local app files into the container
COPY Secondary.py /app/Secondary.py

# Install any needed packages specified in requirements.txt
RUN pip install Flask

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run secondary_server.py when the container launches
CMD ["python", "Secondary.py"]
