# Generated by Django 2.0.3 on 2019-11-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawrkz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharemarket',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
