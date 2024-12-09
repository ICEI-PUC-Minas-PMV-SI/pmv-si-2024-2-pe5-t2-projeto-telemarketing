# Generated by Django 4.2 on 2024-11-19 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clientelemarketing",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200, verbose_name="Nome")),
                ("address", models.CharField(max_length=250, verbose_name="Endereço")),
                (
                    "type_client",
                    models.IntegerField(
                        choices=[(1, "PESSOA FÍSICA"), (2, "EMPRESA")],
                        default=1,
                        verbose_name="Tipo de cliente",
                    ),
                ),
                (
                    "telcell",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        verbose_name="Nº telefone celular",
                    ),
                ),
                (
                    "telfix",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        verbose_name="Nº telefone fixo",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=True, verbose_name="Cliente ativo"),
                ),
            ],
            options={
                "verbose_name": "Operação",
                "verbose_name_plural": "Operações",
            },
        ),
    ]