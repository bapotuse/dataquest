import sys
import math


class WrongCoordinates(Exception):
    pass


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    try:
        base = (0, 0, 0)
        coor = []
        final_list = []
        split_list = []
        if len(sys.argv) == 2:
            split_list = sys.argv[1].split(',')
            for element in split_list:
                element = int(element)
                final_list.append(element)
            if len(split_list) != 3:
                raise WrongCoordinates('You must enter exactly 3 coordinates, \
example: "1,2,3"')
            print(f'Parsing coordinates:    "{sys.argv[1]}"')
            coor = tuple(final_list)
            print(f'Parsed position:    {coor}')
            distance = math.sqrt(
                (coor[0] - base[0]) ** 2
                + (coor[1] - base[1]) ** 2
                + (coor[2] - base[2]) ** 2)
            distance = format(distance, '.2f')
            print(f'Distance between: {base} and {coor}: {distance}\n')
            print("Unpacking demonstration:")
            print(f'Player at x={coor[0]}, y={coor[1]}, z={coor[2]}')
            print(f'Coordinates at X={coor[0]}, Y={coor[1]}, Z={coor[2]}')
        elif len(sys.argv) == 1 or len(sys.argv) > 2:
            raise WrongCoordinates(f'The number of arguments required is 2, \
please enter 1 argument after the "{sys.argv[0]}"')
    except ValueError as e:
        print(f'Parsing invalid coordinates:    "{sys.argv[1]}"')
        print(f'Error parsing coordinates:  {e}')
        print(f'Error details - Type {type(e).__name__}: {e}, Args  ("{e}",)')
    except WrongCoordinates as e:
        print(f'Error:  {e}')
