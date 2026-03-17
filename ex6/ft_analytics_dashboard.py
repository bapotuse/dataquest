events = [
    {
        'id': 1,
        'player': 'alice',
        'score': 2300,
        'active': True,
        'achievements': [
            'first_kill',
            'speed_demon',
            'monster_slayer'
        ],
        'region': 'north'

    },
    {
        'id': 2,
        'player': 'bob',
        'score': 1800,
        'active': True,
        'achievements': [
            'level_10',
            'collector'
        ],
        'region': 'east'
    },
    {
        'id': 3,
        'player': 'charlie',
        'score': 2150,
        'active': True,
        'achievements': [
            'speed_demon',
            'collector'
        ],
        'region': 'central'
    },
    {
        'id': 4,
        'player': 'diana',
        'score': 2050,
        'active': False,
        'achievements': [
            'treasure_hunter',
            'level_10'
        ],
        'region': 'east'
    }
]


if __name__ == "__main__":
    try:
        print("=== List Comprehension Examples ===")
        high_scorers = [e['player'] for e in events if e['score'] > 2000]
        doubles_score = [e['score'] * 2 for e in events]
        active_players = [e['player'] for e in events if e['active']]
        print(f'High scorers (>2000): {high_scorers}')
        print(f'Scores doubled: {doubles_score}')
        print(f'Active players: {active_players}\n')
        print("=== Dict Comprehension Examples ===")
        player_scores = {e['player']: e['score'] for e in events}
        score_categories = {
            "high": sum(1 for e in events if e['score'] >= 2000),
            "medium": sum(1 for e in events if e['score'] >= 1500
                          and e['score'] < 2000),
            "low": sum(1 for e in events if e['score'] < 1500)
        }
        achievement_count = {e['player']: len(e['achievements'])
                             for e in events}
        print(f'Player scores: {player_scores}')
        print(f'Score categories: {score_categories}')
        print(f'Achievement counts: {achievement_count}\n')
        print("=== Set Comprehension Examples ===")
        unique_players = {e['player'] for e in events}
        unique_achievements = {a for e in events for a in e['achievements']}
        unique_regions = {e['region'] for e in events}
        print(f'Unique players: {unique_players}')
        print(f'Unique achievements: {unique_achievements}')
        print(f'Active regions: {unique_regions}\n')
        print("=== Combined Analysis ===")
        total_players = len(events)
        total_unique_achievements = len({a for e in events
                                         for a in e['achievements']})
        average_score = sum(e['score'] for e in events) / len({e['score']
                                                               for e in events
                                                               })
        top_player = max(events, key=lambda p: p["score"])
        print(f'Total players: {total_players}')
        print(f'Total unique achievements: {total_unique_achievements}')
        print(f'Average score: {average_score}')
        print(f"Top performer: {top_player['player']} ({top_player['score']} \
points, {len(top_player['achievements'])} achievements)")
    except ValueError:
        print("Dictionary or values invalid(s)")
