from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='receipt',
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_status',
            field=models.CharField(default='pendente', max_length=100),
        ),
    ]
