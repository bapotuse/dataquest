import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        if len(sys.argv) > 1:
            final_list = []
            for element in sys.argv[1:]:
                element = int(element)
                final_list.append(element)
            print(f'Scores processed:    {final_list}')
            print(f'Total players:  {len(sys.argv) - 1}')
            print(f'Total score:    {sum(final_list)}')
            moyenne = format(sum(final_list) / len(final_list), '.2f')
            print(f'Average score:  {moyenne}')
            print(f'High score:    {max(final_list)}')
            print(f'Low score:    {min(final_list)}')
            print(f'Score range:    {max(final_list) - min(final_list)}\n')
        else:
            raise ValueError
    except ValueError:
        print(f'No scores provided. Usage:   python3 {sys.argv[0]} <score1> \
<score2> ...')
