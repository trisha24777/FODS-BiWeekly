'''
This program reads a CSV file and displays its contents in a tabular format.
'''
import csv

def display_csv(filepath):
    """
    Reads a CSV file and prints its contents in a tabular format.

    Args:
        filepath (str): The path to the CSV file.
    """
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # Read the header row
            if header:
                print("| " + " | ".join(header) + " |")
                print("-" * (3 * len(header) + sum(len(col) for col in header))) # Separator line
                for row in reader:
                    print("| " + " | ".join(row) + " |")
            else:
                print("The CSV file is empty.")
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{filepath}'")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

if __name__ == "__main__":
    csv_path = input("Enter the path to the CSV file: ")
    display_csv(csv_path)