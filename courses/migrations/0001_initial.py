# Generated by Django 2.2.7 on 2019-11-12 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_path', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')])),
                ('value', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses.Course')),
            ],
        ),
    ]