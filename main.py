from database import DatabaseManager
from product import ProductManager
from scanner import BarcodeScanner
from ui import clear_screen, print_header, print_menu, get_input, print_product_table
import sys
import time

def main():
    # Initialize Modules
    db = DatabaseManager()
    pm = ProductManager(db)
    scanner = BarcodeScanner(product_lookup_callback=pm.get_product)

    while True:
        clear_screen()
        print_header("Barcode Product Management System")
        
        menu_options = {
            "1": "Register New Product",
            "2": "Start Barcode Scanner",
            "3": "Exit"
        }
        
        print_menu(menu_options)
        choice = get_input("Enter choice")

        if choice == "1":
            print("\n--- Register Product ---")
            name = get_input("Product Name")
            try:
                price = float(get_input("Price"))
                stock = int(get_input("Stock"))
                
                print("Generating Unique Code and Barcode...")
                product = pm.create_product(name, price, stock)
                
                if product:
                    print("\nSuccess! Product Created:")
                    print_product_table(product)
                    print(f"\nBarcode image saved at: {product['barcode_path']}")
                else:
                    print("\nError creating product.")
            except ValueError:
                print("Invalid input for price or stock.")
            
            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\n--- Scanner Starting ---")
            print("A webcam window will open.")
            print("Ensure the webcam is connected.")
            input("Press Enter to launch scanner...")
            scanner.start_scanning()

        elif choice == "3":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice, try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
