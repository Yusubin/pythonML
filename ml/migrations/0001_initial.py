# Generated by Django 3.2.13 on 2022-05-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.IntegerField()),
                ('week', models.IntegerField()),
                ('time', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('age', models.IntegerField()),
                ('size', models.IntegerField()),
                ('tag', models.IntegerField()),
            ],
        ),
    ]
