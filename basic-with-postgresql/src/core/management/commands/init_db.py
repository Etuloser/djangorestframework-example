import psycopg2
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create PostgreSQL database if it does not exist (from DATABASE_URL)"

    def handle(self, *args, **options):
        db = settings.DATABASES["default"]

        db_name = db["NAME"]
        host = db.get("HOST", "127.0.0.1")
        user = db["USER"]
        password = db["PASSWORD"]
        port = int(db.get("PORT", 5432))

        self.stdout.write(
            f"Ensuring PostgreSQL database `{db_name}` exists on {host}:{port}..."
        )

        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host,
            port=port,
            autocommit=True,
        )

        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (db_name,),
            )
            exists = cursor.fetchone()

            if not exists:
                cursor.execute(f'CREATE DATABASE "{db_name}"')
                self.stdout.write(self.style.SUCCESS(f"Database `{db_name}` created"))
            else:
                self.stdout.write(
                    self.style.SUCCESS(f"Database `{db_name}` already exists")
                )

        conn.close()
