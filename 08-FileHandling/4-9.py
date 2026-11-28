import csv

def print_graphic_designers(filename):
    print("GRAPHIC DESIGNERS")
    print("=================")
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Skip header
            
            for row in csv_reader:
                if len(row) >= 3 and row[2] == 'Graphic Designer':
                    print(f"{row[0]} {row[1]},{row[3]}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    print_graphic_designers('it_company.csv')
