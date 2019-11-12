
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')]),
        ),
    ]
