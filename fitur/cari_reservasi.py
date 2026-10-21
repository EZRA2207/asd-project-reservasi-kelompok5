# ==========================================
# MODUL / FITUR 3: CARI RESERVASI (PANDUAN INPUT SPESIFIK)
# ==========================================

# 2 Contoh Data Reservasi Awal (Array of Struct / List of Dict)
daftar_reservasi = [
    {
        "kode_reservasi": "RSV001",
        "nama_pemesan": "Budi Santoso",
        "jenis": "Ruangan",
        "detail": "Ruang Rapat A",
        "tanggal": "2026-10-15",
        "status": "Aktif"
    },
    {
        "kode_reservasi": "RSV002",
        "nama_pemesan": "Siti Rahma",
        "jenis": "Tiket",
        "detail": "Seminar Nasional Teknologi",
        "tanggal": "2026-10-20",
        "status": "Aktif"
    }
]

def format_status(status):
    """Fungsi helper untuk memberikan penanda visual pada status."""
    if status.lower() == "aktif":
        return "[AKTIF]"
    elif status.lower() == "selesai":
        return "[SELESAI]"
    elif status.lower() == "dibatalkan":
        return "[DIBATALKAN]"
    return f"[{status.upper()}]"

def tampilkan_detail_reservasi(r, nomor=None):
    """Fungsi helper untuk menampilkan detail reservasi dalam format baris ke bawah."""
    if nomor:
        print(f"\n--- DATA RESERVASI KE-{nomor} ---")
    else:
        print("\n--- DETAIL RESERVASI ---")
    print(f"Kode Reservasi  : {r['kode_reservasi']}")
    print(f"Nama Pemesan    : {r['nama_pemesan']}")
    print(f"Jenis           : {r['jenis']}")
    print(f"Detail          : {r['detail']}")
    print(f"Tanggal         : {r['tanggal']}")
    print(f"Status          : {format_status(r['status'])}")
    print("-" * 35)

def cari_reservasi():
    print("\n" + "="*40)
    print("       MENU: CARI RESERVASI")
    print("="*40)
    
    # Looping untuk validasi pemilihan menu (1 atau 2)
    while True:
        print("1. Cari berdasarkan Kode Reservasi (Exact Match)")
        print("2. Cari berdasarkan Nama Pemesan (Partial Match)")
        pilihan = input("Pilih metode pencarian (1/2): ").strip()
        
        if pilihan in ["1", "2"]:
            break
        else:
            print("\n[ERROR] Pilihan tidak valid! Silakan masukkan angka 1 atau 2.\n")
    
    if pilihan == "1":
        # Looping pencarian kode dengan panduan input yang spesifik untuk Kode Reservasi
        while True:
            kata_kunci = input("Masukkan Kode Reservasi (atau ketik 'keluar' untuk batal): ").strip()
            
            # Cek jika user ingin membatalkan
            if kata_kunci.lower() == 'keluar':
                print("[INFO] Pencarian dibatalkan.")
                return
            
            # Validasi input kosong
            if not kata_kunci:
                print("[ERROR] Kode Reservasi tidak boleh kosong! Silakan coba lagi.\n")
                continue
            
            # Cek apakah kode reservasi ada di dalam sistem (Exact Match)
            hasil = None
            for r in daftar_reservasi:
                if r["kode_reservasi"].lower() == kata_kunci.lower():
                    hasil = r
                    break
            
            if hasil:
                print("\n[SUKSES] Reservasi ditemukan!")
                tampilkan_detail_reservasi(hasil)
                break  # Keluar dari loop karena data sudah ketemu
            else:
                print(f"[ERROR] Reservasi dengan kode '{kata_kunci}' tidak ditemukan di sistem. Silakan coba lagi.\n")
            
    elif pilihan == "2":
        # Looping pencarian nama dengan panduan input yang spesifik untuk Nama Pemesan
        while True:
            kata_kunci = input("Masukkan Nama Pemesan (atau ketik 'keluar' untuk batal): ").strip()
            
            # Cek jika user ingin membatalkan
            if kata_kunci.lower() == 'keluar':
                print("[INFO] Pencarian dibatalkan.")
                return
            
            # Validasi input kosong
            if not kata_kunci:
                print("[ERROR] Nama Pemesan tidak boleh kosong! Silakan coba lagi.\n")
                continue
            
            # Menyaring data yang mengandung kata kunci pada nama_pemesan (Partial Match)
            hasil_pencarian = []
            for r in daftar_reservasi:
                if kata_kunci.lower() in r["nama_pemesan"].lower():
                    hasil_pencarian.append(r)
            
            if hasil_pencarian:
                jumlah = len(hasil_pencarian)
                print(f"\n[SUKSES] Ditemukan {jumlah} reservasi yang cocok dengan kata kunci '{kata_kunci}':")
                
                # Menampilkan setiap hasil pencarian menggunakan format baris ke bawah
                for idx, r in enumerate(hasil_pencarian, 1):
                    tampilkan_detail_reservasi(r, nomor=idx)
                break  # Keluar dari loop karena data ditemukan
            else:
                print(f"[ERROR] Tidak ada reservasi dengan nama pemesan yang mengandung '{kata_kunci}'. Silakan coba lagi.\n")

# --- Blok Pengujian Mandiri ---
if __name__ == "__main__":
    cari_reservasi()