# Generated by Django 3.2.8 on 2021-11-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reg_num', models.BigIntegerField()),
                ('dept', models.CharField(max_length=150)),
                ('year_of_joining', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FirstSemSubjects',
            fields=[
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('computer_science', models.IntegerField()),
                ('electrical', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='SecondSemSubjects',
            fields=[
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('environment_science', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='college.student')),
            ],
        ),
    ]
