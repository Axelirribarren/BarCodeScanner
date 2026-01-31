import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(code, output_dir="barcodes"):
    """
    Generates a Code128 barcode for the given code.
    
    :param code: The unique product code.
    :param output_dir: Directory to save the barcode image.
    :return: Absolute path to the saved image file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Use Code128 as requested
    code128 = barcode.get_barcode_class('code128')
    
    # Create barcode object. We do NOT want text below it? 
    # Usually text below is good for human readability.
    my_barcode = code128(code, writer=ImageWriter())
    
    # Save the barcode
    # python-barcode saves with the extension automatically appended, so we don't add .png here
    # We want to save it as output_dir/code
    filename = os.path.join(output_dir, code)
    
    # save() returns the full path with extension
    saved_path = my_barcode.save(filename)
    
    return os.path.abspath(saved_path)
