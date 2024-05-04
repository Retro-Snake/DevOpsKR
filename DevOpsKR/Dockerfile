# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app
COPY requirements.txt .
# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install Flask requests

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Run app.py when the container launches
CMD ["python", "main.py"]