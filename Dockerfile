# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /bookstore

# Install dependencies 
COPY requirements.txt /bookstore/
RUN pip install -r requirements.txt

# Copy project
COPY . /bookstore/