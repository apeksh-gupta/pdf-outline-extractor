FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY main.py .

RUN mkdir -p /app/input /app/output && chmod -R 755 /app/input /app/output

CMD ["python", "main.py"]
