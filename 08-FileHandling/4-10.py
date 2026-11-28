import csv

def process_clothing(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                price = float(row['Price'])
                stock = int(row['Stock_Quantity'])
                
                if price < 60 and stock < 40:
                    print(row)
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    process_clothing('clothing.csv')
