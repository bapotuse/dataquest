import sys


if __name__ == "__main__":
    final_list = []
    length = len(sys.argv)
    count = 1
    for element in sys.argv:
        final_list.append(element)
    print("=== Command Quest ===")
    if length == 1:
        print("No arguments provided!")
        print(f'Program name:   {sys.argv[0]}')
    else:
        print(f'Program name:   {sys.argv[0]}')
        print(f'Arguments received:  {length - 1}')
        for argument in sys.argv[1:]:
            print(f'Argument {count}:   {argument}')
            count += 1
    print(f'Total arguments:    {length}')
