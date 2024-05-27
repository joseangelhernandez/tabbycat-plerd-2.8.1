# Generated by Django 3.1.4 on 2021-02-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0008_auto_20201126_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballotsubmission',
            name='partial',
            field=models.BooleanField(default=False, verbose_name='partial'),
        ),
        migrations.AddField(
            model_name='ballotsubmission',
            name='private_url',
            field=models.BooleanField(default=False, verbose_name='from private URL'),
        ),
        migrations.RunSQL(
            "UPDATE results_ballotsubmission SET private_url = 1 WHERE participant_submitter_id IS NULL;",
            migrations.RunSQL.noop,
        ),
    ]
