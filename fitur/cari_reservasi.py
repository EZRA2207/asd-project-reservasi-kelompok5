"""
Sistem Reservasi - Tahap 1
Fitur: F3 Cari Reservasi (Berdasarkan Kode atau Nama Pemesan)
"""

def cari_reservasi(daftar_reservasi: list) -> None:
    """Fitur F3: Mencari reservasi berdasarkan kode atau nama pemesan."""
    print("\n" + "=" * 50)
    print("          CARI DATA RESERVASI")
    print("=" * 50)

    # Mengecek apakah data reservasi kosong
    if not daftar_reservasi:
        print("Belum ada data reservasi yang tersimpan di sistem.")
        print("=" * 50)
        return

    print("Pilih metode pencarian:")
    print("1. Cari berdasarkan Kode Reservasi (Exact Match)")
    print("2. Cari berdasarkan Nama Pemesan (Partial Match)")
    print("-" * 50)

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "1":
        kode_cari = input("Masukkan Kode Reservasi yang dicari: ").strip()
        if not kode_cari:
            print("Error: Kode reservasi tidak boleh kosong.")
            return

        # Pencarian berdasarkan kode (harus persis sama / exact match)[cite: 3]
        hasil = [r for r in daftar_reservasi if r.get("kode_reservasi", "").lower() == kode_cari.lower()]

        if hasil:
            print(f"\nReservasi dengan kode '{kode_cari}' ditemukan:")
            print("-" * 50)
            for r in hasil:
                print(f"Kode Reservasi : {r.get('kode_reservasi', '-')}")
                print(f"Nama Pemesan   : {r.get('nama_pemesan', '-')}")
                print(f"Jenis Meja     : {r.get('jenis', '-')}")
                print(f"Detail Meja    : {r.get('detail', '-')}")
                print(f"Tanggal        : {r.get('tanggal', '-')}")
                print(f"Status         : {r.get('status', 'Aktif')}")
                print("-" * 50)
        else:
            print(f"Reservasi dengan kode '{kode_cari}' tidak ditemukan.")

    elif pilihan == "2":
        nama_cari = input("Masukkan Nama Pemesan yang dicari: ").strip()
        if not nama_cari:
            print("Error: Nama pemesan tidak boleh kosong.")
            return

        # Pencarian berdasarkan nama (mengandung kata kunci / partial match)[cite: 3]
        hasil = [r for r in daftar_reservasi if nama_cari.lower() in r.get("nama_pemesan", "").lower()]

        if hasil:
            print(f"\nDitemukan {len(hasil)} reservasi dengan kata kunci nama '{nama_cari}':")
            print("-" * 50)
            for nomor, reservasi in enumerate(hasil, start=1):
                print(f"Hasil ke-{nomor}")
                print(f"Kode Reservasi : {reservasi.get('kode_reservasi', '-')}")
                print(f"Nama Pemesan   : {reservasi.get('nama_pemesan', '-')}")
                print(f"Jenis Meja     : {reservasi.get('jenis', '-')}")
                print(f"Detail Meja    : {reservasi.get('detail', '-')}")
                print(f"Tanggal        : {reservasi.get('tanggal', '-')}")
                print(f"Status         : {reservasi.get('status', 'Aktif')}")
                print("-" * 50)
        else:
            print(f"Reservasi dengan nama pemesan '{nama_cari}' tidak ditemukan.")
    else:
        print("Pilihan menu pencarian tidak valid.")