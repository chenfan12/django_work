# Generated by Django 2.2 on 2019-04-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=100)),
                ('phone_price', models.CharField(max_length=20)),
            ],
        ),
    ]