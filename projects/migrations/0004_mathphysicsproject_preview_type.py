# Generated by Django 3.1 on 2020-08-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200811_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathphysicsproject',
            name='preview_type',
            field=models.CharField(default='pdf', max_length=10),
        ),
    ]
