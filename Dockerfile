# Use the official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Copy the required files (bot_logs.log and users.db) into the container
COPY bot_logs.log .
COPY users.db .
COPY requirements.txt .
COPY .env .


# Expose the necessary port (if your bot listens on a specific port, otherwise remove)
EXPOSE 8000

# Command to run the bot
CMD ["python", "main.py"]
