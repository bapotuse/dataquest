import sys


def parse_inventory(arguments: list) -> dict:
    dictionary = dict()
    for element in arguments:
        temp_tab = element.split(':')
        dictionary[temp_tab[0]] = int(temp_tab[1])
    return dictionary


def count_total_items(dictionary) -> int:
    total_items = 0
    for element in dictionary.values():
        total_items += element
    return total_items


def print_summary(dictionary, total_items) -> None:
    print(f'Total items in inventory:   {total_items}')
    different_items = len(dictionary.keys())
    print(f'Unique item types:  {different_items}\n')


def print_inventory(dictionary, total_items) -> None:
    print("=== Current inventory ===")
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        value = dictionary[element]
        percentage = float(value / total_items * 100)
        percentage = format(percentage, ".1f")
        if value == 1:
            print(f'{element}: {dictionary[element]} unit ({percentage}%)')
        elif value > 1:
            print(f'{element}: {dictionary[element]} units ({percentage}%)')


def print_statistics(dictionary) -> None:
    print("\n=== Inventory Statistics ===")
    most = max(dictionary, key=dictionary.get)
    least = min(dictionary, key=dictionary.get)

    if dictionary[most] > 1:
        most_unit = "units"
    else:
        most_unit = "unit"

    if dictionary[least] > 1:
        least_unit = "units"
    else:
        least_unit = "unit"

    print(f"Most abundant: {most} ({dictionary[most]} {most_unit})")
    print(f"Least abundant: {least} ({dictionary[least]} {least_unit})")


def items_categories(dictionary) -> None:
    print("\n=== Item Categories ===")
    scarce_elements = dict()
    moderate_elements = dict()
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        if dictionary[element] <= 3:
            scarce_elements[element] = dictionary[element]
        else:
            moderate_elements[element] = dictionary[element]

    print(f"Moderate: {moderate_elements}")
    print(f"Scarce: {scarce_elements}")


def management_suggestions(dictionary) -> None:
    print("\n=== Management Suggestions ===")
    restock = dict()
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        if dictionary[element] == 1:
            restock[element] = dictionary[element]

    if len(restock) > 0:
        print(f'• Restock needed: {restock}')
    else:
        print('No restock needed')


def check_elements(dictionary, entry) -> str:
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        if element == entry:
            return True


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    dictionary = parse_inventory(sys.argv[1:])
    total_items = count_total_items(dictionary)
    entry = 'sword'

    print_summary(dictionary, total_items)
    print_inventory(dictionary, total_items)
    print_statistics(dictionary)
    items_categories(dictionary)
    management_suggestions(dictionary)
    print("\n=== Dictionary Properties Demo ===")
    print(f'Dictionary keys: {list(dictionary.keys())}')
    print(f'Dictionary values: {list(dictionary.values())}')
    print(f"Sample lookup - '{entry}' in inventory:\
 {check_elements(dictionary, entry)}")
