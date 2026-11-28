import csv

provinces = {}
try:
    with open('province.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if len(row) >= 2:
                provinces[row[0].strip()] = row[1].strip()
except FileNotFoundError:
    print("File 'province.csv' not found.")

counts = {name: 0 for name in provinces.values()}

try:
    with open('vehicle.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            reg = line.strip()
            if reg and reg[0] in provinces:
                prov_name = provinces[reg[0]]
                counts[prov_name] += 1
except FileNotFoundError:
    print("File 'vehicle.txt' not found.")

for prov, count in counts.items():
    print(f"{prov}: {count}")
