# Generated by Django 5.0 on 2023-12-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_shift_asr_alter_shift_shab_alter_shift_sobh'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='string_date',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]