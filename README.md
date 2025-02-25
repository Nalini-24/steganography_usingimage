# steganography_usingimage
# Steganography using LSB and AES Encryption

This project implements *image steganography* using *Least Significant Bit (LSB) encoding* combined with *AES encryption* (via the cryptography library). It allows users to hide a secret message inside an image securely.

## Features
- *Encrypts* the secret message using AES (Fernet encryption)
- *Encodes* the encrypted message into an image using LSB
- *Decodes* and *decrypts* the message from the stego image

## Dependencies
Ensure you have the required Python packages installed:
sh
pip install opencv-python numpy cryptography


## Usage

### 1. Encoding a Message
python
from steganography import encode_image

message = "Hello, this is a secret message!"
encode_image("input_image.png", message)

This will generate a new image stego_image.png with the hidden message.

### 2. Decoding the Message
python
from steganography import decode_image

decode_image("stego_image.png")

This will extract and print the hidden message.

## File Structure

│── steganography.py     
│── README.md            
│── input_image.png      
│── stego_image.png      

## How It Works
1. The message is encrypted using *AES encryption* (Fernet).
2. The encrypted message is converted into *binary*.
3. The binary message is embedded into the *Least Significant Bit (LSB)* of the image pixels.
4. To decode, the process is reversed: binary extraction → decryption → retrieving the original message.

## Notes
- **Ensure input_image.png exists** before running the script.
- The same *encryption key* is needed for decoding (store it safely if required).

## License
This project is open-source under the MIT License.
