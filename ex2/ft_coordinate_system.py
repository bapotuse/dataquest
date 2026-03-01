import sys
import math


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coordonnees = []
    pos = (0, 0, 0)
    try:
        if len(sys.argv) == 2:
            print(f'Parsing coordinates: "{sys.argv[1]}"')
            for param in sys.argv[1:]:
                coordonnees.append(param)
            coordonnees = ''.join(coordonnees)
            coordonnees = coordonnees.split(',')
            for i in range(len(coordonnees)):
                coordonnees[i] = int(coordonnees[i])
            x = coordonnees[0]
            y = coordonnees[1]
            z = coordonnees[2]
            coordonnees = tuple(coordonnees)
            print(f'Position created: {coordonnees}')
            distance = math.sqrt(
                (x - pos[0]) ** 2
                + (y - pos[1]) ** 2
                + (z - pos[2]) ** 2)
            print(f'Distance between {pos} and {coordonnees}: {distance:.2f}')
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
        print(f'Error parsing coordinates: {e}')
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
