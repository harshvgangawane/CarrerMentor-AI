
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the app
CMD ["flask", "run"]
