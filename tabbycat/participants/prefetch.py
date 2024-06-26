from django.db.models import Avg, Value, Count, Sum, Case, When, IntegerField, Q
from django.db.models.functions import Coalesce

from adjallocation.models import DebateAdjudicator
from adjfeedback.models import AdjudicatorFeedback
from participants.models import Adjudicator, Team
from standings.teams import PointsMetricAnnotator, WinsMetricAnnotator



def populate_win_counts(teams, round=None):
    """Populates the `_win_count` and `_points` attributes of the teams in
    `teams`. Operates in-place."""

    teams_by_id = {team.id: team for team in teams}

    for team in teams:
        print(team)

    # CHANGE 1: Added filter to only get confirmed ballots / ISSUE IN THE MSSQL DATABASE FOR ORDERING
    # teams_annotated = Team.objects.filter(
    #     id__in=teams_by_id.keys()
    # ).annotate(
    #     win_count_annotation=Count(Case(When(win=True, then=1)), output_field=IntegerField()),
    #     points_annotation=Coalesce(Sum('points', filter=Q(round=round)), Value(0))
    # )
 
    # PREVIOUS CODE
    teams_annotated = Team.objects.filter(id__in=teams_by_id.keys()).annotate(
         win_count_annotation=WinsMetricAnnotator().get_annotation(round=round),
         points_annotation=Coalesce(PointsMetricAnnotator().get_annotation(round=round), Value(0)),
    )

    print("DEBUG 15555", teams_by_id)
    print()
    print()


    for team in teams_annotated:
        teams_by_id[team.id]._wins_count = team.win_count_annotation
        teams_by_id[team.id]._points = team.points_annotation
        print("DEBUG 15555", team.win_count_annotation)
        print()
        print()


def populate_feedback_scores(adjudicators):
    """Populates the `_feedback_score_cache` attribute of the adjudicators
    in `adjudicators`.
    Operates in-place."""

    adjs_by_id = {adj.id: adj for adj in adjudicators}

    adjfeedbacks = AdjudicatorFeedback.objects.filter(
        adjudicator_id__in=adjs_by_id.keys(),
        confirmed=True,
        ignored=False,
    ).exclude(source_adjudicator__type=DebateAdjudicator.TYPE_TRAINEE)

    adjs_annotated = Adjudicator.objects.filter(
        id__in=adjs_by_id.keys(),
        adjudicatorfeedback__in=adjfeedbacks,
    ).annotate(feedback_score_annotation=Avg('adjudicatorfeedback__score'))

    for adj in adjs_annotated:
        adjs_by_id[adj.id]._feedback_score_cache = adj.feedback_score_annotation

    for adj in adjudicators:
        if not hasattr(adj, '_feedback_score_cache'):
            adj._feedback_score_cache = None
