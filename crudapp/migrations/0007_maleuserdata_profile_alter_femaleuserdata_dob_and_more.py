# Generated by Django 4.1 on 2022-10-22 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0006_alter_femaleuserdata_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maleuserdata',
            name='profile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='femaleuserdata',
            name='DOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='marriage',
            name='Spouce_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Spouce', to='crudapp.maleuserdata', unique=True),
        ),
    ]