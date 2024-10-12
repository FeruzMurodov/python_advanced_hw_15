import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing of number and string with additional options')
    parser.add_argument('number', type=int, help='Number for output')
    parser.add_argument('text', type=str, help='String for output')
    parser.add_argument('-v', '--verbose', action='store_true', help='Addition info about procedure')
    parser.add_argument('--repeat', type=int, default=1, help="Number of string's repetitions")
    args = parser.parse_args()
    if args.verbose:
        print(f'Received arguments: number={args.number}, text="{args.text}", repeat={args.repeat}')
    print(f'Number: {args.number}, Text: "{args.text * args.repeat}"')
