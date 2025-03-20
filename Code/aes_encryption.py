from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

def aes_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size).decode()

# Example Usage
key = b'Sixteen byte key'  # Must be 16 bytes
message = "Confidential Message"

print(Fore.CYAN + "🔐 AES Encryption Demonstration")
print("=" * 40)

encrypted_msg = aes_encrypt(message, key)
print(Fore.GREEN + "✅ Encrypted Message:", Style.BRIGHT + encrypted_msg)

print(Fore.YELLOW + "\n🔓 Decrypting Message...")
decrypted_msg = aes_decrypt(encrypted_msg, key)
print(Fore.GREEN + "✅ Decrypted Message:", Style.BRIGHT + decrypted_msg)

print("\n" + "=" * 40)
print(Fore.CYAN + "🔒 AES Encryption Process Completed!")
