"""Class dan fungsi untuk pengolahan nilai mahasiswa."""
from dataclasses import dataclass
from .validasi import validasi_teks, validasi_nilai


@dataclass
class Mahasiswa:
    npm: str
    nama: str
    nilai: float

    def __post_init__(self):
        # Validasi otomatis saat objek mahasiswa dibuat.
        self.npm = validasi_teks(self.npm, "NPM")
        self.nama = validasi_teks(self.nama, "Nama")
        self.nilai = validasi_nilai(self.nilai)

    def status_kelulusan(self, batas=70):
        # Mengembalikan status berdasarkan nilai batas.
        return "Lulus" if self.nilai >= batas else "Tidak Lulus"

    def sebagai_record(self, **kwargs):
        # kwargs menerima atribut tambahan secara fleksibel.
        record = {"npm": self.npm, "nama": self.nama, "nilai": self.nilai}
        record.update(kwargs)
        return record


class PengelolaNilai:
    def __init__(self, mahasiswa=None):
        self.mahasiswa = mahasiswa or []

    def tambah(self, npm, nama, nilai):
        # Membuat mahasiswa baru dan menyimpannya ke daftar.
        data = Mahasiswa(npm, nama, nilai)
        self.mahasiswa.append(data)
        return data

    def rata_rata(self, *nilai):
        # *args menerima banyak nilai dalam satu pemanggilan.
        if not nilai:
            return 0.0
        angka = [validasi_nilai(n) for n in nilai]
        return sum(angka) / len(angka)

    def urutkan_nilai(self, menurun=True):
        # Lambda menentukan nilai sebagai kunci pengurutan.
        return sorted(self.mahasiswa, key=lambda mhs: mhs.nilai, reverse=menurun)

    def cari_npm(self, npm):
        # Mencari mahasiswa berdasarkan NPM.
        for mhs in self.mahasiswa:
            if mhs.npm == str(npm):
                return mhs
        return None

    def ringkasan(self):
        # Menghitung jumlah mahasiswa, rata-rata, dan jumlah lulus.
        assert all(0 <= mhs.nilai <= 100 for mhs in self.mahasiswa), "Ada nilai di luar rentang."
        if not self.mahasiswa:
            return {"jumlah": 0, "rata_rata": 0.0, "lulus": 0}
        return {
            "jumlah": len(self.mahasiswa),
            "rata_rata": self.rata_rata(*(mhs.nilai for mhs in self.mahasiswa)),
            "lulus": sum(mhs.nilai >= 70 for mhs in self.mahasiswa),
        }
