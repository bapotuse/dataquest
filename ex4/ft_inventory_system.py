import sys


if __name__ == "__main__":
    temp_tab = []
    dictionary = dict()
    total_items = 0

    for element in sys.argv[1:]:
        temp_tab = element.split(':')
        dictionary[temp_tab[0]] = temp_tab[1]

    different_items = len(dictionary.keys())

    for element in dictionary.values():
        total_items += int(element)

    for element in dictionary.keys():
        print(element)

    
    print("=== Inventory System Analysis ===")
    print(f'Total items in inventory:   {total_items}')
    print(f'Unique item types:  {different_items}')



        
    
