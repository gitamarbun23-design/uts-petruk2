"""Program utama Sistem Manajemen Nilai Mahasiswa."""
from sistem_nilai.fileio import buat_file_awal, baca_data, tambah_baris, tulis_laporan
from sistem_nilai.processing import PengelolaNilai
from sistem_nilai.validasi import validasi_teks, validasi_nilai


def tampilkan_menu():
    # Menampilkan pilihan fitur kepada pengguna.
    print("\n=== SISTEM MANAJEMEN NILAI MAHASISWA ===")
    print("1. Tampilkan data")
    print("2. Tambah mahasiswa")
    print("3. Tampilkan analisis dan simpan laporan")
    print("4. Keluar")


def jalankan():
    print(buat_file_awal())
    pengelola = PengelolaNilai(baca_data())

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        try:
            if pilihan == "1":
                if not pengelola.mahasiswa:
                    print("Belum ada data mahasiswa.")
                for mhs in pengelola.mahasiswa:
                    print(f"{mhs.npm} | {mhs.nama} | {mhs.nilai:g} | {mhs.status_kelulusan()}")
            elif pilihan == "2":
                npm = validasi_teks(input("NPM: "), "NPM")
                nama = validasi_teks(input("Nama: "), "Nama")
                nilai = validasi_nilai(input("Nilai 0-100: "))
                mhs = pengelola.tambah(npm, nama, nilai)
                tambah_baris(mhs)
                print("Data berhasil ditambahkan.")
            elif pilihan == "3":
                ringkasan = pengelola.ringkasan()
                urutan = pengelola.urutkan_nilai(menurun=True)
                isi = [
                    "LAPORAN NILAI MAHASISWA",
                    f"Jumlah mahasiswa: {ringkasan['jumlah']}",
                    f"Rata-rata kelas: {ringkasan['rata_rata']:.2f}",
                    f"Jumlah lulus: {ringkasan['lulus']}",
                    "", "Peringkat nilai:"
                ]
                isi.extend(
                    f"{i}. {mhs.nama} - {mhs.nilai:g} ({mhs.status_kelulusan()})"
                    for i, mhs in enumerate(urutan, 1)
                )
                teks_laporan = "\n".join(isi) + "\n"
                tulis_laporan(teks_laporan)
                print(teks_laporan)
                print("Laporan disimpan ke laporan.txt")
            elif pilihan == "4":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak tersedia.")
        except (ValueError, OSError) as error:
            print(f"Terjadi kesalahan: {error}")


if __name__ == "__main__":
    jalankan()
