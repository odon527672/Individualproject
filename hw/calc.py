import argparse
import configparser
import sys

def calculate(operation, numbers):
    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'average':
        result = sum(numbers) / len(numbers)
    elif operation == 'min':
        result = min(numbers)
    elif operation == 'max':
        result = max(numbers)
    return result

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Perform calculations on a list of numbers.')
    parser.add_argument('-s', '--sum', dest='operation', action='store_const', const='sum',
                        help='Calculate the sum of the numbers')
    parser.add_argument('-a', '--average', dest='operation', action='store_const', const='average',
                        help='Calculate the average of the numbers')
    parser.add_argument('-m', '--min', dest='operation', action='store_const', const='min',
                        help='Find the minimum value in the numbers')
    parser.add_argument('-x', '--max', dest='operation', action='store_const', const='max',
                        help='Find the maximum value in the numbers')
    parser.add_argument('-f', '--float', dest='output_format', action='store_const', const=float,
                        help='Output result as a float')
    parser.add_argument('-i', '--int', dest='output_format', action='store_const', const=int,
                        help='Output result as an integer')

    parser.add_argument('numbers', nargs='+', type=float, help='List of numbers')

    args = parser.parse_args()

    # Load configuration from file if specified
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get default settings from configuration
    default_output_format = config.get('Output', 'format', fallback='float')
    default_operation = config.get('Operation', 'default', fallback='sum')

    # Use default settings if not provided in command-line arguments
    operation = args.operation or default_operation
    output_format = args.output_format or (float if default_output_format == 'float' else int)

    # Perform calculation
    result = calculate(operation, args.numbers)

    # Output result in the specified format
    print(output_format(result))

if __name__ == '__main__':
    main()
