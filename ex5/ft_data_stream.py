import time


events = [
    {'id': 1, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-01T23:17', 'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}},
    {'id': 2, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-22T23:57', 'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}},
    {'id': 3, 'player': 'diana', 'event_type': 'login', 'timestamp': '2024-01-01T02:13', 'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}},
    {'id': 4, 'player': 'alice', 'event_type': 'level_up', 'timestamp': '2024-01-07T22:41', 'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}},
    {'id': 5, 'player': 'bob', 'event_type': 'death', 'timestamp': '2024-01-19T08:51', 'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}},
    {'id': 6, 'player': 'charlie', 'event_type': 'kill', 'timestamp': '2024-01-05T06:48', 'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}},
    {'id': 7, 'player': 'diana', 'event_type': 'login', 'timestamp': '2024-01-12T11:38', 'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}},
    {'id': 8, 'player': 'eve', 'event_type': 'login', 'timestamp': '2024-01-30T12:05', 'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}},
    {'id': 9, 'player': 'charlie', 'event_type': 'level_up', 'timestamp': '2024-01-07T22:04', 'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}},
    {'id': 10, 'player': 'alice', 'event_type': 'kill', 'timestamp': '2024-01-28T03:24', 'data': {'level': 5, 'score_delta': 364, 'zone': 'pixel_zone_3'}},
    {'id': 11, 'player': 'bob', 'event_type': 'item_found', 'timestamp': '2024-01-12T06:42', 'data': {'level': 12, 'score_delta': -27, 'zone': 'pixel_zone_5'}},
    {'id': 12, 'player': 'frank', 'event_type': 'logout', 'timestamp': '2024-01-18T23:15', 'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}},
    {'id': 13, 'player': 'charlie', 'event_type': 'level_up', 'timestamp': '2024-01-23T17:14', 'data': {'level': 44, 'score_delta': 232, 'zone': 'pixel_zone_1'}},
    {'id': 14, 'player': 'bob', 'event_type': 'login', 'timestamp': '2024-01-26T10:25', 'data': {'level': 18, 'score_delta': -33, 'zone': 'pixel_zone_2'}},
    {'id': 15, 'player': 'eve', 'event_type': 'item_found', 'timestamp': '2024-01-11T06:41', 'data': {'level': 32, 'score_delta': 305, 'zone': 'pixel_zone_4'}},
    {'id': 16, 'player': 'bob', 'event_type': 'kill', 'timestamp': '2024-01-05T07:47', 'data': {'level': 36, 'score_delta': 451, 'zone': 'pixel_zone_3'}},
    {'id': 17, 'player': 'frank', 'event_type': 'level_up', 'timestamp': '2024-01-14T18:25', 'data': {'level': 24, 'score_delta': 124, 'zone': 'pixel_zone_2'}},
    {'id': 18, 'player': 'eve', 'event_type': 'death', 'timestamp': '2024-01-03T01:55', 'data': {'level': 8, 'score_delta': 56, 'zone': 'pixel_zone_2'}},
    {'id': 19, 'player': 'frank', 'event_type': 'death', 'timestamp': '2024-01-20T02:24', 'data': {'level': 25, 'score_delta': 379, 'zone': 'pixel_zone_5'}},
    {'id': 20, 'player': 'charlie', 'event_type': 'level_up', 'timestamp': '2024-01-28T00:43', 'data': {'level': 47, 'score_delta': 17, 'zone': 'pixel_zone_5'}},
    {'id': 21, 'player': 'charlie', 'event_type': 'item_found', 'timestamp': '2024-01-11T03:18', 'data': {'level': 28, 'score_delta': 61, 'zone': 'pixel_zone_4'}},
    {'id': 22, 'player': 'alice', 'event_type': 'item_found', 'timestamp': '2024-01-29T23:16', 'data': {'level': 33, 'score_delta': 82, 'zone': 'pixel_zone_5'}},
    {'id': 23, 'player': 'alice', 'event_type': 'item_found', 'timestamp': '2024-01-10T20:32', 'data': {'level': 39, 'score_delta': 103, 'zone': 'pixel_zone_2'}},
    {'id': 24, 'player': 'charlie', 'event_type': 'logout', 'timestamp': '2024-01-18T16:58', 'data': {'level': 1, 'score_delta': 231, 'zone': 'pixel_zone_4'}},
    {'id': 25, 'player': 'alice', 'event_type': 'login', 'timestamp': '2024-01-30T11:56', 'data': {'level': 20, 'score_delta': 145, 'zone': 'pixel_zone_1'}},
    {'id': 26, 'player': 'bob', 'event_type': 'level_up', 'timestamp': '2024-01-03T02:46', 'data': {'level': 32, 'score_delta': -30, 'zone': 'pixel_zone_5'}},
    {'id': 27, 'player': 'bob', 'event_type': 'logout', 'timestamp': '2024-01-22T15:35', 'data': {'level': 11, 'score_delta': 171, 'zone': 'pixel_zone_5'}},
    {'id': 28, 'player': 'eve', 'event_type': 'death', 'timestamp': '2024-01-07T17:48', 'data': {'level': 47, 'score_delta': 105, 'zone': 'pixel_zone_3'}},
    {'id': 29, 'player': 'diana', 'event_type': 'item_found', 'timestamp': '2024-01-21T11:28', 'data': {'level': 34, 'score_delta': 362, 'zone': 'pixel_zone_1'}},
    {'id': 30, 'player': 'bob', 'event_type': 'logout', 'timestamp': '2024-01-03T10:01', 'data': {'level': 38, 'score_delta': 467, 'zone': 'pixel_zone_2'}},
    {'id': 31, 'player': 'eve', 'event_type': 'logout', 'timestamp': '2024-01-01T02:45', 'data': {'level': 41, 'score_delta': -40, 'zone': 'pixel_zone_2'}},
    {'id': 32, 'player': 'alice', 'event_type': 'login', 'timestamp': '2024-01-28T10:04', 'data': {'level': 33, 'score_delta': 143, 'zone': 'pixel_zone_3'}},
    {'id': 33, 'player': 'frank', 'event_type': 'death', 'timestamp': '2024-01-07T17:08', 'data': {'level': 47, 'score_delta': 484, 'zone': 'pixel_zone_5'}},
    {'id': 34, 'player': 'diana', 'event_type': 'logout', 'timestamp': '2024-01-26T15:51', 'data': {'level': 27, 'score_delta': 94, 'zone': 'pixel_zone_1'}},
    {'id': 35, 'player': 'alice', 'event_type': 'item_found', 'timestamp': '2024-01-14T11:27', 'data': {'level': 27, 'score_delta': 378, 'zone': 'pixel_zone_1'}},
    {'id': 36, 'player': 'frank', 'event_type': 'item_found', 'timestamp': '2024-01-21T03:03', 'data': {'level': 26, 'score_delta': 247, 'zone': 'pixel_zone_1'}},
    {'id': 37, 'player': 'bob', 'event_type': 'logout', 'timestamp': '2024-01-07T17:28', 'data': {'level': 9, 'score_delta': 332, 'zone': 'pixel_zone_2'}},
    {'id': 38, 'player': 'charlie', 'event_type': 'death', 'timestamp': '2024-01-08T02:28', 'data': {'level': 36, 'score_delta': 0, 'zone': 'pixel_zone_1'}},
    {'id': 39, 'player': 'frank', 'event_type': 'level_up', 'timestamp': '2024-01-27T00:05', 'data': {'level': 49, 'score_delta': 142, 'zone': 'pixel_zone_2'}},
    {'id': 40, 'player': 'diana', 'event_type': 'death', 'timestamp': '2024-01-16T06:55', 'data': {'level': 26, 'score_delta': -40, 'zone': 'pixel_zone_2'}},
    {'id': 41, 'player': 'diana', 'event_type': 'login', 'timestamp': '2024-01-13T08:59', 'data': {'level': 30, 'score_delta': 192, 'zone': 'pixel_zone_4'}},
    {'id': 42, 'player': 'frank', 'event_type': 'item_found', 'timestamp': '2024-01-26T17:42', 'data': {'level': 46, 'score_delta': 398, 'zone': 'pixel_zone_2'}},
    {'id': 43, 'player': 'bob', 'event_type': 'kill', 'timestamp': '2024-01-07T01:37', 'data': {'level': 48, 'score_delta': 455, 'zone': 'pixel_zone_1'}},
    {'id': 44, 'player': 'frank', 'event_type': 'kill', 'timestamp': '2024-01-02T01:37', 'data': {'level': 31, 'score_delta': 414, 'zone': 'pixel_zone_5'}},
    {'id': 45, 'player': 'bob', 'event_type': 'login', 'timestamp': '2024-01-17T02:54', 'data': {'level': 12, 'score_delta': -30, 'zone': 'pixel_zone_5'}},
    {'id': 46, 'player': 'alice', 'event_type': 'item_found', 'timestamp': '2024-01-28T07:25', 'data': {'level': 8, 'score_delta': 483, 'zone': 'pixel_zone_2'}},
    {'id': 47, 'player': 'eve', 'event_type': 'level_up', 'timestamp': '2024-01-02T19:05', 'data': {'level': 27, 'score_delta': 497, 'zone': 'pixel_zone_5'}},
    {'id': 48, 'player': 'eve', 'event_type': 'kill', 'timestamp': '2024-01-30T08:13', 'data': {'level': 43, 'score_delta': 221, 'zone': 'pixel_zone_2'}},
    {'id': 49, 'player': 'charlie', 'event_type': 'death', 'timestamp': '2024-01-05T21:41', 'data': {'level': 20, 'score_delta': 368, 'zone': 'pixel_zone_3'}},
    {'id': 50, 'player': 'alice', 'event_type': 'login', 'timestamp': '2024-01-15T19:36', 'data': {'level': 7, 'score_delta': -25, 'zone': 'pixel_zone_5'}},
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
            print(f"Event {i}: Player {event['player']} (level {event['data']['level']}) {event_var}")
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
        print(f'Prime numbers (first 5): {nombres_premiers()}')
    except Exception as e:
        print(f"Prime number error : {e}")
    print("=== Game Data Stream Processor ===\n")
    print(f'Processing {len(events)} game events...\n')
    debut = time.perf_counter()
    evenements_exemple = trier_evenements(events)
    evenements = trier_evenements(events)
    count_level = 0
    count_treasure = 0
    count_levelup = 0
    for i in range(len(events)):
        event = parse_events(evenements)
        if event['data']['level'] > 10:
            count_level += 1
        if event['event_type'] == 'item_found':
            count_treasure += 1
        if event['event_type'] == 'level_up':
            count_levelup += 1
    for i in range(1, 4):
        event = parse_events(evenements_exemple)
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
        print(f"Event {i}: Player {event['player']}\
 (level {event['data']['level']}) {event_var}")
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
    fib_sequence = fibonacci(10)
    print(f'Fibonacci sequence (first 10): {fibonacci(10)}')
    print(f'Prime numbers (first 10): {nombres_premiers(5)}')
