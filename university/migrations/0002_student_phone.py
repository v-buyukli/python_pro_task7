# Generated by Django 4.2 on 2023-05-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(default="+380", max_length=100),
            preserve_default=False,
        ),
    ]
