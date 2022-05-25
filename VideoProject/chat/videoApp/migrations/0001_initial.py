from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0007_room_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='uploads/')),
                ('title', models.CharField(default='', max_length=255)),
                ('rate_video', models.IntegerField(default=0, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoApp.category')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoApp.video')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ManyToManyField(through='videoApp.VideoCategory', to='videoApp.Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='app.UserProfile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoApp.video')),
            ],
        ),
    ]
