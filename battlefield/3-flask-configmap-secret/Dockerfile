FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Update packages and install Python dependencies
RUN apk update && apk upgrade \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Run Flask application
CMD ["python", "app.py"]