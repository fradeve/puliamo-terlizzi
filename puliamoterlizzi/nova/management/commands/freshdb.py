import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


def recreate_db():
    db = settings.DATABASES["default"]["NAME"]
    if not settings.DATABASES["default"]['HOST'] in ['', 'localhost', '127.0.0.1']:
        # checks that PostGIS DB is not local
        print("*******************************************")
        print("* Cant recreate the db because its remote *")
        print("*******************************************")
        return
    elif settings.DATABASES['default']['ENGINE'] == 'django.contrib.gis.db.backends.spatialite':
        # checks if DB is SpatiaLite
        print("Overwriting old db with new SpatiaLite db...")
        os.system('spatialite ' + db + ' "SELECT InitSpatialMetaData();"')
        call_command("syncdb", interactive=False)
        return
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
        print("Running syncdb...")
        call_command("syncdb")
        fixtures = [
            "nova/fixtures/default_pages.json",
            "nova/fixtures/default_geodata.json",
        ]
        for fixture in fixtures:
            print("Loading fixture {0}".format(fixture))
            call_command('loaddata', fixture)
        print("Freshdb finished successfully!")
