# Generated by Django 2.2.2 on 2019-07-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0003_auto_20190715_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webinars',
            name='remarks',
        ),
        migrations.AddField(
            model_name='webinars',
            name='remark',
            field=models.TextField(default=''),
        ),
    ]
