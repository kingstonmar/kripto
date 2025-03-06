# kripto
Tugas Kriptografi Kingston &amp; Marthin


# 🔒 Crypto Tool

Crypto Tool adalah aplikasi web berbasis Flask yang memungkinkan pengguna untuk melakukan enkripsi dan dekripsi teks atau file menggunakan berbagai algoritma kriptografi. Aplikasi ini dilengkapi dengan antarmuka pengguna yang ramah menggunakan Bootstrap.



# 🌟 Fitur Utama

  Enkripsi & Dekripsi Teks:

Masukkan teks dan kunci untuk melakukan enkripsi atau dekripsi.



  Enkripsi & Dekripsi File:

Unggah file untuk dienkripsi atau didekripsi.


  Algoritma Kriptografi yang Didukung:

-🧩 XOR: Cipher sederhana berbasis operasi XOR.

-🔄 RC4: Algoritma stream cipher yang cepat dan efisien.

-🔐 DES: Algoritma block cipher dengan kunci 56-bit.

-🛡️ AES: Algoritma block cipher dengan kunci 128-bit (standar enkripsi modern).

  Mode Operasi (untuk DES dan AES):

-ECB (Electronic Codebook)

-CBC (Cipher Block Chaining)

  Download Hasil:

Hasil enkripsi/dekripsi dapat diunduh dalam bentuk file.




# 🚀 Cara Menggunakan
  1. Clone Repository

          git clone https://github.com/username/crypto-tool.git

          cd crypto-tool


  2. Install Dependencies

    Pastikan Python dan pip sudah terinstal. Kemudian, jalankan:

    pip install -r requirements.txt


  3. Jalankan Aplikasi

    python app.py

  4. Gunakan Aplikasi

  -Masukkan Teks atau Unggah File.

  -Masukkan Kunci enkripsi/dekripsi.

  -Pilih Algoritma dan Mode Operasi (jika berlaku).

  -Pilih Aksi (Enkripsi atau Dekripsi).

  -Klik tombol 🔄 Proses untuk melihat hasil.

  -Jika Anda mengunggah file, hasilnya dapat diunduh dengan tombol ⬇ Download File.




# 📂 Struktur Proyek

    crypto-tool/
    ├── app.py                  # File utama aplikasi Flask
    ├── crypto_utils.py         # Fungsi kriptografi (XOR, RC4, DES, AES)
    ├── requirements.txt        # Daftar dependensi
    ├── uploads/                # Direktori untuk menyimpan file yang diunggah
    ├── results/                # Direktori untuk menyimpan hasil enkripsi/dekripsi
    └── templates/
      └── index.html          # Template HTML untuk antarmuka pengguna



# 📦 Dependencies

  Proyek ini menggunakan library berikut:

  -Flask: Framework web untuk Python.

  -PyCryptodome: Library kriptografi untuk Python.


  Instal semua dependensi dengan menjalankan:

    pip install -r requirements.txt




# 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi, ikuti langkah berikut:

1.Fork repository ini.

2.Buat branch baru (git checkout -b fitur-baru).

3.Commit perubahan Anda (git commit -m 'Tambahkan fitur baru').

4.Push ke branch (git push origin fitur-baru).

5.Buat Pull Request.



