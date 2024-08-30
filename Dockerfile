
ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-slim as base

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y python3-tk tcl tk

WORKDIR /app

COPY requirements.txt .

RUN apt-get update

RUN  pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python", "main.py"]
