FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pulp padding pandas

COPY . .

ENTRYPOINT ["python", "src/main.py"]