# Sistem Reservasi | Kelompok 5

Project mata kuliah Algoritma dan Struktur Data
Program Studi Sistem Informasi, FTI Universitas Merdeka Malang
Semester 3, Tahun Ajaran 2026/2027

## 1. Deskripsi Sistem

Sistem Reservasi adalah program berbasis Command Line Interface (CLI) yang dibuat menggunakan Python untuk mengelola data reservasi tiket atau ruangan. Sistem ini membantu admin mencatat, menampilkan, mencari, memperbarui status, memfilter, dan menghapus data reservasi.

Data reservasi disimpan menggunakan struktur data list of dictionary (Array of Struct), sesuai materi Algoritma dan Struktur Data Tahap 1. 

## 2. Anggota Kelompok

| No. | Nama Anggota | NIM | Tanggung Jawab |
| :--- | :--- | :--- | :--- |
| 1 | Gilang Ramadhani | [2508300027] | F1: Tambah reservasi baru |
| 2 | Yosepius Richard Simu | [2508300030] | F2: Tampilkan semua reservasi |
| 3 | Fitzartur Ezra Auriel | [2508300044] | F3: Cari reservasi |
| 4 | Stevanus Noel Shanata | [2508300034] | F4: Update status reservasi |
| 5 | | | F5: Filter reservasi berdasarkan status |
| 6 | Yohanes Ananto P | [23083000005] | F6: Hapus reservasi |

## 3. Cara Menjalankan Program

Pastikan komputer Anda sudah terinstal Python 3 (versi 3.8 ke atas). Ikuti langkah-langkah berikut untuk menjalankan program:

1. Clone repository ini ke perangkat lokal Anda:


git clone https://github.com/HumanCanAlive/asd-project-reservasi-kelompok2.git

2. Masuk ke direktori repository:

cd asd-project-reservasi-kelompok5

3. Jalankan program utama melalui terminal:

python main.py

## 4. Fitur yang Sudah Ada (Tahap 1: Array & Struct)

Pada Tahap 1 (Checkpoint UTS), sistem telah mengimplementasikan 6 fitur wajib utama:

F1: Tambah Reservasi Baru — Menambahkan data pemesanan lengkap dengan validasi kode unik, non-kosong, pilihan jenis, dan format tanggal YYYY-MM-DD.

F2: Tampilkan Semua Reservasi — Menampilkan seluruh data reservasi dalam bentuk tabel yang rapi beserta indikator status.

F3: Cari Reservasi — Pencarian data berdasarkan Kode Reservasi (exact match) atau Nama Pemesan (partial match).

F4: Update Status Reservasi — Mengubah status pemesanan (menjadi "Selesai" atau "Dibatalkan") dengan aturan status final.

F5: Filter Reservasi Berdasarkan Status — Menyaring dan menampilkan data berdasarkan status tertentu ("Aktif", "Selesai", atau "Dibatalkan").

F6: Hapus Reservasi — Menghapus data reservasi dari sistem yang didahului dengan tampilan detail dan konfirmasi keamanan (y/n).

## 5. Pembagian Tugas

Berikut adalah pembagian tugas pengerjaan modul di dalam kelompok:

Fitzartur Ezra Auriel -- (Ketua) -- Fitur 3 dan 5 Cari Reservasi dan filter reservasi berdasarkan status
- Membuat struktur file github
- Fitur 3 Cari Reservasi
- Fitur 5 filter reservasi berdasarkan status
- Menyusun README.md

Gilang Ramadhani -- Fitur 1 dan 5 tambah reservasi baru dan filter reservasi berdasarkan status
- Fitur 1 tambah reservasi baru
- Fitur 5 filter reservasi berdasarkan status
- Menyusun README.md
- Memperbaiki beberapa isi fitur 4

Yosepius Richard Simu -- Fitur 2 Tampilkan Semua Resevasi 
- Fitur 2 Tampilkan Semua Resevasi
- Menyusun Laporan

Stevanus Noel Shanata -- Fitur 4 Update Status Reservasi
- Fitur 4 Update Status Reservasi

Yohanes Ananto P -- Fitur 6 Hapus Reservasi
- Fitur Hapus Reservasi