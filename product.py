from database import DatabaseManager
from barcode_generator import generate_barcode

class ProductManager:
    """
    Handles business logic for products: generation, validation, storage.
    """
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def generate_unique_code(self):
        """
        Generates a sequential unique code like PROD-000001
        based on the last ID in the database.
        """
        last_id = self.db.get_last_product_id()
        new_id = last_id + 1
        return f"PROD-{new_id:06d}"

    def create_product(self, name, price, stock):
        """
        Creates a new product with a unique code and barcode.
        """
        # 1. Generate Code
        code = self.generate_unique_code()
        
        # 2. Generate Barcode Image
        # Returns absolute path
        barcode_path = generate_barcode(code)
        
        # 3. Prepare Data
        product_data = {
            "code": code,
            "name": name,
            "price": float(price),
            "stock": int(stock),
            "barcode_path": barcode_path
        }
        
        # 4. Save to Database
        product_id = self.db.add_product(product_data)
        
        if product_id:
            return product_data
        else:
            return None

    def get_product(self, code):
        """Wrapper to get product from DB."""
        return self.db.get_product_by_code(code)
