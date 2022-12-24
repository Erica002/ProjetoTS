# Generated by Django 4.1.4 on 2022-12-24 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nome", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
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
                ("detalhes", models.CharField(max_length=255)),
                ("valor_necessario", models.FloatField()),
                ("valor_salvo", models.FloatField(default=0)),
                ("data", models.DateField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Renda",
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
                ("detalhes", models.CharField(max_length=255)),
                ("valor_renda", models.FloatField()),
                (
                    "origem",
                    models.CharField(
                        choices=[
                            ("Salário", "Salário"),
                            ("Freelancer", "Freelancer"),
                            ("Extra", "Extra"),
                        ],
                        default="Extra",
                        max_length=155,
                    ),
                ),
                ("data", models.DateField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Despesa",
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
                ("detalhes", models.TextField()),
                ("valor_despesa", models.FloatField()),
                ("data", models.DateField()),
                (
                    "forma_pagamento",
                    models.CharField(
                        choices=[
                            ("Cartão de Crédito", "Cartão de Crédito"),
                            ("Dinheiro", "Dinheiro"),
                            ("Pix", "Pix"),
                        ],
                        default="Dinheiro",
                        max_length=155,
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.categoria"
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
        ),
    ]