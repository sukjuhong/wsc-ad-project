# Generated by Django 4.2.1 on 2023-05-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='modify_count',
            field=models.IntegerField(default=222),
            preserve_default=False,
        ),
    ]