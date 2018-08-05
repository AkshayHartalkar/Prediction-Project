# Generated by Django 2.0.1 on 2018-04-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabetesPrediction', '0003_auto_20180415_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetesrecord',
            name='accuracy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='diabetesrecord',
            name='classlabel',
            field=models.CharField(default='', max_length=10),
        ),
    ]