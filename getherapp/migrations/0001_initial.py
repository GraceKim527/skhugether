# Generated by Django 4.0.4 on 2022-05-20 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('class_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('feedback_date', models.DateTimeField()),
                ('feedback_content', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_id', models.IntegerField()),
                ('professor_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.IntegerField()),
                ('classroom_unit', models.CharField(max_length=10)),
                ('class_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='getherapp.class')),
                ('professor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='getherapp.professor')),
            ],
        ),
    ]