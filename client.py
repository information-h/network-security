import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# AES key (same as server)
key = b'ThisIsASecretKey'
# IV (same as server)
iv = b'ThisIsAnIV123456'

def encrypt_message(message):
    # Pad the message
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    # Initialize AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def main():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("[+] Connected to server")

    message = input("Enter message to encrypt and send: ")
    ciphertext = encrypt_message(message)
    print(f"[+] Encrypted message: {ciphertext}")

    client_socket.sendall(ciphertext)
    client_socket.close()

if __name__ == "__main__":
    main()
