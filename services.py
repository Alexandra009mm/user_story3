# lista del inventario
lis_inventory = []

#---------------------------------------------------------

def add_products():
    keep_register = "yes"

    while keep_register == "yes":

        product_name = ""
        while product_name == "":
            print()
            product_name = input("enter a product name: ")
            if product_name == "":
                print("Error, this field must be filled")

        price = 0
        while price <= 0:
            print()
            price = float(input("enter the price: "))
            if price <= 0:
                print("Error, enter a valid number")

        quantity = 0
        while quantity <= 0:
            print()
            quantity = int(input("Enter a quantity: "))
            if quantity <= 0:
                print("Error, enter a valid quantity")

        dict_products = {
            "name": product_name,
            "price": price,
            "quantity": quantity,
        }

        lis_inventory.append(dict_products)

        keep_register = input("do you want enter other product? yes/no: ").lower()

       



#---------------------------------------------------------
def show_lis_inventory():
    if len(lis_inventory) == 0:
        print("inventory empty")
        return

    for products in lis_inventory:
        print()
        print("the states of your inventory:")
        print(f"\n|product name: {products['name']}|")
        print(f"\n|price: {products['price']}|")
        print(f"\n|quantity: {products['quantity']}|")
#---------------------------------------------------------
def search_products():

    if len(lis_inventory) == 0:
        print("inventory empty")
        return

    product_name = input("enter product name: ").lower()
    data = input("what do you want to see (name, price, quantity): ").lower()

    for product in lis_inventory:
        if product["name"].lower() == product_name:

            if data in product:
                print(product[data])
            else:
                print("invalid data")

            return

    print("product not found")

#---------------------------------------------------------
def update_product():

    if len(lis_inventory) == 0:
        print("inventory empty")
        return

    product_name = input("enter product name: ").lower()
    data = input("what do you want to update (name, price, quantity): ").lower()

    for product in lis_inventory:
        if product["name"].lower() == product_name:

            if data in product:

                new_value = input("enter new value: ")

                if data == "price":
                    new_value = float(new_value)
                elif data == "quantity":
                    new_value = int(new_value)

                product[data] = new_value
                print("updated successfully")

            else:
                print("invalid data")

            return

    print("product not found")


def delete_product ():
    name =input ("\nEnter the name of the product to delete: ").lower()

    for product in lis_inventory:
        if product["name"].lower() == name:
            
            confirm = input(f"  Are you sure you want to delete '{product['name']}'? (yes/no): ").lower()
            if confirm == "yes":
                lis_inventory.remove(product)
                print(f"  Product '{name}' deleted successfully!\n")
            else:
                print(" Deletion cancelled.\n")
            return

    print(f" Product '{name}' not found.\n")


def calculate_statistics ():
    
    if not lis_inventory:
        print("  No products to calculate statistics.\n")
        return

    total_units = 0
    total_value = 0
    most_expensive = lis_inventory[0]
    most_stock = lis_inventory[0]

    for product in lis_inventory:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

        if product["price"] > most_expensive["price"]:
            most_expensive = product

        if product["quantity"] > most_stock["quantity"]:
            most_stock = product

    print("\n" + "=" * 60)
    print("  INVENTORY STATISTICS")
    print("-" * 60)
    print(f"  Total units in stock  : {total_units}")
    print(f"  Total inventory value : ${total_value:.2f}")
    print(f"  Most expensive product: {most_expensive['name']} (${most_expensive['price']:.2f})")
    print(f"  Highest stock product : {most_stock['name']} ({most_stock['quantity']} units)")
    print("=" * 60)