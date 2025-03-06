from flask import Flask, request, render_template, send_file
import os
import base64
from Crypto.Cipher import DES, AES
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

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
    key = key.ljust(8, '\0')[:8].encode()
    cipher = DES.new(key, mode)
    encrypted = cipher.encrypt(data.ljust((len(data) + 7) // 8 * 8, b'\0'))
    return encrypted

def des_decrypt(data, key, mode):
    key = key.ljust(8, '\0')[:8].encode()
    cipher = DES.new(key, mode)
    return cipher.decrypt(data).rstrip(b'\0')

def aes_encrypt(data, key, mode):
    key = key.ljust(16, '\0')[:16].encode()
    cipher = AES.new(key, mode)
    encrypted = cipher.encrypt(data.ljust((len(data) + 15) // 16 * 16, b'\0'))
    return encrypted

def aes_decrypt(data, key, mode):
    key = key.ljust(16, '\0')[:16].encode()
    cipher = AES.new(key, mode)
    return cipher.decrypt(data).rstrip(b'\0')

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    download_file = None

    if request.method == "POST":
        text = request.form.get("text", "")
        key = request.form.get("key", "")
        algorithm = request.form.get("algorithm", "")
        mode = request.form.get("mode", "ECB")
        action = request.form.get("action", "Encrypt")

        if algorithm in ["DES", "AES"]:
            mode = DES.MODE_CBC if mode == "CBC" else DES.MODE_ECB
        else:
            mode = None

        # Handle text encryption/decryption
        if text:
            data = text.encode()
            if action == "Encrypt":
                if algorithm == "XOR":
                    result = base64.b64encode(xor_cipher(data, key)).decode()
                elif algorithm == "RC4":
                    result = base64.b64encode(rc4_cipher(data, key)).decode()
                elif algorithm == "DES":
                    result = base64.b64encode(des_encrypt(data, key, mode)).decode()
                elif algorithm == "AES":
                    result = base64.b64encode(aes_encrypt(data, key, mode)).decode()
            elif action == "Decrypt":
                data = base64.b64decode(text)
                if algorithm == "XOR":
                    result = xor_cipher(data, key).decode()
                elif algorithm == "RC4":
                    result = rc4_cipher(data, key).decode()
                elif algorithm == "DES":
                    result = des_decrypt(data, key, mode).decode()
                elif algorithm == "AES":
                    result = aes_decrypt(data, key, mode).decode()

        # Handle file encryption/decryption
        file = request.files.get("file")
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            with open(filepath, "rb") as f:
                file_data = f.read()

            if action == "Encrypt":
                if algorithm == "XOR":
                    encrypted_data = xor_cipher(file_data, key)
                elif algorithm == "RC4":
                    encrypted_data = rc4_cipher(file_data, key)
                elif algorithm == "DES":
                    encrypted_data = des_encrypt(file_data, key, mode)
                elif algorithm == "AES":
                    encrypted_data = aes_encrypt(file_data, key, mode)

                encrypted_filename = f"encrypted_{filename}"
            elif action == "Decrypt":
                if algorithm == "XOR":
                    encrypted_data = xor_cipher(file_data, key)
                elif algorithm == "RC4":
                    encrypted_data = rc4_cipher(file_data, key)
                elif algorithm == "DES":
                    encrypted_data = des_decrypt(file_data, key, mode)
                elif algorithm == "AES":
                    encrypted_data = aes_decrypt(file_data, key, mode)

                encrypted_filename = f"decrypted_{filename}"

            result_filepath = os.path.join(RESULT_FOLDER, encrypted_filename)
            with open(result_filepath, "wb") as f:
                f.write(encrypted_data)

            download_file = encrypted_filename

    return render_template("index.html", result=result, download_file=download_file)

@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join(RESULT_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
