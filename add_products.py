#Esta lista la a contener el inventario con los diccionarios de 
lis_inventory = []
counter = 0


#este va a ser el diccionario con los datos del producto, este se agrega a la lista


#----------------------------------------------------------------------------------------
def add_products():
    keep_register = "yes" #this variable is to enter the loop  principale of funtion 

    while keep_register == "yes":#this is the loop principale
        product_name = ""

        
        while product_name == "":#here valide that product name
            print()
            product_name = input("enter a product name: ")
            if product_name == "":
                print("Error, this field must be filled ")

        price = 0 

        while price <=0:#here valide that price
            print()
            price = float(input("enter the price: "))
            if price <= 0:
                print("Error, enter a number")

        quantity = 0

        while quantity <= 0:#here valide that quantity
            print()
            quantity = int(input("Enter a quantity"))
            if quantity <=0:
                print("Error, enter a quantity")
                
        #this diccionary is for save data products in a list

        dict_products = {
            "nombre": product_name,
            "precio": price, 
            "cantidad": quantity,
            }

        lis_inventory.append(dict_products)#here add to list inventory

    keep_register = input("do you want enter other product? yes/no: ")

#-------------------------------------------------------------------------------------------
def show_inventary():
    for products in lis_inventory:
        print(f"|product name: {products['nombre']}|")
        print(f"|price: {products['price']}|")
        print(f"|quantity: {products['quantity']}|")

#--------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------


def update_product():
    if len(lis_inventory) == 0:# si la lista está vacía
        print("inventory empty")
        return 
                                # pedir nombre del producto
    product_name = input("enter product name: ").lower()

                                # pedir qué quiere cambiar
    data = input("what do you want to update (name, price, quantity): ").lower()

    # recorrer la lista
    for product in lis_inventory:

        # si encuentra el producto
        if product["name"].lower() == product_name:

            # verificar que la clave exista
            if data in product:

                # pedir nuevo valor
                new_value = input("enter new value: ")

                # convertir si es número
                if data == "price":
                    new_value = float(new_value)
                elif data == "quantity":
                    new_value = int(new_value)

                # actualizar
                product[data] = new_value

                print("updated successfully")

            else:
                print("invalid data")

            return  # termina aquí

    # si no lo encontró
    print("product not found")


            
            


        


        

        
        
    


    
       

