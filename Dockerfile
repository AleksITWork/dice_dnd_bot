FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs

RUN useradd -m bot_user && chown -R bot_user:bot_user /app
USER bot_user

CMD ["python", "main.py"]