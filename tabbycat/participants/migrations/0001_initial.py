# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('breakqual', '0001_initial'),
        ('tournaments', '0001_initial'),
        ('divisions', '0001_initial'),
        ('adjallocation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The institution\'s full name, e.g., "University of Cambridge", "Victoria University of Wellington"', max_length=100, verbose_name='name')),
                ('code', models.CharField(help_text='What the institution is typically called for short, e.g., "Cambridge", "Vic Wellington"', max_length=20, verbose_name='code')),
            ],
            options={
                'verbose_name_plural': 'institutions',
                'verbose_name': 'institution',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='name')),
                ('barcode_id', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail address')),
                ('phone', models.CharField(blank=True, max_length=40, verbose_name='phone')),
                ('anonymous', models.BooleanField(default=False, help_text='Anonymous persons will have their name and team redacted on public tab releases', verbose_name='anonymous')),
                ('checkin_message', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], help_text='Gender is displayed in the adjudicator allocation interface, and nowhere else', max_length=1, verbose_name='gender')),
                ('pronoun', models.CharField(blank=True, help_text='If printing ballots using Tabbycat, there is the option to pre-print pronouns', max_length=10, verbose_name='pronoun')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
            },
        ),
        migrations.CreateModel(
            name='SpeakerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name to be displayed, e.g., "Novice", "ESL"', max_length=50, verbose_name='name')),
                ('slug', models.SlugField(help_text='Slug for URLs, e.g., "novice", "esl"', verbose_name='slug')),
                ('seq', models.IntegerField(help_text='The order in which the categories are displayed', verbose_name='sequence number')),
                ('limit', models.IntegerField(default=0, help_text='At most this many speakers will be shown on the public tab for this category, or use 0 for no limit', verbose_name='limit')),
                ('public', models.BooleanField(default=True, help_text='If checked, this category will be included in the speaker category tabs shown to the public', verbose_name='public')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament')),
            ],
            options={
                'verbose_name': 'speaker category',
                'ordering': ['tournament', 'seq'],
                'verbose_name_plural': 'speaker categories',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, help_text='Do not include institution name (see "uses institutional prefix" below)', max_length=150, verbose_name='full name/suffix')),
                ('short_reference', models.CharField(blank=True, help_text='The name shown in the draw. Do not include institution name (see "uses institutional prefix" below)', max_length=35, verbose_name='short name/suffix')),
                ('short_name', models.CharField(editable=False, help_text='The name shown in the draw, including institution name. (This is autogenerated.)', max_length=50, verbose_name='short name')),
                ('long_name', models.CharField(editable=False, help_text='The full name of the team, including institution name. (This is autogenerated.)', max_length=200, verbose_name='long name')),
                ('use_institution_prefix', models.BooleanField(default=False, help_text='If ticked, a team called "1" from Victoria will be shown as "Victoria 1"', verbose_name='Uses institutional prefix')),
                ('url_key', models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key')),
                ('type', models.CharField(choices=[('N', 'none'), ('S', 'swing'), ('C', 'composite'), ('B', 'bye')], default='N', max_length=1, verbose_name='type')),
                ('emoji', models.CharField(blank=True, choices=[('☕', '☕'), ('⛑', '⛑'), ('⛰', '⛰'), ('⛪', '⛪'), ('⛵', '⛵'), ('⛔', '⛔'), ('⛅', '⛅'), ('⛈', '⛈'), ('⛱', '⛱'), ('⛄', '⛄'), ('⚽', '⚽'), ('⛸', ''), ('⛏', '⛏'), ('😁', '😁'), ('😂', '😂'), ('😄', '😄'), ('😅', ''), ('😆', '😆'), ('😉', '😉'), ('😊', '😊'), ('😎', '😎'), ('😍', '😍'), ('😘', '😘'), ('😇', '😇'), ('😐', '😐'), ('😏', '😏'), ('😣', ''), ('😥', '😥'), ('😫', ''), ('😜', '😜'), ('😓', ''), ('😔', ''), ('😖', '😖'), ('😷', '😷'), ('😲', '😲'), ('😞', '😞'), ('😭', '😭'), ('😰', '😰'), ('😱', '😱'), ('😳', '😳'), ('😵', '😵'), ('😡', '😡'), ('👿', '👿'), ('👩', '👩'), ('👴', '👴'), ('👵', '👵'), ('👶', '👶'), ('👮', '👮'), ('👷', '👷'), ('👸', '👸'), ('💂', '💂'), ('🎅', '🎅'), ('👼', '👼'), ('👰', '👰'), ('🙅', '🙅'), ('🙆', '🙆'), ('🙋', '🙋'), ('🙇', '🙇'), ('🙌', '🙌'), ('🙏', '🙏'), ('💃', '💃'), ('💑', '💑'), ('👪', '👪'), ('👫', '👫'), ('👬', '👬'), ('👭', '👭'), ('💪', '💪'), ('👆', '👆'), ('✊', '✊'), ('✋', '✋'), ('👊', '👊'), ('👌', '👌'), ('👍', '👍'), ('👎', '👎'), ('👐', '👐'), ('💅', '💅'), ('👂', '👂'), ('👃', '👃'), ('👅', '👅'), ('👄', '👄'), ('💘', '💘'), ('💔', '💔'), ('💖', '💖'), ('💌', '💌'), ('💧', '💧'), ('💤', ''), ('💣', '💣'), ('💥', '💥'), ('💦', '💦'), ('💨', '💨'), ('💫', ''), ('👓', '👓'), ('👔', '👔'), ('👙', '👙'), ('👜', '👜'), ('👟', '👟'), ('👠', '👠'), ('👒', '👒'), ('🎩', '🎩'), ('💄', '💄'), ('💍', '💍'), ('💎', '💎'), ('👻', '👻'), ('💀', '💀'), ('👽', '👽'), ('👾', '👾'), ('💩', '💩'), ('🐵', ''), ('🙈', ''), ('🙉', ''), ('🙊', ''), ('🐶', '🐶'), ('🐩', ''), ('🐯', '🐯'), ('🐴', '🐴'), ('🐮', '🐮'), ('🐷', '🐷'), ('🐑', '🐑'), ('🐭', '🐭'), ('🐹', '🐹'), ('🐰', '🐰'), ('🐻', '🐻'), ('🐨', '🐨'), ('🐼', '🐼'), ('🐔', '🐔'), ('🐥', ''), ('🐦', '🐦'), ('🐧', '🐧'), ('🐸', '🐸'), ('🐢', ''), ('🐍', '🐍'), ('🐲', '🐲'), ('🐳', '🐳'), ('🐬', ''), ('🐟', '🐟'), ('🐠', ''), ('🐙', '🐙'), ('🐚', '🐚'), ('🐌', ''), ('🐛', ''), ('🐝', '🐝'), ('💐', ''), ('🌸', '🌸'), ('🌹', '🌹'), ('🌻', '🌻'), ('🌷', '🌷'), ('🌱', ''), ('🌴', ''), ('🌵', '🌵'), ('🌿', ''), ('🍀', ''), ('🍁', '🍁'), ('🍇', '🍇'), ('🍉', '🍉'), ('🍊', '🍊'), ('🍋', '🍋'), ('🍌', '🍌'), ('🍍', '🍍'), ('🍎', '🍎'), ('🍑', '🍑'), ('🍒', '🍒'), ('🍓', '🍓'), ('🍅', '🍅'), ('🍆', '🍆'), ('🌽', '🌽'), ('🍄', '🍄'), ('🍞', '🍞'), ('🍔', '🍔'), ('🍟', ''), ('🍕', '🍕'), ('🍙', ''), ('🍨', '🍨'), ('🍩', '🍩'), ('🍪', '🍪'), ('🍰', '🍰'), ('🍭', '🍭'), ('🍼', '🍼'), ('🍷', '🍷'), ('🍸', '🍸'), ('🍹', '🍹'), ('🍺', '🍺'), ('🍴', '🍴'), ('🌋', '🌋'), ('🏠', '🏠'), ('🏢', '🏢'), ('🏥', ''), ('🏩', '🏩'), ('🏰', ''), ('🌊', '🌊'), ('🎡', ''), ('🎢', ''), ('🎨', '🎨'), ('🚃', '🚃'), ('🚄', '🚄'), ('🚝', '🚝'), ('🚍', '🚍'), ('🚔', '🚔'), ('🚘', '🚘'), ('🚲', '🚲'), ('🚨', '🚨'), ('🚣', '🚣'), ('🚁', '🚁'), ('🚀', '🚀'), ('🚦', '🚦'), ('🚧', '🚧'), ('🚫', '🚫'), ('🚷', '🚷'), ('🚻', '🚻'), ('🚽', '🚽'), ('🚿', '🚿'), ('🛀', '🛀'), ('⏳', '⏳'), ('🌑', '🌑'), ('🌕', '🌕'), ('🌗', '🌗'), ('🌞', '🌞'), ('🌈', '🌈'), ('🌂', '🌂'), ('🌟', '🌟'), ('🔥', '🔥'), ('🎃', '🎃'), ('🎄', '🎄'), ('🎈', '🎈'), ('🎉', '🎉'), ('🎓', '🎓'), ('🎯', '🎯'), ('🎀', '🎀'), ('🏀', '🏀'), ('🏈', '🏈'), ('🎾', '🎾'), ('🎱', '🎱'), ('🏊', ''), ('🎮', '🎮'), ('🎲', '🎲'), ('📣', '📣'), ('📯', ''), ('🔔', '🔔'), ('🎶', '🎶'), ('🎤', '🎤'), ('🎹', '🎹'), ('🎺', '🎺'), ('🎻', '🎻'), ('📻', '📻'), ('📱', '📱'), ('📞', '📞'), ('🔋', '🔋'), ('🔌', '🔌'), ('💾', '💾'), ('💿', '💿'), ('🎬', '🎬'), ('📷', '📷'), ('🔍', '🔍'), ('🔭', '🔭'), ('💡', '💡'), ('📕', '📕'), ('📰', '📰'), ('💰', '💰'), ('💸', '💸'), ('📦', ''), ('📫', '📫'), ('💼', '💼'), ('📅', '📅'), ('📎', ''), ('📏', '📏'), ('📐', '📐'), ('🔑', '🔑'), ('🔩', '🔩'), ('💊', ''), ('🔪', '🔪'), ('🔫', '🔫'), ('🚬', '🚬'), ('🏁', ''), ('🔮', '🔮'), ('❌', '❌'), ('❓', '❓'), ('🔞', '🔞'), ('🆒', '🆒'), ('🆗', '🆗'), ('🆘', '🆘'), ('😙', '😙'), ('😑', '😑'), ('😮', '😮'), ('😴', '😴'), ('😛', '😛'), ('😧', '😧'), ('😬', '😬'), ('🕵', '🕵'), ('🖕', '🖕'), ('🖖', '🖖'), ('👁', '👁'), ('🕶', '🕶'), ('🛍', '🛍'), ('🐿', '🐿'), ('🕊', '🕊'), ('🕷', '🕷'), ('🌶', '🌶'), ('🏕', ''), ('🏛', '🏛'), ('🛢', '🛢'), ('🛥', ''), ('🛩', ''), ('🛎', '🛎'), ('🕰', '🕰'), ('🌡', '🌡'), ('🌤', '🌤'), ('🌧', '🌧'), ('🌩', '🌩'), ('🌪', '🌪'), ('🌬', '🌬'), ('🎖', '🎖'), ('🎗', '🎗'), ('🎞', '🎞'), ('🏋', ''), ('🏅', '🏅'), ('🕹', '🕹'), ('🎙', '🎙'), ('🖥', '🖥'), ('🖨', '🖨'), ('🖲', '🖲'), ('📸', ''), ('🕯', '🕯'), ('🗞', ''), ('🖋', '🖋'), ('🗑', '🗑'), ('🛠', ''), ('🗡', '🗡'), ('🛡', '🛡'), ('🏳', '🏳'), ('🏴', '🏴'), ('🤗', '🤗'), ('🤔', '🤔'), ('🙄', '🙄'), ('🤐', '🤐'), ('🤓', '🤓'), ('🙃', '🙃'), ('🤒', '🤒'), ('🤕', '🤕'), ('🤑', '🤑'), ('🤘', '🤘'), ('📿', '📿'), ('🤖', '🤖'), ('🦁', '🦁'), ('🦄', '🦄'), ('🦀', '🦀'), ('🦂', ''), ('🧀', '🧀'), ('🌭', '🌭'), ('🌮', '🌮'), ('🍿', '🍿'), ('🍾', '🍾'), ('🏏', '🏏'), ('🏐', '🏐'), ('🏓', '🏓'), ('🏹', '🏹'), ('\U0001f923', '\U0001f923'), ('\U0001f924', '\U0001f924'), ('\U0001f922', '\U0001f922'), ('\U0001f927', '\U0001f927'), ('\U0001f920', '\U0001f920'), ('\U0001f921', '\U0001f921'), ('\U0001f925', '\U0001f925'), ('\U0001f934', '\U0001f934'), ('\U0001f935', '\U0001f935'), ('\U0001f930', '\U0001f930'), ('\U0001f936', '\U0001f936'), ('\U0001f926', '\U0001f926'), ('\U0001f937', '\U0001f937'), ('\U0001f57a', '\U0001f57a'), ('\U0001f93a', '\U0001f93a'), ('\U0001f938', '\U0001f938'), ('\U0001f939', '\U0001f939'), ('\U0001f933', '\U0001f933'), ('\U0001f91e', '\U0001f91e'), ('\U0001f919', '\U0001f919'), ('\U0001f91b', '\U0001f91b'), ('\U0001f91c', '\U0001f91c'), ('\U0001f91a', '\U0001f91a'), ('\U0001f91d', '\U0001f91d'), ('\U0001f5a4', '\U0001f5a4'), ('\U0001f98a', '\U0001f98a'), ('\U0001f98c', '\U0001f98c'), ('\U0001f987', '\U0001f987'), ('\U0001f985', '\U0001f985'), ('\U0001f986', '\U0001f986'), ('\U0001f989', '\U0001f989'), ('\U0001f98e', '\U0001f98e'), ('\U0001f988', '\U0001f988'), ('\U0001f990', '\U0001f990'), ('\U0001f991', '\U0001f991'), ('\U0001f98b', '\U0001f98b'), ('\U0001f940', '\U0001f940'), ('\U0001f95d', '\U0001f95d'), ('\U0001f951', '\U0001f951'), ('\U0001f954', '\U0001f954'), ('\U0001f955', '\U0001f955'), ('\U0001f952', '\U0001f952'), ('\U0001f95c', '\U0001f95c'), ('\U0001f950', '\U0001f950'), ('\U0001f956', '\U0001f956'), ('\U0001f95e', '\U0001f95e'), ('\U0001f959', '\U0001f959'), ('\U0001f95a', '\U0001f95a'), ('\U0001f957', '\U0001f957'), ('\U0001f95b', '\U0001f95b'), ('\U0001f942', '\U0001f942'), ('\U0001f943', '\U0001f943'), ('\U0001f944', '\U0001f944'), ('\U0001f6f6', '\U0001f6f6'), ('\U0001f94a', '\U0001f94a'), ('\U0001f94b', '\U0001f94b'), ('\U0001f945', '\U0001f945'), ('\U0001f941', '\U0001f941'), ('\U0001f6d2', '\U0001f6d2')], default=None, max_length=2, null=True, verbose_name='emoji')),
                ('break_categories', models.ManyToManyField(blank=True, to='breakqual.BreakCategory', verbose_name='break categories')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='divisions.Division', verbose_name='division')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Institution', verbose_name='institution')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament')),
            ],
            options={
                'verbose_name': 'team',
                'ordering': ['tournament', 'institution', 'short_reference'],
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Adjudicator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='participants.Person')),
                ('test_score', models.FloatField(default=0, verbose_name='test score')),
                ('url_key', models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key')),
                ('trainee', models.BooleanField(default=False, help_text='If checked, this adjudicator will never be auto-allocated a voting position, regardless of their score', verbose_name='always trainee')),
                ('breaking', models.BooleanField(default=False, verbose_name='breaking')),
                ('independent', models.BooleanField(default=False, verbose_name='independent')),
                ('adj_core', models.BooleanField(default=False, verbose_name='adjudication core')),
            ],
            options={
                'verbose_name_plural': 'adjudicators',
                'verbose_name': 'adjudicator',
                'ordering': ['tournament', 'institution', 'name'],
            },
            bases=('participants.person',),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='participants.Person')),
            ],
            options={
                'verbose_name': 'speaker',
                'verbose_name_plural': 'speakers',
            },
            bases=('participants.person',),
        ),
        migrations.AddField(
            model_name='institution',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Region', verbose_name='region'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('reference', 'institution', 'tournament'), ('emoji', 'tournament')]),
        ),
        migrations.AlterIndexTogether(
            name='team',
            index_together=set([('tournament', 'institution', 'short_reference')]),
        ),
        migrations.AlterUniqueTogether(
            name='speakercategory',
            unique_together=set([('tournament', 'seq'), ('tournament', 'slug')]),
        ),
        migrations.AlterIndexTogether(
            name='speakercategory',
            index_together=set([('tournament', 'seq')]),
        ),
        migrations.AddField(
            model_name='speaker',
            name='categories',
            field=models.ManyToManyField(blank=True, to='participants.SpeakerCategory', verbose_name='speaker categories'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team'),
        ),
        migrations.AlterUniqueTogether(
            name='institution',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='conflicts',
            field=models.ManyToManyField(related_name='adj_adj_conflicts', through='adjallocation.AdjudicatorConflict', to='participants.Team', verbose_name='team conflicts'),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='institution_conflicts',
            field=models.ManyToManyField(related_name='adj_inst_conflicts', through='adjallocation.AdjudicatorInstitutionConflict', to='participants.Institution', verbose_name='institution conflicts'),
        ),
        migrations.AddField(
            model_name='adjudicator',
            name='tournament',
            field=models.ForeignKey(blank=True, help_text='Adjudicators not assigned to any tournament can be shared between tournaments', null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
    ]
