import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


def recreate_db():
    db = settings.DATABASES["default"]["NAME"]
    if not settings.DATABASES["default"]['HOST'] in ['', 'localhost', '127.0.0.1']:
        print("*******************************************")
        print("* Cant recreate the db because its remote *")
        print("*******************************************")
        return

    print("Dropping old db...")
    if getattr(settings, "DATABASES")["default"]["ENGINE"] == "django.db.backends.sqlite3":
        db_file = getattr(settings, "DATABASES")["default"]["NAME"]
        print("Creating a new db...")
        os.system("rm {0} ; touch {1}".format(db_file, db_file))
    else:
        if os.system("sudo su - postgres --command 'dropdb {0}'".format(db)) != 0:
            print("Failed to drop the old database...")
            return
        print("Creating a new db...")
        create_db_command = "sudo su - postgres --command 'createdb -T template_postgis --encoding UTF8 {0}'".format(db)
        if os.system(create_db_command) != 0:
            print("Failed to create the database {0}".format(db))


class Command(BaseCommand):
    """
    manage.py command for refreshing the database.
    It drops the database, creates a new one, loads the schema,
    initial data, and environment specific data.
    """

    help = "Create a fresh database"

    def handle(self, *args, **options):
        recreate_db()
        print("Running createdb...")
        call_command("createdb --noinput")
        print("Running migration scripts...")
        call_command("migrate")
        fixtures = [
            "nova/fixtures/default_geodata.json",
        ]
        for fixture in fixtures:
            print("Loading fixture {0}".format(fixture))
            call_command('loaddata', fixture)
        print("Freshdb finished successfully!")
