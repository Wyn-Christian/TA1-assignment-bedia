import rsa
import base64
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

# Generate RSA Keys
public_key, private_key = rsa.newkeys(2048)

def rsa_encrypt(plaintext, pub_key):
    return base64.b64encode(rsa.encrypt(plaintext.encode(), pub_key)).decode()

def rsa_decrypt(ciphertext, priv_key):
    return rsa.decrypt(base64.b64decode(ciphertext), priv_key).decode()

# Example Usage
message = "Sensitive RSA Data"

print(Fore.BLUE + "🔑 RSA Encryption Demonstration")
print("=" * 40)

encrypted_msg = rsa_encrypt(message, public_key)
print(Fore.GREEN + "✅ Encrypted Message:", Style.BRIGHT + encrypted_msg)

print(Fore.YELLOW + "\n🔓 Decrypting Message...")
decrypted_msg = rsa_decrypt(encrypted_msg, private_key)
print(Fore.GREEN + "✅ Decrypted Message:", Style.BRIGHT + decrypted_msg)

print("\n" + "=" * 40)
print(Fore.BLUE + "🔐 RSA Encryption Process Completed!")
