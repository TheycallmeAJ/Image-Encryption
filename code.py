import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# Encrypts an image file using AES encryption
def encrypt_image(image_path, key_path):
    # Prompt the user to enter the path of the img file
    image_path = input("Enter the path of the image file: ")

    # Read the image file in binary mode
    with open(image_path, "rb") as image_file:
        image = image_file.read()

    # Generate a random encryption key
    key = get_random_bytes(32)

    # Read the image file in binary mode
    with open(image_path, "rb") as image_file:
        image = image_file.read()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.ECB())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Pad the image data to ensure that it is a multiple of the block size
    padded_image = pad(image, AES.block_size)

    # Encrypt the image data
    encrypted_image = encryptor.update(padded_image) + encryptor.finalize()

    # Write the encrypted image data to a new file
    with open("encrypted_image.jpg", "wb") as encrypted_image_file:
        encrypted_image_file.write(encrypted_image)

    # Write the encryption key to a file
    with open(key_path, "wb") as key_file:
        key_file.write(key)

# Decrypts an encrypted image file using AES encryption
def decrypt_image(image_path, key_path):
    # Read the encrypted image file in binary mode
    with open(image_path, "rb") as encrypted_image_file:
        encrypted_image = encrypted_image_file.read()

    # Read the encryption key from a file
    with open(key_path, "rb") as key_file:
        key = key_file.read()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.ECB())

    # Create a decryptor object
    decryptor = cipher.decryptor()

    # Decrypt the encrypted image data
    decrypted_image = decryptor.update(encrypted_image) + decryptor.finalize()

    # Unpad the decrypted image data
    unpadded_image = unpad(decrypted_image, AES.block_size)

    # Write the decrypted image data to a new file
    with open("decrypted_image.jpg", "wb") as decrypted_image_file:
        decrypted_image_file.write(unpadded_image)

# Encrypt an image file
encrypt_image("original_image.jpg", "image_key.bin")

# Decrypt the encrypted image file
decrypt_image("encrypted_image.jpg", "image_key.bin")