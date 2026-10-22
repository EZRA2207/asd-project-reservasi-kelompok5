
def tampilkan_semua_reservasi(daftar_reservasi: list) -> None:
    """Fitur F2: menampilkan semua data reservasi."""

    print("\n" + "=" * 70)
    print("                 DAFTAR SEMUA RESERVASI")
    print("=" * 70)

    # Memeriksa apakah ada data reservasi
    if not daftar_reservasi:
        print("Belum ada data reservasi yang tersimpan.")
        print("=" * 70)
        return

    # Menampilkan judul kolom
    print(
        f"{'No':<4}"
        f"{'Kode Reservasi':<18}"
        f"{'Nama Pemesan':<22}"
        f"{'Jenis':<12}"
        f"{'Status':<12}"
    )
    print("-" * 70)

    # Menampilkan setiap reservasi
    for nomor, reservasi in enumerate(daftar_reservasi, start=1):
        print(
            f"{nomor:<4}"
            f"{reservasi['kode_reservasi']:<18}"
            f"{reservasi['nama_pemesan']:<22}"
            f"{reservasi['jenis']:<12}"
            f"{reservasi['status']:<12}"
        )

        print(f"     Detail  : {reservasi['detail']}")
        print(f"     Tanggal : {reservasi['tanggal']}")
        print("-" * 70)

    # Menampilkan jumlah seluruh reservasi
    print(f"Total reservasi: {len(daftar_reservasi)}")
    print("=" * 70)
