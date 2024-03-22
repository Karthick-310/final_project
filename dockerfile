# FROM python:3.8.0
# WORKDIR /final_project
# COPY  . /final_project
# RUN /bin/sh -c pip intall -r requirements.txt
# EXPOSE 3000
# CMD python ./app.py

# Use an existing base image
FROM python:3.8.18-bullseye

# Set environment variables


# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
