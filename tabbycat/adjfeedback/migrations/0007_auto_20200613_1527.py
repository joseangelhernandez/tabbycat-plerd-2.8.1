# Generated by Django 2.2.9 on 2020-06-13 18:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adjfeedback', '0006_auto_20191109_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjudicatorfeedbackquestion',
            name='choices_temp',
            field=models.TextField(blank=True, help_text="Permissible choices for select one/multiple fields (ignored for other fields)", verbose_name='choices', default=""),
        ),
        migrations.RunSQL(
            sql="UPDATE adjfeedback_adjudicatorfeedbackquestion SET choices_temp=REPLACE(choices, '//', ', ');",
            reverse_sql="UPDATE adjfeedback_adjudicatorfeedbackquestion SET choices=REPLACE(choices_temp, ', ', '//');",
        ),
        migrations.RemoveField(
            model_name='adjudicatorfeedbackquestion',
            name='choices',
        ),
        migrations.RenameField(
            model_name='adjudicatorfeedbackquestion',
            old_name='choices_temp',
            new_name='choices',
        ),
        migrations.CreateModel(
            name='AdjudicatorFeedbackManyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adjfeedback.AdjudicatorFeedback', verbose_name='feedback')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adjfeedback.AdjudicatorFeedbackQuestion', verbose_name='question')),
            ],
            options={
                'verbose_name': 'adjudicator feedback multiple select answer',
                'verbose_name_plural': 'adjudicator feedback multiple select answers',
                'abstract': False,
                'unique_together': {('question', 'feedback')},
            },
        ),
        migrations.RunSQL(
            sql="INSERT INTO adjfeedback_adjudicatorfeedbackmanyanswer (answer, feedback_id, question_id) SELECT REPLACE(a.answer, '//', ', '), a.feedback_id, q.id FROM adjfeedback_adjudicatorfeedbackstringanswer a INNER JOIN adjfeedback_adjudicatorfeedbackquestion q ON a.question_id=q.id WHERE q.answer_type='ms';",
            reverse_sql="INSERT INTO adjfeedback_adjudicatorfeedbackstringanswer (answer, feedback_id, question_id) SELECT REPLACE(answer, ', ', '//'), feedback_id, question_id FROM adjfeedback_adjudicatorfeedbackmanyanswer;",
        ),
        migrations.RunSQL(
            sql="DELETE FROM adjfeedback_adjudicatorfeedbackstringanswer WHERE question_id IN (SELECT id FROM adjfeedback_adjudicatorfeedbackquestion WHERE answer_type='ms');",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
