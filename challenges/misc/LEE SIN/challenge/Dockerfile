FROM python:3.9-slim

WORKDIR /app

COPY ./bot.py /app/bot.py

ENV FLAG="Securinets{i_see_all}"

RUN pip install discord.py

CMD ["python", "bot.py"]