# Generated by Django 4.2.11 on 2024-04-07 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("strategy", "0002_rename_passphrase_account_api_passphrase_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="strategy",
            options={"verbose_name": "策略配置", "verbose_name_plural": "策略配置"},
        ),
        migrations.AlterField(
            model_name="strategy",
            name="max_close_rate",
            field=models.DecimalField(
                decimal_places=4,
                help_text="价差低于该值可平仓",
                max_digits=5,
                verbose_name="平仓最高收益率",
            ),
        ),
        migrations.AlterField(
            model_name="strategy",
            name="min_open_rate",
            field=models.DecimalField(
                decimal_places=4,
                help_text="价差超过该值可开仓",
                max_digits=5,
                verbose_name="开仓最低收益率",
            ),
        ),
    ]