# Generated by Django 3.2.8 on 2021-11-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=False, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='ph_num',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
