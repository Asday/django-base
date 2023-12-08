from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Capability",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Can",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "denormalised_str",
                    models.CharField(editable=False, max_length=255),
                ),
                (
                    "capability",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="capabilities",
                        to="capabilities.capability",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "capability")},
            },
        ),
        migrations.CreateModel(
            name="Implication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("references", models.PositiveIntegerField(default=1)),
                (
                    "denormalised_str",
                    models.CharField(editable=False, max_length=209),
                ),
                (
                    "capability",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="implicators",
                        to="capabilities.capability",
                    ),
                ),
                (
                    "implies",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="implications",
                        to="capabilities.capability",
                    ),
                ),
            ],
            options={
                "unique_together": {("capability", "implies")},
            },
        ),
    ]
