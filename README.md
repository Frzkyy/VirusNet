# VirusNet

Simulasi penyebaran virus dalam lingkungan tertutup, ditulis menggunakan Python.

Program ini memodelkan bagaimana sebuah virus dapat berpindah dari satu individu ke individu lain di dalam sebuah kapal penumpang. Setiap sesi simulasi dapat dikonfigurasi, disimpan, dan dilanjutkan kapan saja.

---

## Daftar Isi

- [Tentang Project](#tentang-project)
- [Cara Menggunakan](#cara-menggunakan)
- [Konfigurasi](#konfigurasi)
- [Struktur Kode](#struktur-kode)
- [Tim](#tim)

---

## Tentang Project

VirusNet dibuat sebagai tugas kelompok untuk mempelajari penerapan struktur data dalam pemodelan sistem nyata. Simulasi ini terinspirasi dari konsep epidemiologi dasar, di mana sebuah penyakit menyebar melalui kontak antar individu dalam ruang yang terbatas.

Alur kerja program secara umum:

Pengguna memilih satu penumpang sebagai sumber infeksi pertama, lalu menjalankan simulasi. Setiap ronde, virus menyebar ke penumpang lain berdasarkan parameter yang sudah dikonfigurasi sebelumnya. Status setiap penumpang ditampilkan secara langsung, dan hasil simulasi dapat disimpan untuk dilanjutkan di lain waktu.

---

## Cara Menggunakan

Pastikan Python 3 sudah terpasang di sistem kamu.

```bash
git clone https://github.com/Frzkyy/VirusNet.git
cd VirusNet
python main.py
```

Setelah program berjalan, akan muncul menu utama dengan empat pilihan:

```
[1] Simulasi Baru       — mulai sesi simulasi dari awal
[2] Pilih Save File     — lanjutkan simulasi yang pernah disimpan
[3] Konfigurasi Virus   — ubah parameter sebelum simulasi dimulai
[4] About               — informasi program dan tim
```

Tidak ada dependensi eksternal yang perlu dipasang. Program berjalan sepenuhnya dengan pustaka bawaan Python.

---

## Konfigurasi

Sebelum simulasi dimulai, kamu bisa mengatur parameter virus melalui menu Konfigurasi Virus. Parameter ini mempengaruhi jalannya simulasi secara keseluruhan, termasuk seberapa cepat virus menyebar dan berapa lama masa inkubasinya.

Konfigurasi disimpan bersama save file, sehingga setiap sesi simulasi bisa memiliki karakteristik virus yang berbeda-beda.

---

## Struktur Kode

```
VirusNet/
├── main.py              entry point program
├── simulasi.py          logika inti penyebaran virus per ronde
├── ship.py              representasi kapal dan penumpang di dalamnya
├── virus_manager.py     pengelolaan konfigurasi parameter virus
├── file_manager.py      penyimpanan dan pemuatan sesi simulasi
├── classes/             definisi objek utama (Penumpang, Kapal, Virus)
├── features/            fitur-fitur pendukung program
├── structures/          struktur data yang digunakan
└── data/                tempat save file simulasi tersimpan
```

---

## Tim

Project ini dikerjakan oleh tiga orang sebagai bagian dari tugas kelompok.

Said Fairuz Zacky sebagai ketua, bersama Ketrin Aprilia Pandiangan dan Rasyikah Azzahra sebagai anggota.

---

Project ini dibuat untuk keperluan akademik.
