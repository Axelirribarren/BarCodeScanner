# Barcode Product Management System

## 📋 Description
This project is a complete Python application designed to manage a product inventory using barcodes. It allows you to register items, automatically generate their codes (and associated images), and scan them in real-time using your PC's webcam.

## 🚀 Key Features

*   **Unique Code Generation**: Automatically creates unique sequential codes (e.g., `PROD-000001`) to prevent duplicates.
*   **Barcode Generation**: Creates `.png` images in **Code128** format, saved locally.
*   **Smart Scanner**: Uses the webcam to detect barcodes in real-time.
*   **Visual Identification**:
    *   🟩 **Green Box**: Product exists in the database (Displays Name and Price).
    *   🟥 **Red Box**: Unknown or unregistered product.
*   **Persistent Database**: Uses SQLite for secure and lightweight data storage.

## 🛠 System Requirements

*   **Operating System**: Windows, macOS, or Linux.
*   **Python**: Version 3.10 or higher.
*   **Webcam**: Integrated or external (for the scanning function).

## 📦 Step-by-Step Installation Guide

Follow these steps to install and run the project on your computer:

### 1. Clone or Download the Project
If using Git, open your terminal and run:
```bash
git clone https://github.com/Axelirribarren/BarCodeScanner.git
cd BarCodeScanner
```
*If you don't use Git, download the ZIP file and extract it to a folder.*

### 2. Create a Virtual Environment (Optional but Recommended)
This isolates the project dependencies.
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install the necessary libraries by running:
```bash
pip install -r requirements.txt
```

> **Important Note for Windows**: The `pyzbar` library sometimes requires Visual C++ libraries. If you encounter errors while scanning, install the [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

## 💻 How It Works

To start the application, run the main script:
```bash
python main.py
```

You will see a menu with the following options:

### 1️⃣ Register New Product
*   Select option `1`.
*   Enter the **Name**, **Price**, and Initial **Stock**.
*   ✅ **Result**: The system creates the product and tells you where the barcode image was saved (in the `barcodes/` folder).

### 2️⃣ Start Scanner
*   Select option `2`.
*   A window will open showing your webcam feed.
*   Point the camera at a barcode (you can open the generated image on your phone or print it).
*   The system will draw a box over the code with the product information.
*   Press **'q'** to close the scanner and return to the menu.

## 🏗 Architecture and Technologies

The project follows a modular architecture for easy maintenance:

*   **`main.py`**: Entry point and flow control.
*   **`database.py`**: SQLite database management (`inventory.db`).
*   **`product.py`**: Business logic and unique code generation.
*   **`barcode_generator.py`**: PNG image creation using `python-barcode`.
*   **`scanner.py`**: Computer vision with `opencv-python` and `pyzbar`.
*   **`ui.py`**: Clean and friendly console interface.

---
**Developed with Python 🐍**
