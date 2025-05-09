# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Final ----------
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
