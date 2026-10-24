"""
Fitur: F1 Tambah Reservasi Baru (Konsep Restoran)
"""

import sys

def generate_kode_reservasi(daftar_reservasi: list) -> str:
    nomor = len(daftar_reservasi) + 1
    while True:
        kode = f"RSV{nomor:03d}"
        if not any(r["kode_reservasi"] == kode for r in daftar_reservasi):
            return kode
        nomor += 1

def validasi_format_tanggal(tanggal: str) -> bool:
    if not tanggal or tanggal.count("-") != 2:
        return False
    bagian = tanggal.split("-")
    if len(bagian) != 3:
        return False
    tahun, bulan, hari = bagian
    if len(tahun) != 4 or len(bulan) != 2 or len(hari) != 2:
        return False
    if not (tahun.isdigit() and bulan.isdigit() and hari.isdigit()):
        return False
    
    angka_bulan = int(bulan)
    angka_hari = int(hari)
    
    if angka_bulan < 1 or angka_bulan > 12:
        return False
    if angka_hari < 1 or angka_hari > 31:
        return False
    return True

def normalisasi_jenis(jenis_input: str) -> str:
    jenis_bersih = jenis_input.strip().lower()
    if jenis_bersih == "reguler": return "Reguler"
    if jenis_bersih == "vip": return "VIP"
    return ""

def cek_detail_meja(detail_input: str, jenis: str) -> bool:
    """Fungsi khusus untuk memvalidasi inputan detail meja"""
    detail_lower = detail_input.lower()
    
    if jenis == "VIP":
        if "vip" not in detail_lower:
            print(f"Error: Input '{detail_input}' tidak valid. Karena Anda memilih VIP, detail harus mengandung kata 'VIP' (contoh: VIP-01).")
            return False
        if "reg" in detail_lower or "reguler" in detail_lower:
            print("Error: Anda memilih VIP, detail meja tidak boleh mengandung kata 'Reguler/Reg'.")
            return False
            
    elif jenis == "Reguler":
        if "reg" not in detail_lower and "reguler" not in detail_lower:
            print(f"Error: Input '{detail_input}' tidak valid. Karena Anda memilih Reguler, detail harus mengandung kata 'Reg' atau 'Reguler' (contoh: Reg-04).")
            return False
        if "vip" in detail_lower:
            print("Error: Anda memilih Reguler, detail meja tidak boleh mengandung kata 'VIP'.")
            return False
            
    return True

def tambah_reservasi(daftar_reservasi: list) -> None:
    print("\n=== TAMBAH RESERVASI RESTORAN ===")
    print("(Ketik 'back' pada kolom mana pun untuk kembali ke input sebelumnya)\n")

    kode_reservasi = generate_kode_reservasi(daftar_reservasi)
    
    nama_pemesan = ""
    jenis = ""
    detail = ""
    tanggal = ""

    # 1. INPUT NAMA
    while True:
        print(f"Kode Reservasi: {kode_reservasi}")
        nama_input = input("Atas Nama: ").strip()
        if nama_input.lower() == "back":
            print("-> Ini adalah input pertama, tidak bisa kembali.")
            continue
        if not nama_input:
            print("Error: Nama pemesan tidak boleh kosong.")
            continue
        nama_pemesan = nama_input
        break

    # 2. INPUT JENIS
    while True:
        jenis_input = input("Jenis Reservasi (Reguler/VIP): ").strip()
        
        if jenis_input.lower() == "back":
            while True:
                nama_input = input(f"Atas Nama (sebelumnya: {nama_pemesan}): ").strip()
                if nama_input.lower() == "back":
                    print("-> Ini adalah input pertama, tidak bisa kembali.")
                    continue
                if not nama_input:
                    print("Error: Nama pemesan tidak boleh kosong.")
                    continue
                nama_pemesan = nama_input
                break
            continue
            
        jenis = normalisasi_jenis(jenis_input)
        if not jenis:
            print("Error: Jenis hanya boleh 'Reguler' atau 'VIP'.")
            continue
        break

    # 3. INPUT DETAIL MEJA
    while True:
        detail_input = input(f"Detail Meja (Ketik '{jenis.lower()}' + nomor, contoh: {jenis}-01): ").strip()
        
        if detail_input.lower() == "back":
            while True:
                jenis_input = input(f"Jenis Reservasi (sebelumnya: {jenis}) (Reguler/VIP): ").strip()
                if jenis_input.lower() == "back":
                    while True:
                        nama_input = input(f"Atas Nama (sebelumnya: {nama_pemesan}): ").strip()
                        if nama_input.lower() == "back":
                            print("-> Ini adalah input pertama.")
                            continue
                        if not nama_input:
                            print("Error: Nama tidak boleh kosong.")
                            continue
                        nama_pemesan = nama_input
                        break
                    continue
                jenis = normalisasi_jenis(jenis_input)
                if not jenis:
                    print("Error: Jenis hanya boleh 'Reguler' atau 'VIP'.")
                    continue
                break
            continue

        if not detail_input:
            print("Error: Detail meja tidak boleh kosong.")
            continue
            
        # Panggil fungsi validasi
        if not cek_detail_meja(detail_input, jenis):
            continue

        detail = detail_input
        break

    # 4. INPUT TANGGAL
    while True:
        tanggal_input = input("Tanggal Kedatangan (YYYY-MM-DD): ").strip()
        
        if tanggal_input.lower() == "back":
            # JIKA USER KETIK BACK, MASUK KE LOOP DETAIL MEJA DENGAN VALIDASI LENGKAP
            while True:
                detail_input = input(f"Detail Meja (sebelumnya: {detail}): ").strip()
                
                if detail_input.lower() == "back":
                    while True:
                        jenis_input = input(f"Jenis Reservasi (sebelumnya: {jenis}) (Reguler/VIP): ").strip()
                        if jenis_input.lower() == "back":
                            while True:
                                nama_input = input(f"Atas Nama (sebelumnya: {nama_pemesan}): ").strip()
                                if nama_input.lower() == "back":
                                    print("-> Ini adalah input pertama.")
                                    continue
                                if not nama_input:
                                    print("Error: Nama tidak boleh kosong.")
                                    continue
                                nama_pemesan = nama_input
                                break
                            continue
                        jenis = normalisasi_jenis(jenis_input)
                        if not jenis:
                            print("Error: Jenis hanya boleh 'Reguler' atau 'VIP'.")
                            continue
                        break
                    continue
                    
                if not detail_input:
                    print("Error: Detail meja tidak boleh kosong.")
                    continue
                    
                # Panggil fungsi validasi di sini juga
                if not cek_detail_meja(detail_input, jenis):
                    continue

                detail = detail_input
                break
            continue

        if not tanggal_input:
            print("Error: Tanggal tidak boleh kosong.")
            continue
        if not validasi_format_tanggal(tanggal_input):
            print("Format tanggal salah atau tidak valid. Gunakan format YYYY-MM-DD (Bulan 01-12, Hari 01-31), contoh: 2026-10-15.")
            continue
        tanggal = tanggal_input
        break

    # --- SIMPAN DATA ---
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
    print("\nProgram penambahan reservasi baru selesai.\n")
    sys.exit()

# --- MENU UTAMA ---
def main():
    daftar_reservasi = []

    while True:
        print("\n" + "=" * 40)
        print("    SISTEM RESERVASI RESTORAN PAWON DIENG")
        print("=" * 40)
        print("1. Tambah Reservasi Baru")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_reservasi(daftar_reservasi)
        elif pilihan == "0":
            print("\nProgram diberhentikan\n")
            sys.exit() 
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()


