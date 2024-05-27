from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_move_welcome_message'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO options_tournamentpreferencemodel (section, name, raw_value, instance_id)
            SELECT section, new_pref, raw_value, instance_id
            FROM options_tournamentpreferencemodel
            CROSS JOIN (SELECT 'ballots_per_debate_prelim' AS new_pref UNION SELECT 'ballots_per_debate_elim' AS new_pref) t
            WHERE section = 'debate_rules' AND name = 'ballots_per_debate'
            AND NOT EXISTS (
                SELECT 1
                FROM options_tournamentpreferencemodel otp
                WHERE otp.section = options_tournamentpreferencemodel.section
                AND otp.name = t.new_pref
                AND otp.instance_id = options_tournamentpreferencemodel.instance_id
            );
            """,
            """
            DELETE FROM options_tournamentpreferencemodel
            WHERE section = 'debate_rules' AND name IN ('ballots_per_debate_prelim', 'ballots_per_debate_elim');
            """,
            elidable=True,
        ),
        migrations.RunSQL(
            """
            DELETE FROM options_tournamentpreferencemodel
            WHERE section = 'debate_rules' AND name = 'ballots_per_debate';
            """,
            """
            INSERT INTO options_tournamentpreferencemodel (section, name, raw_value, instance_id)
            SELECT section, name, raw_value, instance_id
            FROM options_tournamentpreferencemodel
            WHERE section = 'debate_rules' AND name = 'ballots_per_debate_prelim';
            """,
            elidable=True,
        ),
    ]
