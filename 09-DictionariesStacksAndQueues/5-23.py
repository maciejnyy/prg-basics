import json

try:
    with open('euro.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
    print("=" * 44)
    for rate in data['rates']:
        print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:.4f}")
except FileNotFoundError:
    print("File 'euro.json' not found. Please download the last 10 EUR rates from api.nbp.pl first.")
