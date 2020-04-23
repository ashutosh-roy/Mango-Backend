# Generated by Django 3.0.5 on 2020-04-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=100, null=True)),
                ('uemail', models.CharField(max_length=100, unique=True)),
                ('upass', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=16)),
                ('upass', models.CharField(max_length=16)),
                ('uemail', models.CharField(max_length=16)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]