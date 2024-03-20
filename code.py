import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# Encrypt an img file using AES encryption
def encrypt_image(image_path, key_path):
    with open(image_path, "rb") as image_file:
        image = image_file.read()

    key = get_random_bytes(32)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    encrypted_image = encryptor.update(image) + encryptor.finalize()

    with open(key_path, "wb") as key_file:
        key_file.write(key)

    with open("encrypted_image.jpg", "wb") as encrypted_image_file:
        encrypted_image_file.write(encrypted_image)

def decrypt_image(image_path, key_path):
    with open(image_path, "rb") as encrypted_image_file:
        encrypted_image = encrypted_image_file.read()

    with open(key_path, "rb") as key_file:
        key = key_file.read()

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted_image = decryptor.update(encrypted_image) + decryptor.finalize()

    with open("decrypted_image.jpg", "wb") as decrypted_image_file:
        decrypted_image_file.write(decrypted_image)

encrypt_image("original_image.jpg", "image_key.bin")
decrypt_image("encrypted_image.jpg", "image_key.bin")