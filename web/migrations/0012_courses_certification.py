# Generated by Django 5.1.2 on 2024-10-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_courses_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='certification',
            field=models.TextField(default='certification'),
            preserve_default=False,
        ),
    ]
