# Generated by Django 4.1.2 on 2022-10-29 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_link', models.URLField()),
                ('short_link', models.CharField(max_length=6, unique=True)),
                ('last_enter_date', models.DateTimeField()),
                ('unique_users_counter', models.IntegerField(default=0)),
                ('user_ip', models.GenericIPAddressField(unique=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
