FROM python:3.10-slim

# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 
 
# Copy the requirements file first (better caching)
COPY requirements.txt /app/
 
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
