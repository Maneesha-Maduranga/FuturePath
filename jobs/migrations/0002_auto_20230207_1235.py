# Generated by Django 3.2.16 on 2023-02-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='modality',
            field=models.CharField(blank=True, choices=[('R', 'Remote'), ('I', 'InOffice')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]