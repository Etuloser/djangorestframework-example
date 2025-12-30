import MySQLdb
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create MySQL database if it does not exist (from DATABASE_URL)"

    def handle(self, *args, **options):
        db = settings.DATABASES["default"]

        db_name = db["NAME"]
        host = db.get("HOST", "127.0.0.1")
        user = db["USER"]
        password = db["PASSWORD"]
        port = int(db.get("PORT", 3306))

        self.stdout.write(f"Ensuring database `{db_name}` exists on {host}:{port}...")

        conn = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            port=port,
            charset="utf8mb4",
        )

        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE DATABASE IF NOT EXISTS `{db_name}`
            CHARACTER SET utf8mb4
            COLLATE utf8mb4_unicode_ci;
            """
        )

        cursor.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS(f"Database `{db_name}` is ready"))
