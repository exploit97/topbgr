# Generated by Django 4.1 on 2022-08-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("examen_et_concours", "0008_subject_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
    ]
