# Generated by Django 4.1 on 2022-10-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_alter_marriage_spouce_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='marriage',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
