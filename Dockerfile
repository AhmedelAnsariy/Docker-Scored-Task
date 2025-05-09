# ---------- Stage 1: Build ---------- 
FROM python:3.11-slim as builder

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# ---------- Stage 2: Final ---------- 
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy only the application code
COPY app ./app

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
