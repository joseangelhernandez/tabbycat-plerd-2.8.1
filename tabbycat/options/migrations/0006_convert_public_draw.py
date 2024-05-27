from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0005_speaker_standings'),
    ]

    operations = [
        migrations.RunSQL(
            """
            UPDATE o1
            SET o1.raw_value = CASE 
                                WHEN o1.raw_value = 'True' AND o2.raw_value = 'True' THEN 'all-released'
                                WHEN o1.raw_value = 'True' THEN 'current'
                                ELSE 'off'
                              END
            FROM options_tournamentpreferencemodel o1
            INNER JOIN options_tournamentpreferencemodel o2
            ON o1.instance_id = o2.instance_id
            WHERE o1.section = 'public_features' 
            AND o1.name = 'public_draw' 
            AND o2.section = 'ui_options' 
            AND o2.name = 'show_all_draws';
            """,
            """
            UPDATE options_tournamentpreferencemodel
            SET raw_value = CASE 
                            WHEN raw_value = 'off' THEN 'False' 
                            ELSE 'True' 
                            END
            WHERE section = 'public_features' 
            AND name = 'public_draw';
            """,
            elidable=True,
        ),
        migrations.RunSQL(
            """
            DELETE FROM options_tournamentpreferencemodel
            WHERE section = 'ui_options' 
            AND name = 'show_all_draws';
            """,
            """
            INSERT INTO options_tournamentpreferencemodel (section, name, raw_value, instance_id)
            SELECT 'ui_options', 'show_all_draws',
                   CASE 
                     WHEN raw_value = 'all-released' THEN 'True' 
                     ELSE 'False' 
                   END, 
                   instance_id
            FROM options_tournamentpreferencemodel
            WHERE section = 'public_features' 
            AND name = 'public_draw'
            AND NOT EXISTS (
                SELECT 1
                FROM options_tournamentpreferencemodel otp
                WHERE otp.section = 'ui_options'
                AND otp.name = 'show_all_draws'
                AND otp.instance_id = options_tournamentpreferencemodel.instance_id
            );
            """,
            elidable=True,
        ),
    ]
