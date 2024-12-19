# lib/cli.py

from helpers import (
    exit_program,
    
    get_all_products,
    add_product,
    delete_product,
    get_product_by_id,
    low_stock_products,
    update_product,
    filter_products_by_category,
    find_supplier_products,
   
    get_all_suppliers,
    add_suplier,
    delete_suplier,
    get_supplier_by_id,
    update_supplier,
   
    get_all_orders,
    make_order,
    find_order_by_id,
    delete_order,
)

def main():
    while True:
        menu()
        choice = input("> ")
        
      
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            get_product_by_id()
        elif choice == "5":
            low_stock_products()
        elif choice == "6":
            update_product()
        elif choice == "7":
            filter_products_by_category()
        elif choice == "8":
            find_supplier_products()
        
        
        elif choice == "9":
            get_all_suppliers()
        elif choice == "10":
            add_suplier()
        elif choice == "11":
            delete_suplier()
        elif choice == "12":
            get_supplier_by_id()
        elif choice == "13":
            update_supplier()
        
        
        elif choice == "14":
            get_all_orders()
        elif choice == "15":
            make_order()
        elif choice == "16":
            find_order_by_id()
        elif choice == "17":
            delete_order()
        
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("\n 0. Exit the program")
    
    
    print("\n--- Product Management ---")
    print("1. Display every product")
    print("2. Add product")
    print("3. Delete product")
    print("4. Get product by ID")
    print("5. Display products with less than 10 quantity remaining")
    print("6. Update product")
    print("7. Filter products by category")
    print("8. Display products for a supplier")
    
  
    print("\n--- Supplier Management ---")
    print("9. Display every supplier")
    print("10. Add supplier")
    print("11. Delete supplier")
    print("12. Get supplier by ID")
    print("13. Update supplier")
    
    
    print("\n--- Order Management ---")
    print("14. Get order history")
    print("15. Make an order")
    print("16. Get order by ID")
    print("17. Delete order")

if __name__ == "__main__":
    main()
