# Generated by Django 3.1.7 on 2021-04-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210409_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
