# Generated by Django 4.2.4 on 2023-08-11 17:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_rename_capa_veiculo_img"),
    ]

    operations = [
        migrations.RenameField(
            model_name="veiculo",
            old_name="img",
            new_name="capa",
        ),
    ]
