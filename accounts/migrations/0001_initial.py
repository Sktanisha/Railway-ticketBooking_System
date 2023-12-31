# Generated by Django 2.1.3 on 2022-01-09 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('confpassword', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('contact', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
            options={
                'db_table': 'profile_tokens',
            },
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=20)),
                ('purchaser_name', models.CharField(max_length=20)),
                ('purchaser_email', models.CharField(max_length=20)),
                ('purchaser_contact', models.IntegerField(max_length=11)),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('seats', models.IntegerField()),
                ('availableseats', models.IntegerField()),
                ('arrivetime', models.TimeField()),
                ('nofperson', models.IntegerField()),
                ('doj', models.DateField()),
                ('totalfare', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_email', models.CharField(max_length=20)),
                ('train_name', models.CharField(max_length=20)),
                ('nofperson', models.IntegerField()),
                ('doj', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('train_name', models.CharField(max_length=20)),
                ('arrivetime', models.TimeField()),
                ('doj', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=20)),
                ('seats', models.IntegerField()),
                ('fare', models.IntegerField()),
            ],
        ),
    ]
