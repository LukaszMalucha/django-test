# Generated by Django 2.2 on 2021-02-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('day', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=254)),
                ('text', models.TextField(default='')),
                ('text_en', models.TextField(default='')),
                ('text_pl', models.TextField(default='')),
                ('text_es', models.TextField(default='')),
                ('text_fr', models.TextField(default='')),
                ('month_string', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
