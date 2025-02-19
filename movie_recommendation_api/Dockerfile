# versi python
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy file requirements
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# copy all files
COPY . /app

# running API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]