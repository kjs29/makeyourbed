# Generated by Django 4.1.5 on 2023-02-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
