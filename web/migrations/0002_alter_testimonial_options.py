# Generated by Django 5.1.2 on 2024-10-15 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['id']},
        ),
    ]
