# Generated by Django 4.2.4 on 2023-08-11 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_veiculo_capa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='capa',
            new_name='img',
        ),
    ]
