# Generated by Django 2.2.10 on 2020-05-24 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_auto_20200524_0855"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventattendee",
            options={
                "ordering": ("signup_date",),
                "verbose_name": "Přihláška na akci",
                "verbose_name_plural": "Přihlášky na akce",
            },
        ),
    ]