# Generated by Django 2.0.3 on 2018-04-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, help_text='Pre-Windows 2000 login username.', max_length=128, null=True)),
            ],
        ),
    ]
