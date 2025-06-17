# 🔐 Network Security System using AES Encryption

A Python-based **Network Security System** that demonstrates secure communication between a **client and server** using **AES (Advanced Encryption Standard)** for encryption and decryption of data transmitted over a socket-based network.

---

## 🌐 Project Overview

This project simulates a secure network communication channel between a client and a server. All messages sent over the network are **encrypted using AES-CBC mode** to ensure confidentiality and prevent unauthorized access.

---

## 🔧 Technologies Used

* Python 3
* `socket` for network communication
* `cryptography` library for AES encryption
* AES (CBC Mode) with PKCS7 Padding

---

## 📂 Project Structure

```
network_security_system/
│
├── client.py          # Encrypts and sends a secure message to the server
├── server.py          # Decrypts and reads the received message
└── README.md          # Project documentation
```

---

## 🔐 Encryption Details

* **Algorithm**: AES (Advanced Encryption Standard)
* **Mode**: CBC (Cipher Block Chaining)
* **Key size**: 128-bit (16 bytes)
* **IV**: 16 bytes (static or randomly generated)

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies:

```bash
pip install cryptography
```

### 2️⃣ Start the server:

```bash
python server.py
```

### 3️⃣ In a new terminal, run the client:

```bash
python client.py
```

### 4️⃣ Enter a message when prompted and see it securely sent, encrypted, and decrypted.

---

## 🧪 Example Output

### On the client side:

```
[+] Connected to server
Enter message to encrypt and send: Hello, this is a secret!
[+] Encrypted message: b'\x93\xab...'
```

### On the server side:

```
[*] Listening on 127.0.0.1:5000...
[+] Connection from ('127.0.0.1', 59732)
[+] Received encrypted message: b'\x93\xab...'
[+] Decrypted message: Hello, this is a secret!
```

---

## ✅ Features

* Secure AES-based encryption and decryption
* Real-time encrypted communication
* Basic socket programming with security integration
* Lightweight and easy to run

---

## 🔐 Future Enhancements

* Add random IV per message and transmit it securely
* Use RSA for key exchange (hybrid cryptosystem)
* Add message authentication (HMAC)
* Multi-client support
* GUI with PyQt or Flask frontend

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and demonstrates basic encryption over a local network. For real-world applications, additional layers like authentication, integrity, and certificate-based security are essential.

---

Let me know if you want:

* a version in **Hindi**
* a **LinkedIn description**
* or help packaging it into a full project zip!
