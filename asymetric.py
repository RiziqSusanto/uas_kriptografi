from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def generate_rsa_keys():
  # Membangkitkan pasangan kunci RSA
  private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
  )
  public_key = private_key.public_key()
  return private_key, public_key

def encrypt_message(message, public_key):
  # Menenkripsi pesan menggunakan kunci publik RSA
  encrypted_message = public_key.encrypt(
    message.encode(),
    padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )
  )
  return encrypted_message

def decrypt_message(encrypted_message, private_key):
  # Mendekripsi pesan menggunakan kunci privat RSA
  decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )
  )
  return decrypted_message.decode()

# Membangkitkan pasangan kunci RSA
private_key, public_key = generate_rsa_keys()

# Pesan yang akan dienkripsi
message = "Ini adalah pesan rahasia."

# Menenkripsi pesan
encrypted_message = encrypt_message(message, public_key)
encrypted_message_base64 = base64.b64encode(encrypted_message)
print(f"Pesan terenkripsi (base64): {encrypted_message_base64.decode()}")

# Mendekripsi pesan
decrypted_message = decrypt_message(encrypted_message, private_key)
print(f"Pesan terdekripsi: {decrypted_message}")