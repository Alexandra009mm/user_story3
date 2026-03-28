import csv

def save_csv(lis_inventory, archivo="database.csv"):
    with open(archivo, "w", newline="") as csvfile:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in lis_inventory:
                writer.writerow(product)



def load_csv(lis_inventory, archivo="database.csv"):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            next(file)
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, price, quantity = line.split(",")
                price = float(price)
                quantity = int(quantity)

                exists = False
                for product in lis_inventory:
                    if (product["name"] == name and
                        product["price"] == price and
                        product["quantity"] == quantity):
                        exists = True
                        break

                if not exists:
                    lis_inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity  
                    })

        print(f"Inventory loaded from: {archivo}")  

    except FileNotFoundError:
        print(f"No file found at {archivo}, starting with empty inventory.")

    except Exception as e:
        print(f"Error loading CSV: {e}")