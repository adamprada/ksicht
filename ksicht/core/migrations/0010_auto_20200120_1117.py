# Generated by Django 2.2.8 on 2020-01-20 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_gradeseries_results_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={
                "ordering": ("series", "title"),
                "permissions": (("solution_export", "Export odevzdaných úloh"),),
                "verbose_name": "Úloha",
                "verbose_name_plural": "Úlohy",
            },
        ),
        migrations.AlterField(
            model_name="participant",
            name="school_year",
            field=models.CharField(
                choices=[
                    ("4", "4."),
                    ("3", "3."),
                    ("2", "2."),
                    ("1", "1."),
                    ("l", "nižší"),
                ],
                max_length=1,
                verbose_name="Ročník",
            ),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Název")),
                ("description", models.TextField(blank=True, verbose_name="Popis")),
                (
                    "place",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Místo konání"
                    ),
                ),
                ("start_date", models.DateField(db_index=True, verbose_name="Začíná")),
                ("end_date", models.DateField(db_index=True, verbose_name="Končí")),
                (
                    "capacity",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Doporučený max. počet účastníků",
                    ),
                ),
                (
                    "enlistment_message",
                    models.TextField(blank=True, verbose_name="Zpráva po přihlášení"),
                ),
                (
                    "attendees",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL, verbose_name="Účastníci"
                    ),
                ),
            ],
            options={
                "verbose_name": "Akce",
                "verbose_name_plural": "Akce",
                "ordering": ("start_date",),
            },
        ),
    ]