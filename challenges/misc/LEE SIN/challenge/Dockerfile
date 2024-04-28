FROM python:3.9-slim

WORKDIR /app

COPY ./bot.py /app/bot.py

RUN pip install discord.py

CMD ["python", "bot.py"]
