# kripto
Tugas Kriptografi Kingston &amp; Marthin

markdown
Copy
# Crypto Tool

Crypto Tool adalah aplikasi web sederhana yang memungkinkan pengguna untuk melakukan enkripsi dan dekripsi teks atau file menggunakan berbagai algoritma kriptografi. Aplikasi ini dibangun menggunakan Flask (Python) dan Bootstrap untuk antarmuka pengguna.

## Fitur

- **Enkripsi dan Dekripsi Teks**: Pengguna dapat memasukkan teks dan kunci untuk melakukan enkripsi atau dekripsi.
- **Enkripsi dan Dekripsi File**: Pengguna dapat mengunggah file untuk dienkripsi atau didekripsi.
- **Algoritma Kriptografi yang Didukung**:
  - XOR
  - RC4
  - DES
  - AES
- **Mode Operasi** (untuk DES dan AES):
  - ECB (Electronic Codebook)
  - CBC (Cipher Block Chaining)
- **Download Hasil**: Pengguna dapat mengunduh hasil enkripsi atau dekripsi dalam bentuk file.

## Cara Menggunakan

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/crypto-tool.git
   cd crypto-tool
Install Dependencies:
Pastikan Anda telah menginstal Python dan pip. Kemudian, jalankan perintah berikut untuk menginstal dependensi yang diperlukan:

bash
Copy
pip install -r requirements.txt
Jalankan Aplikasi:

bash
Copy
python app.py
Aplikasi akan berjalan di http://127.0.0.1:5000/. Buka browser Anda dan akses URL tersebut.

Gunakan Aplikasi:

Masukkan teks atau unggah file.

Masukkan kunci enkripsi/dekripsi.

Pilih algoritma dan mode operasi (jika berlaku).

Pilih aksi (enkripsi atau dekripsi).

Klik tombol "Proses" untuk melihat hasilnya.

Jika Anda mengunggah file, Anda akan diberikan opsi untuk mengunduh hasil enkripsi/dekripsi.

Struktur Proyek
app.py: File utama yang menjalankan aplikasi Flask.

crypto_utils.py: Berisi fungsi-fungsi kriptografi untuk XOR, RC4, DES, dan AES.

templates/index.html: Template HTML untuk antarmuka pengguna.

uploads/: Direktori untuk menyimpan file yang diunggah.

results/: Direktori untuk menyimpan hasil enkripsi/dekripsi.

Dependencies
Flask

PyCryptodome

Anda dapat menginstal semua dependensi yang diperlukan dengan menjalankan:

bash
Copy
pip install -r requirements.txt
