# Generated by Django 5.1.4 on 2024-12-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_communitie_delete_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitie',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
