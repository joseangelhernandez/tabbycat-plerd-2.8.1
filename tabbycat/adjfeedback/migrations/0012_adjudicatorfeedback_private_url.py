# Generated by Django 3.1.4 on 2021-02-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjfeedback', '0011_auto_20210102_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjudicatorfeedback',
            name='private_url',
            field=models.BooleanField(default=False, verbose_name='from private URL'),
        ),
        migrations.RunSQL(
            sql="UPDATE adjfeedback_adjudicatorfeedback SET private_url=1 WHERE participant_submitter_id IS NULL;",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]