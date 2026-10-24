
def hapus_reservasi(daftar_reservasi: list) -> None:
    """Menghapus reservasi berdasarkan kode dengan konfirmasi pengguna."""

    print("\n=== HAPUS RESERVASI ===")

    # Memeriksa apakah data reservasi tersedia
    if not daftar_reservasi:
        print("Belum ada data reservasi.")
        return

    # Meminta kode reservasi
    kode = input(
        "Masukkan kode reservasi yang ingin dihapus: "
    ).strip()

    # Validasi kode tidak boleh kosong
    if not kode:
        print("Kode reservasi tidak boleh kosong.")
        return

    # Mencari reservasi berdasarkan kode
    indeks = -1

    for i, reservasi in enumerate(daftar_reservasi):
        if reservasi.get("kode_reservasi", "").lower() == kode.lower():
            indeks = i
            break

    # Jika kode reservasi tidak ditemukan
    if indeks == -1:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    # Mengambil data reservasi yang ditemukan
    reservasi = daftar_reservasi[indeks]

    # Menampilkan detail sebelum penghapusan
    print("\nData reservasi yang akan dihapus:")
    print("----------------------------------")
    print(f"Kode reservasi : {reservasi.get('kode_reservasi', '-')}")
    print(f"Nama pemesan   : {reservasi.get('nama_pemesan', '-')}")
    print(f"Jenis          : {reservasi.get('jenis', '-')}")
    print(f"Detail         : {reservasi.get('detail', '-')}")
    print(f"Tanggal        : {reservasi.get('tanggal', '-')}")
    print(f"Status         : {reservasi.get('status', '-')}")
    print("----------------------------------")

    # Meminta konfirmasi penghapusan
    konfirmasi = input(
        "Yakin ingin menghapus reservasi ini? (Y/N): "
    ).strip().upper()

    # Menghapus reservasi jika dikonfirmasi
    if konfirmasi == "Y":
        daftar_reservasi.pop(indeks)

        print(
            f"Reservasi {reservasi['kode_reservasi']} "
            f"atas nama {reservasi['nama_pemesan']} "
            "berhasil dihapus dari sistem."
        )

    # Membatalkan penghapusan
    elif konfirmasi == "N":
        print("Penghapusan dibatalkan. Data tetap tersimpan.")

    # Menolak konfirmasi selain Y atau N
    else:
        print(
            "Pilihan tidak valid. "
            "Penghapusan dibatalkan."
        )
