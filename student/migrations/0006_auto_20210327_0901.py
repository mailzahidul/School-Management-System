# Generated by Django 3.1.7 on 2021-03-27 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210320_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.AddField(
            model_name='studetailsinfo',
            name='roll',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.studetailsinfo')),
            ],
        ),
    ]