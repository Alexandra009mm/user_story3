from services import *
from files import *

keep_register = "yes"

while keep_register == "yes":
    try:
        option= (input(f"""
    ╔════════════════════════════════════════════════════════════╗
            WELCOME TO THE SALES RECORD RIWI STORE!!             
    ╚════════════════════════════════════════════════════════════╝
                 ╔════════════════════════════╗
    ------------------------MAIN MENU ---------------------------------
                 ╚════════════════════════════╝
                     1. Add product.
                     2. show inventory.
                     3. Search product.
                     4. Update product.
                     5. Save CSV.
                     6. Remove product.
                     7. calculate statistics.
                     8. Load CSV 
                     9. Exit.
    --------------------------------------------------------------                   
    enter a option => """)).strip()
        

                            
        if option =="1":
            add_products()


        elif option == "2":
            show_lis_inventory()

        elif option == "3":
            search_products()

        elif option == "4":
            update_product()

        elif option == "5":
            save_csv(lis_inventory)
            print("Product saved successfully!")

        elif option == "6":
            delete_product()

        elif option == "7":
            calculate_statistics()

        elif option == "8":
            load_csv(lis_inventory,archivo="database.csv")

        elif option == "9":
            print ("Exting...")
            print()
            keep_register = "no"

    except ValueError:
            print("Error, enter option invalide")