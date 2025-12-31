# Basic

## 快速开始

```bash
uv sync
python manage.py init_db basic
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```

## 重要组件

```toml
ruff
drf-spectacular[sidecar]
django-environ
pytest-django
```