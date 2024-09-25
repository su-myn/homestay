# Generated by Django 5.1.1 on 2024-09-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=20)),
                ('contractor', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('repair_issue', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')], default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
