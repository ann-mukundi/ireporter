# Generated by Django 2.1.7 on 2019-03-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0005_auto_20190315_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redflagmodel',
            name='createdBy',
            field=models.CharField(max_length=30, null=True),
        ),
    ]