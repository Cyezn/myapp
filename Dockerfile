# Use Python base image
FROM python:3.11-slim

# Set display environment variable (for GUI support)
ENV DISPLAY=:0

# Install GUI dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all source files into the container
COPY . /app

# Install Python dependencies (if any, else skip this line)
# RUN pip install -r requirements.txt

# Run the GUI app
CMD ["python3", "gui.py"]
