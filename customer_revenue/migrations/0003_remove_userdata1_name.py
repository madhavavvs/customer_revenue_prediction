# Generated by Django 3.2.8 on 2021-11-16 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_revenue', '0002_auto_20211116_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata1',
            name='name',
        ),
    ]
