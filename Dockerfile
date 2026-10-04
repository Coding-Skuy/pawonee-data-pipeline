FROM python:3.12.7-slim-bookworm
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY config ./config
CMD ["python", "src/pipeline.py", "--sekali"]
