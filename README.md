'''
# TechAI — Сайт о технологиях искусственного интеллекта

Это учебный проект на Django, посвящённый теме искусственного интеллекта.  
Сайт включает несколько страниц и реализован с использованием Bootstrap для адаптивного дизайна.

## 🧩 Функционал

- Главная страница
- Новости ИИ
- Контакты
- О сайте

## 🛠️ Технологии

- Python 3
- Django 4+
- Bootstrap 5
- HTML / CSS

## 📁 Структура проекта

```
ai_tech/
├── ai_tech/              # Настройки проекта
├── pages/                # Приложение с шаблонами и представлениями
│   ├── templates/        # Шаблоны сайта
│   │   └── pages/
│   │       └── includes/ # menu.html, footer.html
│   ├── static/           # Стили, изображения
│   ├── views.py          # Представления
│   └── urls.py           # Маршруты
├── manage.py
└── db.sqlite3
```

## 🧾 Клонирование проекта

Чтобы склонировать проект к себе локально, выполните следующую команду в терминале:

```
git clone https://github.com/CHEPURNOV-S-S/DJ02.git
cd DJ02
```


## 🚀 Установка и запуск

1. Создайте venv и установите зависимости:

```Powershell
python.exe -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Перейдите в папку проекта:
```Powershell
cd DJ02
```

3. Примените миграции:
```
python manage.py migrate
```

3. Запустите сервер:
```
python manage.py runserver
```

4. Откройте в браузере: [http://localhost:8000](http://localhost:8000)
'''