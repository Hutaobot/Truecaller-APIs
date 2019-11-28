# Generated by Django 2.2.7 on 2019-11-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalcontacts',
            name='spam_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='personalcontacts',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]