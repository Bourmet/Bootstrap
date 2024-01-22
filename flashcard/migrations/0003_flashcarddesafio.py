# Generated by Django 5.0.1 on 2024-01-19 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_flashcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashcardDesafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondido', models.BooleanField(default=False)),
                ('acertou', models.BooleanField(default=False)),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flashcard.flashcard')),
            ],
        ),
    ]
