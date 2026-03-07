import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    temp_tab = []
    dictionary = dict()
    total_items = 0

    # parser les elements dans le dictionnaire
    for element in sys.argv[1:]:
        temp_tab = element.split(':')
        dictionary[temp_tab[0]] = temp_tab[1]

    # savoir le nombre d'items
    for element in dictionary.values():
        total_items += int(element)
    print(f'Total items in inventory:   {total_items}')

    # savoir la taille des elements
    different_items = len(dictionary.keys())
    print(f'Unique item types:  {different_items}\n')

    print("=== Current inventory ===")
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        value = int(dictionary[element])
        purcentage = float(value / total_items * 100)
        purcentage = format(purcentage, ".1f")
        if value == 1:
            print(f'{element}: {dictionary[element]} unit ({purcentage}%)')
        elif value > 1:
            print(f'{element}: {dictionary[element]} units ({purcentage}%)')

    print("\n=== Inventory Statistics ===")
    for element in dictionary.keys():
        

