from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    # Change 'admin' and 'yourpassword' to what you want!
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword123')

class Migration(migrations.Migration):
    dependencies = [
        ('wall', '0001_initial'), # Make sure this matches your first migration file name
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
    ]
