import socket
import os
from cryptography.hazmat.primitives.ciphers import cipher , alogrithms, modes
from cryptography.hazmat.primitives.ciphers import padding
from cryptography.hazmat.primitives.ciphers import default_backend

key = b '8051AUsa'

iv = so b 'thisisan11223344'

def decrpt_message(ciphertext):
    cipher = cipher(alogrithms.AES(key), modes.CBC(iv), backend = cipher.decryptor())
    decryptor = cipher.decryptor()

padding_data = decryptor.update(ciphertext) + decrpt.finalize()

