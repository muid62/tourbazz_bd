# Generated by Django 3.0.3 on 2020-03-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1500)),
            ],
        ),
    ]
