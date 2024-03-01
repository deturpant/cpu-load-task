# ***CPU Load microservice***
Данный микросервис написан на aiohttp фреймворке. Позволяет получить информацию о загрузке процессора за последний час. Кажджые 5 секунд делает запись в базе данных, записывая загрузку процессора в данный момент.
Предоставляет следующую информацию:
1) Записи о загрузке процессора за последний час.
2) Записи о загрузке процессора (усредненно) по минутам.
3) Записи о выключениях сервиса.

## Развертывание
Прежде всего необходимо создать конфигурационный файл "conf.yaml" в директории config. Там необходимо указать данные для подключения к БД, порт приложения. Пример заполненного конфига находится там же.

Для запуска приложения необходимо установить все зависимости, содержащиеся в файле requirements.txt, после чего командой python main.py запустить приложение.

Приложение можно запустить в докер-контейнере. В репозитории находится Dockerfile, можно собрать образ на базе этого файла ("docker build -t <название образа> ."), после чего запустить командой "docker run -d --name <название контейнера> -p <port входной>:<порт внутренний> <название образа>"

## Демонстрация
Для примера приложение было развернуто на сервере. Для показа визуальной части был создан веб-интерфейс, доступный по адресу: https://cpu-load.deturpant.ru/
![image](https://github.com/deturpant/cpu-load-task/assets/73655932/a8d7500c-b825-434f-a34b-b00c695e9910)
![image](https://github.com/deturpant/cpu-load-task/assets/73655932/1cb65466-16b5-4631-96d4-bb0748899381)

Пример графиков с остановкой сервиса:
![image](https://github.com/deturpant/cpu-load-task/assets/73655932/acf49aff-8f8b-4157-8a08-f0ecf0915167)
![image](https://github.com/deturpant/cpu-load-task/assets/73655932/e1dd6faf-e0ce-426d-ab4a-ab6de6602dc9)