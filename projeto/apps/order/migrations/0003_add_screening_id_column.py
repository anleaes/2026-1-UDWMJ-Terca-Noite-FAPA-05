# Sync SCREENING_ID column on ORDERS when missing in Oracle.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_order_user_alter_order_client'),
        ('screening', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[],
            database_operations=[
                migrations.AddField(
                    model_name='order',
                    name='screening',
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='orders',
                        to='screening.screening',
                    ),
                ),
            ],
        ),
    ]
