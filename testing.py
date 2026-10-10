"""Pengujian otomatis menggunakan unittest."""
import unittest
from .processing import Mahasiswa, PengelolaNilai
from .validasi import validasi_nilai, validasi_teks


class TestSistemNilai(unittest.TestCase):
    def setUp(self):
        self.pengelola = PengelolaNilai()
        self.pengelola.tambah("1001", "Andi", 80)
        self.pengelola.tambah("1002", "Sari", 60)

    def test_validasi_nilai_benar(self):
        self.assertEqual(validasi_nilai(80), 80)

    def test_nilai_di_luar_batas_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_nilai(120)

    def test_nama_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_teks("  ", "Nama")

    def test_status_lulus(self):
        self.assertEqual(Mahasiswa("1", "Dina", 75).status_kelulusan(), "Lulus")

    def test_status_tidak_lulus(self):
        self.assertEqual(Mahasiswa("2", "Doni", 50).status_kelulusan(), "Tidak Lulus")

    def test_rata_rata(self):
        self.assertEqual(self.pengelola.rata_rata(80, 60), 70)

    def test_pencarian_npm(self):
        self.assertEqual(self.pengelola.cari_npm("1001").nama, "Andi")

    def test_urutkan_menurun(self):
        hasil = self.pengelola.urutkan_nilai()
        self.assertEqual([mhs.nilai for mhs in hasil], [80, 60])


if __name__ == "__main__":
    unittest.main()
