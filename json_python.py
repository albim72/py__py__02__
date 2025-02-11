import json

# Przykładowy złożony plik JSON
data = {
    "users": [
        {
            "id": 1,
            "name": "Jan Kowalski",
            "email": "jan.kowalski@example.com",
            "orders": [
                {"order_id": 101, "product_id": 2001, "quantity": 2},
                {"order_id": 102, "product_id": 2003, "quantity": 1}
            ]
        },
        {
            "id": 2,
            "name": "Anna Nowak",
            "email": "anna.nowak@example.com",
            "orders": [
                {"order_id": 103, "product_id": 2002, "quantity": 5}
            ]
        }
    ],
    "products": [
        {"product_id": 2001, "name": "Laptop", "price": 3500.0},
        {"product_id": 2002, "name": "Smartphone", "price": 2500.0},
        {"product_id": 2003, "name": "Tablet", "price": 1500.0}
    ]
}

# Zapis do pliku JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Odczyt z pliku JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Parsowanie i manipulacja danymi
users = loaded_data["users"]
products = {p["product_id"]: p for p in loaded_data["products"]}

# Wypisanie zamówień użytkowników ze szczegółami produktów
def print_orders():
    for user in users:
        print(f"Użytkownik: {user['name']} ({user['email']})")
        for order in user["orders"]:
            product = products.get(order["product_id"], {})
            print(f"  Zamówienie {order['order_id']}: {product.get('name', 'Nieznany produkt')} x{order['quantity']} - {product.get('price', 0) * order['quantity']} PLN")
        print()

print_orders()

# Dodanie nowego użytkownika
def add_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email, "orders": []})
    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)

add_user(3, "Piotr Zieliński", "piotr.zielinski@example.com")
print_orders()
