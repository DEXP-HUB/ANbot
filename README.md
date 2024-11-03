1) Выполнить git clone git@github.com:DEXP-HUB/ANbot.git
2) Создать виртуальное окружение python3 -m venv aiogram_venv 
3) Активировать виртуальное окружение source aiogram_venv/bin/activate
4) Установить все библиотеки pip install -r requarement.txt
5) Взять токен для бота у @BotFather (https://t.me/BotFather) в чате с @BotFather вводим /newbot
6) Полученный токен вставляем в параметр token класса Bot в файле dispatcher.py
7) Запускаем бота и тестируем его.

ЕСЛИ У ВАС WINDOWS ИЛИ MAC ВОЗМОЖНО ПРИДЁТСЯ ЗАЙТИ В Routers/category_beginner.py, Routers/category_participant.py, Routers/category_society.py, Routers/feed_back.py, dispatcher.py И ИЗМЕНИТЬ ТАМ СЛЭШИ В ФУНКЦИЯХ open В КОТОРЫХ УКАЗАН ПУТЬ К ФАЙЛАМ.
