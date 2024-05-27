# Generated by Django 3.1.4 on 2021-01-02 21:37

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('adjfeedback', '0010_merge_20200904_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicatorfeedbackmanyanswer',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedbackquestion',
            name='choices',
            field=models.TextField(blank=True, default='', help_text='Permissible choices for select one/multiple fields (ignored for other fields)', verbose_name='choices'),
        ),
    ]
