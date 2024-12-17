# lib/cli.py

from helpers import (
    exit_program,
    get_all_products,
    get_all_suppliers,
    get_all_orders,
    add_product
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
            get_all_suppliers()
        elif choice == "3":
            get_all_orders()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display every product")
    print("2. Display every supplier")
    print("3. Get Order's history")


if __name__ == "__main__":
    main()
