import json

def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)['reservations']

def count_rooms(reservations):
    return len(reservations)

def count_paid(reservations):
    return sum(1 for r in reservations if r['paid'])

def count_unpaid(reservations):
    return sum(1 for r in reservations if not r['paid'])

def total_value(reservations, paid_status):
    return sum(r['nights'] * r['price_per_night'] for r in reservations if r['paid'] == paid_status)

if __name__ == "__main__":
    reservations = load_reservations('reservations.json')
    print(f"Number of rooms: {count_rooms(reservations)}")
    print(f"Number of paid reservations: {count_paid(reservations)}")
    print(f"Number of unpaid reservations: {count_unpaid(reservations)}")
    print(f"Total value of paid reservations: {total_value(reservations, True):.2f}")
    print(f"Total value of unpaid reservations: {total_value(reservations, False):.2f}")
