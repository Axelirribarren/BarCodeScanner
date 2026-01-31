import sqlite3
import os

class DatabaseManager:
    """
    Manages the connection and operations for the SQLite database.
    """
    def __init__(self, db_name="inventory.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        """Establishes a connection to the database."""
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        """Creates the products table if it does not exist."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    barcode_path TEXT
                )
            """)
            conn.commit()

    def add_product(self, product_data):
        """
        Adds a new product to the database.
        :param product_data: Dictionary containing product details.
        :return: The ID of the inserted product.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO products (code, name, price, stock, barcode_path)
                    VALUES (:code, :name, :price, :stock, :barcode_path)
                """, product_data)
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"[DB Error] Product with code {product_data['code']} already exists.")
            return None
        except Exception as e:
            print(f"[DB Error] {e}")
            return None

    def get_product_by_code(self, code):
        """
        Retrieves a product by its unique code.
        :param code: The product code (e.g., PROD-000001).
        :return: Dictionary product data or None.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE code = ?", (code,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "code": row[1],
                    "name": row[2],
                    "price": row[3],
                    "stock": row[4],
                    "barcode_path": row[5]
                }
            return None

    def get_last_product_id(self):
        """
        Gets the last inserted product ID to help with sequential code generation.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM products")
            result = cursor.fetchone()[0]
            return result if result is not None else 0
