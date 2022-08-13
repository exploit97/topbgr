# Generated by Django 4.1 on 2022-08-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("examen_et_concours", "0005_auto_20220811_1052"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="/image"),
        ),
        migrations.RemoveField(
            model_name="subject",
            name="matter",
        ),
        migrations.AddField(
            model_name="subject",
            name="matter",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="examen_et_concours.matter"
            ),
        ),
    ]