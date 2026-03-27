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

        # diccionario corregido (claves en inglés)
        dict_products = {
            "name": product_name,
            "price": price,
            "quantity": quantity,
        }

        lis_inventory.append(dict_products)

        # ✅ ahora sí está dentro del while
        keep_register = input("do you want enter other product? yes/no: ").lower()

#---------------------------------------------------------
def show_inventary():
    if len(lis_inventory) == 0:
        print("inventory empty")
        return

    for products in lis_inventory:
        print(f"|product name: {products['name']}|")
        print(f"|price: {products['price']}|")
        print(f"|quantity: {products['quantity']}|")

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