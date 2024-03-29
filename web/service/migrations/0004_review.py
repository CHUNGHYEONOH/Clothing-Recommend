# Generated by Django 2.2.1 on 2019-11-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0003_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('designer', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
