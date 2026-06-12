# Use official slim Python runtime
FROM python:3.11-slim

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for audio decoding (ffmpeg, libsndfile) and Git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set local working directory inside the container
WORKDIR /workspace

# Copy dependency definition file
COPY requirements.txt .

# Install pinned packages and jupyter
RUN pip install --no-cache-dir -r requirements.txt

# Expose standard Jupyter Notebook port
EXPOSE 8888

# Command to boot Jupyter Notebook with token security disabled for local developer ease
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
