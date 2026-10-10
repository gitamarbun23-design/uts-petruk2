# Sistem Manajemen Nilai Mahasiswa

Program Python sederhana untuk menyimpan, memvalidasi, menganalisis, dan melaporkan nilai mahasiswa.

## Cara menjalankan
1. Pastikan Python 3 sudah terpasang.
2. Buka terminal pada folder yang berisi `main.py`.
3. Jalankan `python main.py` (Windows dapat memakai `py main.py`).
4. Untuk pengujian: `python -m unittest sistem_nilai.testing -v`.

## Struktur program
- `main.py`: menu dan alur utama.
- `sistem_nilai/validasi.py`: validasi input.
- `sistem_nilai/processing.py`: class dan analisis nilai.
- `sistem_nilai/fileio.py`: operasi file.
- `sistem_nilai/testing.py`: pengujian otomatis.

## Contoh tabel refactoring
| Sebelum | Sesudah | Teknik | Alasan |
|---|---|---|---|
| Validasi nilai ditulis di beberapa tempat | Fungsi `validasi_nilai()` | Extract function | Validasi lebih konsisten |
| Nama variabel terlalu umum | Nama seperti `mahasiswa` dan `pengelola` | Rename variable | Lebih mudah dibaca |
| Baca file dan validasi tercampur | Fungsi baca file dan validasi dipisah ke modul | Extract function / modularisasi | Lebih mudah diuji dan diperbaiki |

## Mode file
- `x`: membuat file awal tanpa menimpa file yang sudah ada.
- `a`: menambahkan data mahasiswa di akhir file.
- `r`: membaca data baris demi baris.
- `w`: menulis ulang laporan.

Data menggunakan format `NPM;Nama;Nilai`. Baris yang format atau nilainya tidak valid dilewati dengan pesan.
