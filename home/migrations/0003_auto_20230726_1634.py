# Generated by Django 2.2.12 on 2023-07-26 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='dec_spec',
            new_name='doc_spec',
        ),
    ]
