FROM python:3.11-slim
LABEL maintainer="NotLawson"

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV DOCKER=true

# Run the application
ENTRYPOINT [ "python3 main.py" ]
