FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the file into the container
COPY dummy_site/app.py .

# Explicitly tell Flask where the app file is
ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]