# Generated by Django 4.2 on 2023-04-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(default='', max_length=30)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(default='', max_length=50)),
            ],
        ),
    ]