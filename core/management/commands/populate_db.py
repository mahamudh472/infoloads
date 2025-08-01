from django.core.management import BaseCommand
import json
from downloads.models import App, AppVersion, Platform

class Command(BaseCommand):
    help = "Populate database with app data."

    def handle(self, *args, **options):
        with open('app_data.json', 'r') as f:
            data = json.load(f)
            for item in data:
                app_name = item['fields']['name']
                meta_description = item['fields']['meta_description']
                long_description = item['fields']['long_description']
                image_url = item['fields']['image_url']
                platform = item['fields']['platform']
                language = item['fields']['language']
                licence = item['fields']['licence']
                os = item['fields']['os']
                app_type = item['fields']['app_type']

                version = item['fields']['version'].lower().replace('v', '')
                file_url = item['fields']['file_url']
                size = item['fields']['size']

                platform_, created = Platform.objects.get_or_create(name="Android")

                app = App.objects.create(
                    name=app_name,
                    meta_description=meta_description,
                    long_description=long_description,
                    image_url=image_url,
                    platform=platform_,
                    language=language,
                    licence=licence,
                    os=os,
                    app_type=app_type
                )

                app_version = AppVersion.objects.create(
                    app=app,
                    version_name=version,
                    version_code=1,
                    file_url=file_url,
                    size=size,
                )
                self.stdout.write(f'{app.id}App: {app.name}\nApp version: {app_version}')
