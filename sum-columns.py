'''Your task is to write a program that parses a CSV file.
Write a program in Python called "sum-columns.py" where you pass a CSV file name and a column number as arguments. The program should return the sum of values in the column.

Example usage:

sum-columns expenses.csv 3
Example output:

The total 'amount' is 5,384.2
The program will:

Open the CSV file. 
Go over all values in the column.
Print the sum of all the values, formatted nicely (see example above).'''



import csv
import sys

def sum_column(file_name, column_number):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            column_index = column_number - 1  # Convert to 0-based index
            total = 0.0

            for row in reader:
                try:
                    value = float(row[column_index])
                    total += value
                except ValueError:
                    print(f"Skipping non-numeric value: {row[column_index]}")
            
            column_name = header[column_index]
            print(f"The total '{column_name}' is {total:,.2f}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IndexError:
        print(f"Error: Column number {column_number} is out of range for the given file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sum-columns.py <file_name> <column_number>")
    else:
        file_name = sys.argv[1]
        try:
            column_number = int(sys.argv[2])
            sum_column(file_name, column_number)
        except ValueError:
            print("Error: Column number must be an integer.")
