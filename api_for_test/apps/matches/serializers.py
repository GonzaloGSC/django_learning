from rest_framework import serializers

from apps.matches.models import (
    m_match,
    m_team,
)

class s_match(serializers.ModelSerializer):
    class meta:
        model = m_match
        read_only_fields = ['id']
        fields = [
            'id',
            'team1',
            'team2',
            'score1',
            'score2',
            'start_time_tz',
            'end_time_tz',
        ]


class s_team(serializers.ModelSerializer):
    class meta:
        model = m_team
        read_only_fields = ['id']
        fields = [
            'id',
            'team_name',
            'coach',
            'captain',
            'stadium',
            'location',
            'wins',
            'losses',
            'draws',
        ]