# <img src="https://img.freepik.com/premium-photo/isolated-planet-globe_13339-192196.jpg?w=1060" width="89"/> place_in_space


### Platform for publishing free and paid content

Backend-приложение на **Django** для публикации контента с поддержкой бесплатных и платных публикаций.

Проект демонстрирует реализацию пользовательской регистрации, доступа к платному контенту, подписок, платежей через Stripe и фоновых задач с использованием Celery.

---

## ✨ Features

* user registration and authentication;
* publishing and managing content;
* free and paid publications;
* access control for paid content;
* one-time subscription payments;
* Stripe integration;
* PostgreSQL database;
* background task processing with Celery;
* scheduled tasks with Celery Beat;
* Redis as a message broker;
* Django Admin;
* Docker-based development environment;
* forms, permissions and tests.

---

## 🏗️ Project Structure

```text
place_in_space_1.0/
├── app_main_page/
├── app_publications/
├── app_subscriptions/
├── config/
├── users/
├── media/
├── static/
├── Dockerfile
├── docker-compose.yaml
├── manage.py
├── requirements.txt
└── .env.sample
```

### `app_main_page`

Основная логика главной страницы приложения.

### `app_publications`

Работа с публикациями и контентом.

Публикации могут быть бесплатными или доступны только пользователям, имеющим оплаченный доступ.

### `app_subscriptions`

Логика подписок и оплаты доступа к платному контенту.

В приложении также находятся фоновые задачи Celery.

### `users`

Регистрация, авторизация и работа с пользователями.

### `config`

Основная конфигурация Django-проекта, включая настройки Celery.

---

## 🔐 Authentication & Permissions

Доступ к различным частям приложения зависит от типа контента и состояния пользователя.

Бесплатные публикации доступны без авторизации, а платный контент — только авторизованным пользователям с соответствующим доступом.

Для ограничения доступа используются Django permissions и проверки состояния пользователя.

---

## 💳 Stripe Integration

Для реализации платного доступа используется **Stripe**.

Основной сценарий:

```text
User
  │
  ▼
Select paid content
  │
  ▼
Payment via Stripe
  │
  ▼
Subscription / access
  │
  ▼
Paid content becomes available
```

---

## ⚙️ Background Tasks

Для выполнения фоновых и периодических задач используется связка:

```text
Django
   │
   ▼
Celery
   │
   ├── Redis
   │
   └── Celery Beat
```

**Celery** отвечает за выполнение фоновых задач, а **Celery Beat** — за их планирование.

Redis используется как брокер сообщений.

---

## 🐳 Docker

Проект содержит Docker-конфигурацию для запуска основных компонентов приложения.

Docker Compose объединяет:

* Django application;
* PostgreSQL;
* Redis;
* Celery worker;
* Celery Beat.

Это позволяет запускать backend и необходимые инфраструктурные сервисы как единую среду разработки.

---

## 🗄️ Data & Backend

Основной стек backend:

* **Python**
* **Django**
* **PostgreSQL**
* **Django ORM**
* **Celery**
* **Redis**
* **Stripe**

Для инфраструктуры:

* **Docker**
* **Docker Compose**

---

## 🧩 Application Architecture

Основные компоненты приложения разделены по зонам ответственности:

```text
Users
  │
  ├───────────────┐
  ▼               ▼
Publications    Subscriptions
  │               │
  │               ▼
  │             Stripe
  │
  ▼
Access control
  │
  ▼
Paid content
```

Фоновые операции выносятся из основного request/response цикла в Celery.

---

## 🎯 Project Purpose

Проект был создан для практики разработки backend-приложений на Django и объединения нескольких технологий в одном проекте.

Основные задачи:

* проектирование Django-приложения;
* работа с моделями и Django ORM;
* реализация пользовательской аутентификации;
* управление правами доступа;
* создание платного контента;
* интеграция внешнего платёжного сервиса;
* работа с PostgreSQL;
* выполнение фоновых задач;
* планирование периодических задач;
* контейнеризация приложения.

---

## 📚 What I Practiced

В проекте я отработала:

* Django project structure;
* Django models and ORM;
* authentication;
* permissions;
* forms;
* PostgreSQL;
* Stripe API integration;
* Celery;
* Celery Beat;
* Redis;
* Docker;
* Django Admin;
* testing;
* PEP 8.

---

## 🚀 Development Path

Этот проект является частью моего развития в backend-разработке.

Здесь я перешла от базовой работы с Django и REST API к более комплексной backend-задаче, включающей платежи, управление доступом, фоновые процессы и инфраструктуру.

Дальше backend-направление продолжилось через **Node.js, Express и MongoDB**, а сейчас развивается в full-stack проектах на современном стеке:

**Angular · TypeScript · NestJS · PostgreSQL · Prisma · Docker**

---

## 👩‍💻 Author

**Фокс**

Web Engineer · Frontend Developer → Full-stack
