# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install dependencies
RUN pip install --upgrade pip
RUN pip install --timeout=600 --retries=5 -r requirements.txt

# Step 5: Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=" 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"

# Step 6: Expose the port the app runs on (if it's a web server)
# EXPOSE 8000  # Uncomment if you're using a web server

# Step 7: Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
