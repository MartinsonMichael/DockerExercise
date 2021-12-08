# Define base image
FROM python:3.8.5

# Install requirements inside docker
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the main code
COPY server.py .

# Define entrypoint - command to run on start
ENTRYPOINT python3 server.py