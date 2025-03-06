import base64
import os
from Crypto.Cipher import DES, AES

def xor_cipher(data, key):
    key = key.encode()
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def rc4_cipher(data, key):
    key = key.encode()
    S = list(range(256))
    j = 0
    out = bytearray()

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])

    return bytes(out)

def des_encrypt(data, key, mode):
    key = key.ljust(8, '\0')[:8].encode()  # Pastikan key 8 byte
    iv = os.urandom(8) if mode == DES.MODE_CBC else None
    cipher = DES.new(key, mode, iv) if iv else DES.new(key, mode)
    encrypted = cipher.encrypt(data)  # Data harus kelipatan 8 byte
    return (iv or b'') + encrypted

def des_decrypt(data, key, mode):
    key = key.ljust(8, '\0')[:8].encode()
    iv, data = (data[:8], data[8:]) if mode == DES.MODE_CBC else (None, data)
    cipher = DES.new(key, mode, iv) if iv else DES.new(key, mode)
    return cipher.decrypt(data)

def aes_encrypt(data, key, mode):
    key = key.ljust(16, '\0')[:16].encode()  # Pastikan key 16 byte
    iv = os.urandom(16) if mode == AES.MODE_CBC else None
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    encrypted = cipher.encrypt(data)  # Data harus kelipatan 16 byte
    return (iv or b'') + encrypted

def aes_decrypt(data, key, mode):
    key = key.ljust(16, '\0')[:16].encode()
    iv, data = (data[:16], data[16:]) if mode == AES.MODE_CBC else (None, data)
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    return cipher.decrypt(data)

# Contoh Penggunaan
if __name__ == "__main__":
    text = b"12345678ABCDEFGH"  # Ukuran harus kelipatan 8 (DES) atau 16 (AES)
    key = "mysecret"

    print("DES Encryption & Decryption")
    encrypted_des = des_encrypt(text, key, DES.MODE_ECB)
    decrypted_des = des_decrypt(encrypted_des, key, DES.MODE_ECB)
    print("Encrypted:", encrypted_des)
    print("Decrypted:", decrypted_des)

    print("\nAES Encryption & Decryption")
    encrypted_aes = aes_encrypt(text, key, AES.MODE_ECB)
    decrypted_aes = aes_decrypt(encrypted_aes, key, AES.MODE_ECB)
    print("Encrypted:", encrypted_aes)
    print("Decrypted:", decrypted_aes)
