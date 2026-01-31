# Barcode Product Management System

## 🚀 Features
- **Unique Code Generation**: Automatically creates sequential codes (`PROD-000001`).
- **Barcode Generation**: Creates Code128 PNGs for each product.
- **Real-time Scanning**: Uses webcam to detect and identify products.
- **Database**: Stores all data in a local SQLite file (`inventory.db`).

## 🛠️ Installation

1.  **Install Python 3.10+**
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If you get an error related to `zbar` or `DLL load failed`, install the Visual C++ Redistributable.*

## ▶️ How to Run

Execute the main script:
```bash
python main.py
```

## 📂 Project Structure
- `main.py`: Entry point.
- `database.py`: Database operations.
- `product.py`: Product logic.
- `scanner.py`: Webcam scanning logic.
- `barcode_generator.py`: Generates PNG images.
- `ui.py`: Console definitions.
- `barcodes/`: Folder where images are saved.
# BarCodeScanner
