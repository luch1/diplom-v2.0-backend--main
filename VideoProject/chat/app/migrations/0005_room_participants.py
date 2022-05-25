from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20211013_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
