
FROM python:3.11-slim

WORKDIR /app_dir

COPY requirements.txt /app_dir/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app_dir/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
