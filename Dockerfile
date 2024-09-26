FROM python:3.12.2-slim-bookworm

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-server-dev-all

WORKDIR /app

COPY requirements.txt main.py ./
COPY src ./src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]