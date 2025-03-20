Here’s a well-structured **README.md** file for your project:

---

# **Cryptographic Security Implementation (IT363)**

### **Terminal Assessment 1 – Cryptographic Security Implementation**

**Author:** Bedia, Leidy Alecxia C.  
**Student ID:** TUPM-19-5100  
**Course:** IT363 – Information Assurance and Security 2  
**Instructor:** Sir Darwin Vargas  
**Submission Date:** 03/20/2025

---

## 📌 **Project Overview**

This project is part of **IT363 – Information Assurance and Security 2** and demonstrates **cryptographic security techniques** through hands-on implementation of:

- **AES (Advanced Encryption Standard)** – Symmetric encryption for securing messages.
- **RSA (Rivest-Shamir-Adleman)** – Asymmetric encryption for key exchange.
- **Digital Signatures** – Signing and verifying messages using RSA.

---

## 📁 **Project Structure**

```
IT363_TerminalAssessment1_Bedia_LeidyAlecxia/
│── Report.pdf                   # Final report (case study + implementation)
│── Screenshots/                  # Screenshots of execution results
│   ├── aes_encryption.png        # AES encryption screenshot
│   ├── rsa_encryption.png        # RSA encryption screenshot
│   ├── digital_signature.png     # Digital signature screenshot
│── Code/                         # Python source code
│   ├── aes_implementation.py     # AES encryption script
│   ├── rsa_implementation.py     # RSA encryption script
│   ├── digital_signature.py      # Digital signature script
│── README.md                     # Project documentation
```

---

## 🚀 **Setup & Installation**

### **1️⃣ Prerequisites**

Ensure you have **Python 3.7+** installed. You can check your Python version using:

```bash
python --version
```

### **2️⃣ Install Dependencies**

Before running the scripts, install the required Python libraries:

```bash
pip install cryptography pycryptodome rsa
```

---

## 🔐 **How to Run the Scripts**

### **1️⃣ AES Encryption & Decryption**

Run the **AES encryption script**:

```bash
python Code/aes_implementation.py
```

📌 This will:

- Encrypt a message using AES.
- Decrypt it back to plaintext.

### **2️⃣ RSA Encryption & Decryption**

Run the **RSA encryption script**:

```bash
python Code/rsa_implementation.py
```

📌 This will:

- Generate an **RSA key pair**.
- Encrypt and decrypt a message using RSA.

### **3️⃣ Digital Signatures**

Run the **digital signature script**:

```bash
python Code/digital_signature.py
```

📌 This will:

- Generate an **RSA key pair**.
- Sign a message with the **private key**.
- Verify the signature using the **public key**.

---

## 📸 **Screenshots**

Execution results are stored in the `Screenshots/` folder:

- **AES Encryption** (`aes_encryption.png`)
- **RSA Encryption** (`rsa_encryption.png`)
- **Digital Signature Verification** (`digital_signature.png`)

---

## 🔎 **Security Considerations**

- **AES uses CBC mode** with padding for proper encryption.
- **RSA uses 2048-bit keys**, ensuring strong asymmetric encryption.
- **Digital signatures use SHA-256**, making verification secure.

---

## 📄 **References**

- **AES Encryption**: [NIST AES Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)
- **RSA Algorithm**: [RSA Cryptography by RSA Labs](https://www.rsa.com)
- **Digital Signatures**: [NIST Digital Signature Standard](https://csrc.nist.gov/publications/detail/fips/186/4/final)

---

## 📌 **Submission Guidelines**

🔹 **Submit the final project as a `.zip` file:**

```
IT363_TerminalAssessment1_Lastname_Firstname.zip
```

🔹 **Submit via:** [MS Teams or University Portal]  
🔹 **Deadline:** [Specify Due Date]

🚀 **Thank you! Let me know if you need any modifications.** 😊
