import time


events = [
    {
        'id': 1,
        'player': 'frank',
        'event_type': 'login',
        'timestamp': '2024-01-01T23:17',
        'data': {
            'level': 16,
            'score_delta': 128,
            'zone': 'pixel_zone_2'
        }
    },
    {
        'id': 2,
        'player': 'frank',
        'event_type': 'login',
        'timestamp': '2024-01-22T23:57',
        'data': {
            'level': 35,
            'score_delta': -11,
            'zone': 'pixel_zone_5'
        }
    },
    {
        'id': 3,
        'player': 'diana',
        'event_type': 'login',
        'timestamp': '2024-01-01T02:13',
        'data': {
            'level': 15,
            'score_delta': 417,
            'zone': 'pixel_zone_5'
        }
    },
    {
        'id': 4,
        'player': 'alice',
        'event_type': 'level_up',
        'timestamp': '2024-01-07T22:41',
        'data': {
            'level': 45,
            'score_delta': 458,
            'zone': 'pixel_zone_4'
        }
    },
    {
        'id': 5,
        'player': 'bob',
        'event_type': 'death',
        'timestamp': '2024-01-19T08:51',
        'data': {
            'level': 1,
            'score_delta': 63,
            'zone': 'pixel_zone_4'
        }
    },
]


def trier_evenements(liste):
    try:
        liste_triee = sorted(liste, key=lambda x: x['id'])
        for element in liste_triee:
            yield element
    except ValueError:
        print("Invalid list")


def parse_events(element):
    try:
        return next(element)
    except StopIteration:
        return None


def fibonacci(number):
    count = 0
    nombre_a = 0
    nombre_b = 1
    result = 0
    liste = [0, 1]
    while count < number - 2:
        result = nombre_a + nombre_b
        liste.append(result)
        nombre_a = nombre_b
        nombre_b = result
        count += 1
    return ', '.join(str(n) for n in liste)


def nombres_premiers(taille):
    liste = []
    nombre = 2
    while len(liste) < taille:
        est_premier = True
        for i in range(2, nombre):
            if nombre % i == 0:
                est_premier = False
                break
        if est_premier:
            liste.append(nombre)
        nombre += 1
    return ', '.join(str(n) for n in liste)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print(f'Processing {len(events)} game events...\n')
    debut = time.perf_counter()

    try:
        evenements_exemple = trier_evenements(events)
        evenements = trier_evenements(events)
    except Exception as e:
        print(f"Error sorting events : {e}")
        exit()

    count_level = 0
    count_treasure = 0
    count_levelup = 0

    for i in range(len(events)):
        try:
            event = parse_events(evenements)
            if event is None:
                print(f"Missing event {i}")
                continue
            if event['data']['level'] > 10:
                count_level += 1
            if event['event_type'] == 'item_found':
                count_treasure += 1
            if event['event_type'] == 'level_up':
                count_levelup += 1
        except KeyError as e:
            print(f"Missing key in the event {i} : {e}")
        except Exception as e:
            print(f"Error on the event {i} : {e}")

    for i in range(1, 4):
        try:
            event = parse_events(evenements_exemple)
            if event is None:
                print(f"Missing event {i}")
                continue
            if event['event_type'] == 'kill':
                event_var = "killed monster"
            elif event['event_type'] == 'level_up':
                event_var = "leveled up"
            elif event['event_type'] == 'item_found':
                event_var = "found treasure"
            elif event['event_type'] == 'login':
                event_var = "is connected"
            elif event['event_type'] == 'logout':
                event_var = "is disconnected"
            elif event['event_type'] == 'death':
                event_var = "is death"
            else:
                event_var = "unknown event"
            print(f"Event {i}: Player {event['player']}\
 (level {event['data']['level']}) {event_var}")
        except KeyError as e:
            print(f"Missing key in the event {i} : {e}")
        except Exception as e:
            print(f"Error on the event {i} : {e}")

    fin = time.perf_counter()
    print("...\n")
    print("=== Stream Analytics ===\n")
    print(f'Total events processed: {len(events)}')
    print(f'High-level players (10+): {count_level}')
    print(f'Treasure events: {count_treasure}')
    print(f'Level-up events: {count_levelup}\n')
    print("Memory usage: Constant (streaming)")
    print(f'Processing time: {fin - debut:.6f} seconds\n')
    print("=== Generator Demonstration ===\n")

    try:
        fib_sequence = fibonacci(10)
        print(f'Fibonacci sequence (first 10): {fib_sequence}')
    except Exception as e:
        print(f"Fibonacci Error : {e}")

    try:
        print(f'Prime numbers (first 5): {nombres_premiers(5)}')
    except Exception as e:
        print(f"Prime number error : {e}")
