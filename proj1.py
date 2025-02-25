import cv2
import numpy as np
import binascii
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_image(image_path, secret_message):
    img = cv2.imread(image_path)
    secret_message = cipher.encrypt(secret_message.encode()).decode()
    binary_secret = text_to_binary(secret_message) + '1111111111111110'  # End marker
    data_index = 0
    
    for row in img:
        for pixel in row:
            for color in range(3):  # Iterate over R, G, B
                if data_index < len(binary_secret):
                    pixel[color] = int(pixel[color]) & ~1 | int(binary_secret[data_index])
                    data_index += 1
                else:
                    break
    
    cv2.imwrite('stego_image.png', img)
    print("Message encoded and saved as stego_image.png")

def decode_image(image_path):
    img = cv2.imread(image_path)
    binary_data = ""
    
    for row in img:
        for pixel in row:
            for color in range(3):
                binary_data += str(pixel[color] & 1)
                if binary_data.endswith('1111111111111110'):
                    binary_data = binary_data[:-16]
                    secret_message = cipher.decrypt(binary_to_text(binary_data).encode()).decode()
                    print("Decoded Message:", secret_message)
                    return

# Example Usage
message = "Hello, this is a secret message!"
encode_image("panther.png", message)
decode_image("stego_image.png")