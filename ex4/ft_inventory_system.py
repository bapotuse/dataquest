import sys


def parse_inventory(arguments):
    dictionary = dict()
    for element in arguments:
        temp_tab = element.split(':')
        dictionary[temp_tab[0]] = int(temp_tab[1])
    return dictionary


def count_total_items(dictionary):
    total_items = 0
    for element in dictionary.values():
        total_items += element
    return total_items


def print_summary(dictionary, total_items):
    print(f'Total items in inventory:   {total_items}')
    different_items = len(dictionary.keys())
    print(f'Unique item types:  {different_items}\n')


def print_inventory(dictionary, total_items):
    print("=== Current inventory ===")
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        value = dictionary[element]
        percentage = float(value / total_items * 100)
        percentage = format(percentage, ".1f")
        if value == 1:
            print(f'{element}: {dictionary[element]} unit ({percentage}%)')
        elif value > 1:
            print(f'{element}: {dictionary[element]} units ({percentage}%)')


def print_statistics(dictionary):
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

    print(f"Most abundant: {most} ({dictionary[most]} units)")
    print(f"Least abundant: {least} ({dictionary[least]} units)")

## A CONTINUER
def items_categories(dictionary):
    print("=== Item Categories ===")
    scarce_elements = dict()
    moderate_elements = dict()
    for element in sorted(dictionary, key=dictionary.get, reverse=True):
        if dictionary[element] <= 3:
            scarce_elements[] 
        else:
            moderate_elements.append(dictionary[element])



if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    dictionary = parse_inventory(sys.argv[1:])
    total_items = count_total_items(dictionary)

    print_summary(dictionary, total_items)
    print_inventory(dictionary, total_items)
    print_statistics(dictionary)
    items_categories(dictionary)