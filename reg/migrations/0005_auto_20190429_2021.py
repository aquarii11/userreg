# Generated by Django 2.2 on 2019-04-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_auto_20190429_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
