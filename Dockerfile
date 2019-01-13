# Use an official Python runtime as a parent image
FROM python:3.7.1

# Set the working directory to /takugen
WORKDIR /takugen

# Copy the current directory contents into the container at /takugen
COPY . /takugen

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run main.py when the container launches
CMD ["python", "-u", "main.py"]
