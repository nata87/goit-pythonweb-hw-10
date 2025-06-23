# **Contacts API — Homework 10**

Цей проєкт — REST API для управління контактами з:
✅ Аутентифікацією
✅ Авторизацією через JWT
✅ Верифікацією email
✅ Обмеженням запитів (`Rate Limit` через Redis)
✅ Оновленням аватара через Cloudinary
✅ CORS увімкнено

---

## Запуск

**Склонуй репозиторій**

```bash
git clone https://github.com/твій-нік/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

**Створи `.env` на основі `.env_example`**

```bash
cp .env_example .env
```

**Заповни значення змінних:**

* `DATABASE_URL`
* `SECRET_KEY`
* `CLOUDINARY_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
* `MAIL_USERNAME`, `MAIL_PASSWORD` і т.д.
* `REDIS_HOST=localhost`
* `REDIS_PORT=6379`

**Запусти базу даних та Redis через Docker:**

```bash
docker-compose up -d
```

**Встанови залежності:**

```bash
pip install -r requirements.txt
```

**Запусти FastAPI:**

```bash
uvicorn main:app --reload
```

---

##  **Swagger & Redoc**

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) — інтерактивна OpenAPI-документація
* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) — зручна Redoc-документація
* [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) — JSON-файл опису API

---

## **Важливо**

**Всі операції з контактами доступні лише для авторизованих користувачів!**
Кожен користувач бачить тільки свої контакти.

Після реєстрації приходить лист для верифікації email (через FastAPI Mail).

Оновлення аватара працює через Cloudinary.

`/me` обмежено по Rate Limit

