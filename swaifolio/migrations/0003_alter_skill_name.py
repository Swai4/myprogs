# Generated by Django 4.0 on 2023-05-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaifolio', '0002_portfolio_fk_services_fk_serv_skill_fk_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
