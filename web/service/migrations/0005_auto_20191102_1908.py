# Generated by Django 2.2.1 on 2019-11-02 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='userid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
