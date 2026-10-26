"""
Sistem Reservasi - Tahap 1
Fitur: F4 Update Status Reservasi
"""

PILIHAN_STATUS = {
    "1": "Aktif",
    "2": "Selesai",
    "3": "Dibatalkan",
}


def update_status_reservasi(daftar_reservasi: list) -> None:
    """Fitur F4: Mengubah status reservasi berdasarkan kode reservasi."""
    print("\n" + "=" * 50)
    print("          UPDATE STATUS RESERVASI")
    print("=" * 50)

    # Mengecek apakah data reservasi kosong
    if not daftar_reservasi:
        print("Belum ada data reservasi yang tersimpan di sistem.")
        print("=" * 50)
        return

    # Ringkasan singkat agar pengguna mudah memilih kode
    print("Daftar reservasi saat ini:")
    for r in daftar_reservasi:
        print(
            f"  {r.get('kode_reservasi', '-')} | "
            f"{r.get('nama_pemesan', '-')} | "
            f"{r.get('status', 'Aktif')}"
        )
    print("-" * 50)

    kode_cari = input("Masukkan Kode Reservasi yang akan diubah: ").strip()
    if not kode_cari:
        print("Error: Kode reservasi tidak boleh kosong.")
        return

    # Pencarian exact match (tidak membedakan huruf besar/kecil)
    reservasi = None
    for r in daftar_reservasi:
        if r.get("kode_reservasi", "").lower() == kode_cari.lower():
            reservasi = r
            break

    if reservasi is None:
        print(f"Reservasi dengan kode '{kode_cari}' tidak ditemukan.")
        return

    status_lama = reservasi.get("status", "Aktif")

    print(f"\nKode Reservasi : {reservasi.get('kode_reservasi', '-')}")
    print(f"Nama Pemesan   : {reservasi.get('nama_pemesan', '-')}")
    print(f"Jenis Meja     : {reservasi.get('jenis', '-')}")
    print(f"Detail Meja    : {reservasi.get('detail', '-')}")
    print(f"Tanggal        : {reservasi.get('tanggal', '-')}")
    print(f"Status Saat Ini: {status_lama}")
    print("-" * 50)

    print("Pilih status baru:")
    for nomor, status in PILIHAN_STATUS.items():
        print(f"{nomor}. {status}")
    print("0. Batal")
    print("-" * 50)

    pilihan = input("Masukkan pilihan: ").strip()

    if pilihan == "0":
        print("Update status dibatalkan.")
        return

    if pilihan not in PILIHAN_STATUS:
        print("Pilihan status tidak valid. Status tidak diubah.")
        return

    status_baru = PILIHAN_STATUS[pilihan]

    if status_baru == status_lama:
        print(f"Status reservasi sudah '{status_lama}'. Tidak ada perubahan.")
        return

    konfirmasi = input(
        f"Ubah status dari '{status_lama}' menjadi '{status_baru}'? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":
        reservasi["status"] = status_baru
        print(
            f"Status reservasi {reservasi.get('kode_reservasi', '-')} "
            f"berhasil diubah menjadi '{status_baru}'."
        )
    else:
        print("Update status dibatalkan.")