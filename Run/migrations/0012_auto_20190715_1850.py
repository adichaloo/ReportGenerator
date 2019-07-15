# Generated by Django 2.2.2 on 2019-07-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Run', '0011_auto_20190715_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='', max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('authority', models.CharField(default='', max_length=1000)),
                ('period', models.CharField(default='', max_length=1000)),
                ('grant', models.CharField(default='', max_length=1000)),
                ('order', models.CharField(default='', max_length=1000)),
                ('profile1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pro6', to='Run.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='research2',
            field=models.ManyToManyField(to='Run.Research2'),
        ),
    ]
