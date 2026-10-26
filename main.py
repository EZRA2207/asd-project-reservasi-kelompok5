"""
Sistem Reservasi Restoran Pawon Dieng
Menu utama untuk menghubungkan F1, F2, F3, F4, dan F5.
"""

import sys
from pathlib import Path

# Menambahkan folder utama proyek ke jalur pencarian Python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Import fungsi fitur F1 sampai F5
from fitur.tambah_reservasi_baru import tambah_reservasi
from fitur.tampilkan_semua_reservasi import tampilkan_semua_reservasi
from fitur.cari_reservasi import cari_reservasi
from fitur.update_status_reservasi import update_status_reservasi
from fitur.filter_reservasi_berdasarkan_status import filter_reservasi_berdasarkan_status


def main():
    daftar_reservasi = []

    while True:
        print("\n" + "=" * 40)
        print("    SISTEM RESERVASI RESTORAN PAWON DIENG")
        print("=" * 40)
        print("1. Tambah Reservasi Baru")
        print("2. Tampilkan Semua Reservasi")
        print("3. Cari Reservasi")
        print("4. Update Status Reservasi")
        print("5. Filter Reservasi Berdasarkan Status")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_reservasi(daftar_reservasi)

        elif pilihan == "2":
            tampilkan_semua_reservasi(daftar_reservasi)

        elif pilihan == "3":
            cari_reservasi(daftar_reservasi)

        elif pilihan == "4":
            update_status_reservasi(daftar_reservasi)

        elif pilihan == "5":
            filter_reservasi_berdasarkan_status(daftar_reservasi)

        elif pilihan == "0":
            print("\nProgram diberhentikan. Terima kasih!\n")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()