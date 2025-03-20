import rsa
import base64
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

# Generate RSA Keys
public_key, private_key = rsa.newkeys(2048)

def sign_message(message, priv_key):
    return base64.b64encode(rsa.sign(message.encode(), priv_key, 'SHA-256')).decode()

def verify_signature(message, signature, pub_key):
    try:
        rsa.verify(message.encode(), base64.b64decode(signature), pub_key)
        return Fore.GREEN + "✅ Signature Verified"
    except rsa.VerificationError:
        return Fore.RED + "❌ Verification Failed"

# Example Usage
message = "Secure Digital Signature"

print(Fore.MAGENTA + "🖊️ Digital Signature Demonstration")
print("=" * 40)

signature = sign_message(message, private_key)
print(Fore.GREEN + "✅ Digital Signature:", Style.BRIGHT + signature)

print(Fore.YELLOW + "\n🔍 Verifying Signature...")
verification = verify_signature(message, signature, public_key)
print(verification)

print("\n" + "=" * 40)
print(Fore.MAGENTA + "🛡️ Digital Signature Process Completed!")
