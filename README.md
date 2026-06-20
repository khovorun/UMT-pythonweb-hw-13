# Contacts API

REST API for managing contacts built with FastAPI, PostgreSQL, Redis, Docker, JWT authentication, and Sphinx documentation.

## Features

* User registration and login
* JWT authentication
* Email confirmation
* Password reset via token
* User roles (user/admin)
* Contact management (CRUD)
* Search contacts
* Upcoming birthdays
* Redis caching
* Cloudinary avatar upload
* Docker support
* Sphinx documentation
* Pytest test suite

## Technologies

* FastAPI
* SQLAlchemy
* PostgreSQL
* Redis
* Docker & Docker Compose
* JWT (python-jose)
* Cloudinary
* Pytest
* Sphinx

## Installation

Clone repository:

```bash
git clone https://github.com/khovorun/UMT-pythonweb-hw-13.git
cd UMT-pythonweb-hw-13
```

Create environment variables:

```bash
cp .env.example .env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run with Docker

```bash
docker compose up --build
```

API will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## Running Tests

```bash
pytest -v
```

Coverage report:

```bash
pytest --cov=. --cov-report=term
```

Current coverage:

```text
72%
```

## Documentation

Build Sphinx documentation:

```bash
cd docs
make html
```

Generated documentation:

```text
docs/build/html/index.html
```

## Author

Kseniia Hovorun
