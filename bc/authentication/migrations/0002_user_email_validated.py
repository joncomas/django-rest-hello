# Generated by Django 3.0.2 on 2020-02-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_validated',
            field=models.BooleanField(default=False),
        ),
    ]