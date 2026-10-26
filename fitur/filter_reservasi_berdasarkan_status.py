"""
Sistem Reservasi - Tahap 1
Fitur: F5 Filter Reservasi Berdasarkan Status (Aktif / Selesai / Dibatalkan)
"""

def filter_reservasi_berdasarkan_status(daftar_reservasi: list) -> None:
    """Fitur F5: Memfilter dan menampilkan daftar reservasi berdasarkan status tertentu."""
    print("\n" + "=" * 50)
    print("       FILTER RESERVASI BERDASARKAN STATUS")
    print("=" * 50)

    # Mengecek apakah data reservasi kosong
    if not daftar_reservasi:
        print("Belum ada data reservasi yang tersimpan di sistem.")
        print("=" * 50)
        return

    print("Pilih status yang ingin ditampilkan:")
    print("1. Aktif")
    print("2. Selesai")
    print("3. Dibatalkan")
    print("-" * 50)

    pilihan = input("Masukkan pilihan (1/2/3) atau ketik statusnya: ").strip().lower()

    # Mapping pilihan ke status yang valid (tidak case-sensitive sesuai brief)[cite: 3]
    mapping_status = {
        "1": "Aktif",
        "2": "Selesai",
        "3": "Dibatalkan",
        "aktif": "Aktif",
        "selesai": "Selesai",
        "dibatalkan": "Dibatalkan"
    }

    if pilihan not in mapping_status:
        print("Error: Pilihan status hanya boleh 'Aktif', 'Selesai', atau 'Dibatalkan'.")
        print("=" * 50)
        return

    status_filter = mapping_status[pilihan]

    # Melakukan filter data (tidak case-sensitive)[cite: 3]
    hasil_filter = [
        r for r in daftar_reservasi 
        if r.get("status", "Aktif").strip().lower() == status_filter.lower()
    ]

    print("\n" + "=" * 50)
    # Header keterangan sesuai format brief[cite: 3]
    print(f"Menampilkan reservasi dengan status: {status_filter} ({len(hasil_filter)} data)")
    print("=" * 50)

    if not hasil_filter:
        print(f"Tidak ada reservasi dengan status '{status_filter}'.")
        print("=" * 50)
        return

    # Menampilkan hasil filter secara terstruktur
    for nomor, reservasi in enumerate(hasil_filter, start=1):
        print(f"Reservasi ke-{nomor}")
        print(f"Kode Reservasi : {reservasi.get('kode_reservasi', '-')}")
        print(f"Nama Pemesan   : {reservasi.get('nama_pemesan', '-')}")
        print(f"Jenis Meja     : {reservasi.get('jenis', '-')}")
        print(f"Detail Meja    : {reservasi.get('detail', '-')}")
        print(f"Tanggal        : {reservasi.get('tanggal', '-')}")
        print(f"Status         : {reservasi.get('status', 'Aktif')}")
        print("-" * 50)

    print("Filter reservasi selesai.")
    print("=" * 50)