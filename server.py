import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# AES key (must be 16, 24, or 32 bytes for AES)
key = b'ThisIsASecretKey'
# Initialization Vector (IV)
iv = b'ThisIsAnIV123456'

def decrypt_message(ciphertext):
    # Initialize AES Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt data
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Unpad data
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    return data.decode()

def main():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")

    ciphertext = conn.recv(1024)
    print(f"[+] Received encrypted message: {ciphertext}")

    plaintext = decrypt_message(ciphertext)
    print(f"[+] Decrypted message: {plaintext}")

    conn.close()

if __name__ == "__main__":
    main()
