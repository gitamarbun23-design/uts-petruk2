"""Validasi input dan data mahasiswa."""


def validasi_teks(teks, nama_field="Field"):
    # Memastikan teks wajib diisi.
    if not isinstance(teks, str) or not teks.strip():
        raise ValueError(f"{nama_field} tidak boleh kosong.")
    return teks.strip()


def validasi_nilai(nilai):
    # Memastikan nilai berada dalam rentang 0 sampai 100.
    nilai = float(nilai)
    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada antara 0 sampai 100.")
    return nilai
