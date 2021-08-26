# Generated by Django 3.2.6 on 2021-08-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FORM1A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM1B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM2A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM2B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM3A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM3B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM4A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FORM4B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson1', models.CharField(max_length=200)),
                ('Lesson2', models.CharField(max_length=200)),
                ('Break_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson3', models.CharField(max_length=200)),
                ('Lesson4', models.CharField(max_length=200)),
                ('Break_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson5', models.CharField(max_length=200)),
                ('Lesson6', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(blank=True, max_length=200, null=True)),
                ('L_Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('Lesson7', models.CharField(max_length=200)),
                ('Lesson8', models.CharField(max_length=200)),
                ('Lesson9', models.CharField(max_length=200)),
                ('Games', models.CharField(blank=True, max_length=200, null=True)),
                ('Class_Teacher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
