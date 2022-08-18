FROM python

WORKDIR /app

RUN pip install discord.py

RUN pip install python-dotenv

COPY . .

CMD ["python", "main.py"]