FROM python:3.10-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]