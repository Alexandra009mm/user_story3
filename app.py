from services import add_products, show_inventary, search_products, update_product

 

rn = "yes"
while rn == "yes":
    print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")
    print()
    print("-----------MENU-----------")
    print("1. Add product.")
    print("2. show inventory.")
    print("3. Search product.")
    print("4. Save  CSV.")
    print("5. Delete product.")
    print("6. Calculate statistics.")
    print("7. Save CSV.")
    print("8. Load CSV ")
    print("9. Exit.")
    print({"="*60})

    keep_register = "yes"

    while keep_register == "yes":


            option = ""
            while option == "":
                    try:
                        print()
                        option = input("enter a option => ")
                        if option == ("1","2", "3","4","5","6","7","8","9"):
                            break
                        else:
                             continue
                    except ValueError:
                         print("Error, enter option invalide")
                        
            if option =="1":
                add_products()


            elif option == "2":
                 show_inventary()
                 
            elif option == "3":
                 search_products()

            elif option == "4":
                 update_product()
                 
                 


