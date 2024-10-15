from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_some_migration'),  # Adjust this to your latest migration
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
