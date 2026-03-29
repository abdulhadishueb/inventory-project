import requests

base_url = "http://127.0.0.1:5000"

while True:
    print("\n1. View all items")
    print("2. View one item")
    print("3. Add item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Fetch product from API")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        response = requests.get(f"{base_url}/inventory")
        print(response.json())

    elif choice == "2":
        item_id = input("Enter item id: ")
        response = requests.get(f"{base_url}/inventory/{item_id}")
        print(response.json())

    elif choice == "3":
        name = input("Enter name: ")
        price = input("Enter price: ")
        stock = input("Enter stock: ")

        response = requests.post(
            f"{base_url}/inventory",
            json={
                "name": name,
                "price": float(price),
                "stock": int(stock)
            }
        )
        print(response.json())

    elif choice == "4":
        item_id = input("Enter item id: ")
        name = input("Enter new name: ")
        price = input("Enter new price: ")
        stock = input("Enter new stock: ")

        response = requests.patch(
            f"{base_url}/inventory/{item_id}",
            json={
                "name": name,
                "price": float(price),
                "stock": int(stock)
            }
        )
        print(response.json())

    elif choice == "5":
        item_id = input("Enter item id: ")
        response = requests.delete(f"{base_url}/inventory/{item_id}")
        print(response.json())

    elif choice == "6":
        barcode = input("Enter barcode: ")
        response = requests.get(f"{base_url}/inventory/fetch/{barcode}")
        print(response.json())

    elif choice == "7":
        print("Bye")
        break

    else:
        print("Invalid choice")