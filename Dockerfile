# Fayvad Digital - Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        postgresql-client \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY fayvad_digital/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy project
COPY . /app/

# Create directories for static, media and logs
RUN mkdir -p /app/static /app/media /app/logs && \
    useradd --create-home fayvad && \
    chown -R fayvad:fayvad /app

# Expose port
EXPOSE 8000