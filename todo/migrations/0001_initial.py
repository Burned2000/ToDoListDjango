# Generated by Django 2.2.1 on 2019-12-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_text', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
