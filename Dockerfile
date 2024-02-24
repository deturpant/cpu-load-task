FROM python:3.7

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копирование вашего приложения в контейнер
COPY . /app

# Определение команды для запуска вашего приложения
CMD ["python", "main.py"]
