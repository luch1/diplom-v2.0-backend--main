from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_room_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='participants',
        ),
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
