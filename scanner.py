import cv2
import numpy as np
from pyzbar.pyzbar import decode

class BarcodeScanner:
    def __init__(self, product_lookup_callback):
        """
        :param product_lookup_callback: Function that takes a code string and returns product dict or None.
        """
        self.lookup_callback = product_lookup_callback

    def start_scanning(self):
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        print("Starting Scanner... Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Decode barcodes
            decoded_objects = decode(frame)
            
            for obj in decoded_objects:
                # Extract data
                code_data = obj.data.decode('utf-8')
                rect = obj.rect
                
                # Draw bounding box
                cv2.rectangle(frame, 
                              (rect.left, rect.top), 
                              (rect.left + rect.width, rect.top + rect.height), 
                              (0, 255, 0), 2)
                
                # Lookup product
                product = self.lookup_callback(code_data)
                
                # Prepare display text
                if product:
                    text_display = f"{product['name']} | ${product['price']}"
                    color = (0, 255, 0) # Green
                else:
                    text_display = f"Unknown: {code_data}"
                    color = (0, 0, 255) # Red

                # Put text above the barcode
                cv2.putText(frame, text_display, 
                            (rect.left, rect.top - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                # Also print to console if you want (optional)
                # print(f"Scanned: {code_data}")

            cv2.imshow('Barcode Scanner', frame)

            # Exit condition
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
