# Generated by Django 3.2 on 2022-09-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuable', models.BooleanField(null=True, verbose_name='Valuable')),
            ],
        ),
    ]
