# Daftar status yang valid
STATUS_VALID = ["Aktif", "Selesai", "Dibatalkan"]


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


def normalisasi_status(status_input: str) -> str:
    """Normalisasi status jadi 'Aktif'/'Selesai'/'Dibatalkan', atau '' jika invalid."""
    status_bersih = status_input.strip().lower()
    for status in STATUS_VALID:
        if status.lower() == status_bersih:
            return status
    return ""


def cari_reservasi(daftar_reservasi: list, kode: str):
    """Cari reservasi berdasarkan kode (tidak case-sensitive). None jika tidak ada."""
    for reservasi in daftar_reservasi:
        if reservasi["kode_reservasi"].upper() == kode.upper():
            return reservasi
    return None


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


def update_status_reservasi(daftar_reservasi: list) -> None:
    """Fitur F2: ubah status reservasi berdasarkan kode reservasi."""
    print("\n=== UPDATE STATUS RESERVASI ===")

    # Cek apakah sudah ada data
    if not daftar_reservasi:
        print("Belum ada data reservasi. Tambahkan reservasi terlebih dahulu.")
        return

    # Input kode reservasi
    kode = input("Masukkan Kode Reservasi (contoh: RSV001): ").strip()
    if not kode:
        print("Error: Kode reservasi tidak boleh kosong.")
        return

    reservasi = cari_reservasi(daftar_reservasi, kode)
    if reservasi is None:
        print(f"Error: Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    # Tampilkan data reservasi saat ini
    print("\nData Reservasi:")
    print(f"  Kode      : {reservasi['kode_reservasi']}")
    print(f"  Atas Nama : {reservasi['nama_pemesan']}")
    print(f"  Jenis     : {reservasi['jenis']}")
    print(f"  Detail    : {reservasi['detail']}")
    print(f"  Tanggal   : {reservasi['tanggal']}")
    print(f"  Status    : {reservasi['status']}")

    # Input status baru
    print(f"\nStatus yang tersedia: {', '.join(STATUS_VALID)}")
    status_input = input("Status baru: ").strip()
    if not status_input:
        print("Error: Status baru tidak boleh kosong.")
        return

    status_baru = normalisasi_status(status_input)
    if not status_baru:
        print(f"Error: Status tidak valid. Pilih salah satu: {', '.join(STATUS_VALID)}.")
        return

    # Cek apakah status sama dengan sebelumnya
    status_lama = reservasi["status"]
    if status_baru == status_lama:
        print(f"Status reservasi {reservasi['kode_reservasi']} sudah '{status_lama}'. Tidak ada perubahan.")
        return

    # Konfirmasi perubahan
    konfirmasi = input(f"Ubah status dari '{status_lama}' menjadi '{status_baru}'? (y/n): ").strip().lower()
    if konfirmasi != "y":
        print("Perubahan status dibatalkan.")
        return

    # Simpan perubahan
    reservasi["status"] = status_baru
    print(f"\nStatus reservasi {reservasi['kode_reservasi']} berhasil diubah: {status_lama} -> {status_baru}.")


def main() -> None:
    """Loop menu utama."""
    daftar_reservasi = []

    while True:
        print("\n" + "=" * 40)
        print("      SISTEM RESERVASI - MENU UTAMA")
        print("=" * 40)
        print("1. Tambah Reservasi Baru")
        print("2. Update Status Reservasi")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_reservasi(daftar_reservasi)
        elif pilihan == "2":
            update_status_reservasi(daftar_reservasi)
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()