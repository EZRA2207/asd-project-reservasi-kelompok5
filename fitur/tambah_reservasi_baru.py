"""
Sistem Reservasi - Tahap 1
Fitur: F1 Tambah Reservasi Baru
Kode reservasi di-generate otomatis oleh sistem.
"""


def generate_kode_reservasi(daftar_reservasi: list) -> str:
    """Generate kode unik otomatis: RSV001, RSV002, dst."""
    nomor = len(daftar_reservasi) + 1
    while True:
        kode = f"RSV{nomor:03d}"
        if not any(r["kode_reservasi"] == kode for r in daftar_reservasi):
            return kode
        nomor += 1


def validasi_format_tanggal(tanggal: str) -> bool:
    """Cek format YYYY-MM-DD tanpa library eksternal."""
    if not tanggal:
        return False
    if tanggal.count("-") != 2:
        return False

    bagian = tanggal.split("-")
    if len(bagian) != 3:
        return False

    tahun, bulan, hari = bagian
    if len(tahun) != 4 or len(bulan) != 2 or len(hari) != 2:
        return False
    if not (tahun.isdigit() and bulan.isdigit() and hari.isdigit()):
        return False
    return True


def normalisasi_jenis(jenis_input: str) -> str:
    """Normalisasi jenis jadi 'Ruangan'/'Tiket', atau '' jika invalid."""
    jenis_bersih = jenis_input.strip().lower()
    if jenis_bersih == "ruangan":
        return "Ruangan"
    if jenis_bersih == "tiket":
        return "Tiket"
    return ""


def tambah_reservasi(daftar_reservasi: list) -> None:
    """Fitur F1: tambah reservasi baru dengan validasi lengkap."""
    print("\n=== TAMBAH RESERVASI BARU ===")

    kode_reservasi = generate_kode_reservasi(daftar_reservasi)
    print(f"Kode Reservasi: {kode_reservasi}")

    # Validasi nama pemesan
    nama_pemesan = input("Atas Nama: ").strip()
    if not nama_pemesan:
        print("Error: Nama pemesan tidak boleh kosong.")
        return

    # Validasi jenis
    jenis_input = input("Jenis Reservasi (Ruangan/Tiket): ").strip()
    jenis = normalisasi_jenis(jenis_input)
    if not jenis:
        print("Error: Jenis hanya boleh 'Ruangan' atau 'Tiket'.")
        return

    # Validasi detail
    detail = input("Detail (nama ruangan / nama acara): ").strip()
    if not detail:
        print("Error: Detail tidak boleh kosong.")
        return

    # Validasi tanggal
    tanggal = input("Tanggal (YYYY-MM-DD, contoh: 2026-10-15): ").strip()
    if not tanggal:
        print("Error: Tanggal tidak boleh kosong.")
        return
    if not validasi_format_tanggal(tanggal):
        print("Format tanggal salah. Gunakan format YYYY-MM-DD, contoh: 2026-10-15.")
        return

    # Simpan data
    reservasi_baru = {
        "kode_reservasi": kode_reservasi,
        "nama_pemesan": nama_pemesan,
        "jenis": jenis,
        "detail": detail,
        "tanggal": tanggal,
        "status": "Aktif",
    }
    daftar_reservasi.append(reservasi_baru)

    print(f"\nReservasi {kode_reservasi} atas nama {nama_pemesan} berhasil ditambahkan.")


def main() -> None:
    """Loop menu utama."""
    daftar_reservasi = []

    while True:
        print("\n" + "=" * 40)
        print("      SISTEM RESERVASI - MENU UTAMA")
        print("=" * 40)
        print("1. Tambah Reservasi Baru")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_reservasi(daftar_reservasi)
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()