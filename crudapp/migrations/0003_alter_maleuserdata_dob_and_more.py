# Generated by Django 4.1 on 2022-10-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_femaleuserdata_profile_maleuserdata_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maleuserdata',
            name='DOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='marriage',
            name='Marriage_certificate',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]