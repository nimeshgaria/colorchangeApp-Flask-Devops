FROM python:3.9-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r app/requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn","-b", "0.0.0.0:5000","app:app"]