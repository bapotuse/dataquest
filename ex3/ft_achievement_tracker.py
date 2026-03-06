def unique_achievements(liste: list):
    final_set = set()
    for achievements in liste:
        final_set = final_set.union(achievements)
    return final_set


def common_achievement(liste: list):
    final_set = liste[0]
    for achievements in liste[1:]:
        final_set = final_set.intersection(achievements)
    return final_set


def rare_achievement(liste):
    all = set()
    doubles = set()

    for people in liste:
        for achievement in people:
            if achievement in all:
                doubles.add(achievement)
            else:
                all.add(achievement)
    return all - doubles


def compare_achievement(set1: set, set2: set):
    liste = []
    for achievement in set1:
        if achievement in set1 and achievement in set2:
            liste.append(achievement)
    liste = set(liste)
    return liste


def unique_single(people_base, people_dest):
    return people_base.difference(people_dest)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = set(
        ['first_kill',
         'level_10',
         'treasure_hunter',
         'speed_demon'])
    bob = set(
        ['first_kill',
         'level_10',
         'boss_slayer',
         'collector'])
    charlie = set(
        ['level_10',
         'treasure_hunter',
         'boss_slayer',
         'speed_demon',
         'perfectionist'])
    liste = [alice, bob, charlie]
    print(f'Player alice achievements: {alice}')
    print(f'Player bob achievements: {bob}')
    print(f'Player charlie achievements: {charlie}\n')
    print("=== Achievement Analytics ===")
    print(f'All unique achievements: {unique_achievements(liste)}')
    print(f'Total unique achievements: {len(unique_achievements(liste))}\n')
    print(f'Common to all players: {common_achievement(liste)}')
    print(f"Rare achievements (1 player): {rare_achievement(liste)}\n")
    print(f'Alice vs Bob common:    {compare_achievement(alice, bob)}')
    print(f'Alice unique: {unique_single(alice, bob)}')
    print(f'Bob unique: {unique_single(bob, alice)}')
