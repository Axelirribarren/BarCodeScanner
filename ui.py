import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def print_menu(options):
    print("\nSelect an option:")
    for key, value in options.items():
        print(f"[{key}] {value}")

def get_input(prompt):
    return input(f"{prompt}: ").strip()

def print_product_table(product_dict):
    """
    Pretty prints a single product.
    """
    if not product_dict:
        print("No product data to display.")
        return

    print("-" * 50)
    print(f"Code:       {product_dict['code']}")
    print(f"Name:       {product_dict['name']}")
    print(f"Price:      ${product_dict['price']:.2f}")
    print(f"Stock:      {product_dict['stock']}")
    print(f"Barcode:    {product_dict['barcode_path']}")
    print("-" * 50)
