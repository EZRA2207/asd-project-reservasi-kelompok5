def hapus_reservasi(daftar_reservasi: list) -> None:
    """Menghapus reservasi berdasarkan kode dengan konfirmasi pengguna."""

    print("\n=== HAPUS RESERVASI ===")

    if not daftar_reservasi:
        print("Belum ada data reservasi.")
        return

    kode = input("Masukkan kode reservasi yang ingin dihapus: ").strip()

    if not kode:
        print("Kode reservasi tidak boleh kosong.")
        return

    # Cari reservasi berdasarkan kode, tanpa membedakan huruf besar/kecil.
    reservasi_ditemukan = None

    for reservasi in daftar_reservasi:
        if reservasi["kode_reservasi"].lower() == kode.lower():
            reservasi_ditemukan = reservasi
            break

    if reservasi_ditemukan is None:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    # Tampilkan detail reservasi sebelum meminta konfirmasi.
    print("\nData reservasi yang akan dihapus:")
    print("----------------------------------")
    print(f"Kode reservasi : {reservasi_ditemukan['kode_reservasi']}")
    print(f"Nama pemesan   : {reservasi_ditemukan['nama_pemesan']}")
    print(f"Jenis          : {reservasi_ditemukan['jenis']}")
    print(f"Detail         : {reservasi_ditemukan['detail']}")
    print(f"Tanggal        : {reservasi_ditemukan['tanggal']}")
    print(f"Status         : {reservasi_ditemukan['status']}")
    print("----------------------------------")

    konfirmasi = input("Yakin ingin menghapus reservasi ini? (Y/N): ").strip().upper()

    if konfirmasi == "Y":
        daftar_reservasi.remove(reservasi_ditemukan)
        print(
            f"Reservasi {reservasi_ditemukan['kode_reservasi']} "
            f"atas nama {reservasi_ditemukan['nama_pemesan']} "
            "berhasil dihapus dari sistem."
        )
    else:
        print("Penghapusan dibatalkan.")