# --- F2: MENAMPILKAN SEMUA RESERVASI ---
def tampilkan_semua_reservasi(daftar_reservasi: list) -> None:
    """Menampilkan semua data reservasi restoran."""

    print("\n" + "=" * 50)
    print("       DAFTAR SEMUA RESERVASI")
    print("          RESTORAN PAWON DIENG")
    print("=" * 50)

    # Mengecek apakah ada data reservasi
    if not daftar_reservasi:
        print("Belum ada data reservasi.")
        print("=" * 50)
        return

    # Menampilkan jumlah reservasi
    print(f"Jumlah Reservasi: {len(daftar_reservasi)}")
    print("-" * 50)

    # Menampilkan setiap data reservasi
    for nomor, reservasi in enumerate(daftar_reservasi, start=1):
        print(f"\nReservasi ke-{nomor}")
        print(f"Kode Reservasi : {reservasi['kode_reservasi']}")
        print(f"Nama Pemesan   : {reservasi['nama_pemesan']}")
        print(f"Jenis Meja     : {reservasi['jenis']}")
        print(f"Detail Meja    : {reservasi['detail']}")
        print(f"Tanggal        : {reservasi['tanggal']}")
        print(f"Status         : {reservasi['status']}")
        print("-" * 50)

    print("Semua data reservasi berhasil ditampilkan.")
    print("=" * 50)
