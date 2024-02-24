FROM python:3.7

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENV TZ=Europe/Moscow
COPY . /app

CMD ["python", "main.py"]
