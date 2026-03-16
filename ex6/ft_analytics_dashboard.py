events = [
    {
        'id': 1,
        'player': 'alice',
        'score': 2300,
        'active': True
    },
    {
        'id': 2,
        'player': 'bob',
        'score': 1800,
        'active': True
    },
    {
        'id': 3,
        'player': 'charlie',
        'score': 2150,
        'active': True
    },
    {
        'id': 4,
        'player': 'diana',
        'score': 2050,
        'active': False
    }
]


if __name__ == "__main__":
    try:
        print("=== List Comprehension Examples ===")
        high_scorers = list({e['player'] for e in events if e['score'] > 2000})
        doubles_score = list({e['score'] * 2 for e in events})
        active_players = list({e['player'] for e in events if e['active']})
        print(f'High scorers (>2000): {high_scorers}')
        print(f'Scores doubled: {doubles_score}')
        print(f'Active players: {active_players}\n')
    except ValueError:
        print("Dictionary or values invalid(s)")
