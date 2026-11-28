import json

product = {}
product['name'] = input("Enter product name: ")
product['price'] = round(float(input("Enter product price: ")), 2)
paid_input = input("Is the product paid? (yes/no): ").strip().lower()
product['paid'] = (paid_input == 'yes')

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print("Saved to product.json")
