# Generated by Django 4.1 on 2022-08-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company_vakancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]
