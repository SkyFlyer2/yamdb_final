# Generated by Django 2.2.16 on 2022-09-02 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220830_0342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',)},
        ),
    ]
