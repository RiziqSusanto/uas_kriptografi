from cryptography.fernet import Fernet

def generate_key():
  # Membangkitkan kunci enkripsi simetris
  key = Fernet.generate_key()
  return key

def encrypt_message(message, key):
  # Menenkripsi pesan menggunakan kunci simetris
  f = Fernet(key)
  encrypted_message = f.encrypt(message.encode())
  return encrypted_message

def decrypt_message(encrypted_message, key):
  # Mendekripsi pesan menggunakan kunci simetris
  f = Fernet(key)
  decrypted_message = f.decrypt(encrypted_message).decode()
  return decrypted_message

# Membangkitkan kunci enkripsi
key = generate_key()

# Pesan yang akan dienkripsi
message = "Ini adalah pesan rahasia."

# Menenkripsi pesan
encrypted_message = encrypt_message(message, key)
print(f"Pesan terenkripsi: {encrypted_message.decode()}")

# Mendekripsi pesan
decrypted_message = decrypt_message(encrypted_message, key)
print(f"Pesan terdekripsi: {decrypted_message}")