"""Fungsi untuk membaca dan menulis file."""
from .processing import Mahasiswa

DATA_FILE = "nilai.txt"
REPORT_FILE = "laporan.txt"


def buat_file_awal(nama_file=DATA_FILE):
    # Mode x membuat file baru dan tidak menimpa file yang sudah ada.
    try:
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write("2035;Gita;85\n")
            file.write("2036;Rina;75\n")
            file.write("2037;Budi;60\n")
        return "File data berhasil dibuat."
    except FileExistsError:
        return "File data sudah ada, jadi tidak ditimpa."


def tambah_baris(mahasiswa, nama_file=DATA_FILE):
    # Mode a menambahkan data tanpa menghapus isi lama.
    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(f"{mahasiswa.npm};{mahasiswa.nama};{mahasiswa.nilai:g}\n")


def baca_data(nama_file=DATA_FILE):
    # Mode r membaca file baris demi baris dan melewati baris rusak.
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                try:
                    bagian = baris.strip().split(";")
                    if len(bagian) != 3:
                        raise ValueError("Format harus NPM;Nama;Nilai")
                    npm, nama, nilai = bagian
                    data.append(Mahasiswa(npm, nama, nilai))
                except (ValueError, TypeError) as error:
                    print(f"Baris {nomor} dilewati: {error}")
    except FileNotFoundError:
        print(f"File '{nama_file}' belum ditemukan. Buat file terlebih dahulu.")
    return data


def tulis_laporan(teks, nama_file=REPORT_FILE):
    # Mode w menulis ulang isi file laporan.
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(teks)
