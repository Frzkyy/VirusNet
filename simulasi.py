import random
import tool
import json
import datetime
from features.sorting import bubble_sort_evakuasi, cari_penumpang_berdasarkan_id, cari_penumpang_berdasarkan_lokasi
from structures.linked_list import DoubleLinkedList, CircularLinkedList
from structures.tree import InfectionTree, TreeNode
from structures.queue import Queue
from structures.stack import Stack


def next_day(kapal, virus, pohon, antrian_isolasi, riwayat_aksi):
    """
    Jalankan simulasi satu hari.

    Parameters:
        kapal           : object Ship
        virus           : object Virus
        pohon           : InfectionTree — pohon penularan, root = pasien 0
        antrian_isolasi : Queue — penumpang yang menunggu masuk isolasi
        riwayat_aksi    : Stack — log aksi per hari untuk fitur undo
    """

    print("\n" + "=" * 50)
    print("         SIMULASI HARI BERIKUTNYA")
    print("=" * 50)

    daftar_terpapar  = []
    daftar_sembuh    = []
    daftar_meninggal = []

    # 0. Penumpang beraktivitas — pindah ruangan secara random 
    for penumpang in kapal.penumpang:
        if penumpang.status not in ["meninggal", "sembuh"]:
            deck_baru    = random.randint(1, kapal.jumlah_deck)
            ruangan_baru = random.randint(1, 10)
            penumpang.lokasi.deck    = deck_baru
            penumpang.lokasi.ruangan = ruangan_baru

    # Rebuild graph berdasarkan lokasi baru
    kapal.generate_koneksi()

    # 1. Proses penyebaran 
    for penumpang in kapal.penumpang:
        if penumpang.status == "terinfeksi":
            koneksi = kapal.jaringan.ambil_koneksi(penumpang.id)

            for target_id in koneksi:
                target = kapal.cari_penumpang(target_id)
                if target and target.status == "rentan":
                    if random.random() <= virus.tingkat_penularan:
                        target.terpapar()
                        daftar_terpapar.append(target.nama)

                        # Catat di pohon penularan
                        _tambah_ke_pohon(pohon, penumpang.id, target.id)

    # 2. Update status semua penumpang 
    for penumpang in kapal.penumpang:
        status_sebelum = penumpang.status
        penumpang.update_status(virus.masa_inkubasi, virus.mortalitas)
        status_sesudah = penumpang.status

        # Baru jadi terinfeksi → masuk antrian isolasi
        if status_sebelum == "terpapar" and status_sesudah == "terinfeksi":
            antrian_isolasi.enqueue(penumpang)

        # Baru sembuh
        elif status_sebelum == "terinfeksi" and status_sesudah == "sembuh":
            daftar_sembuh.append(penumpang.nama)

        # Baru meninggal
        elif status_sebelum == "terinfeksi" and status_sesudah == "meninggal":
            daftar_meninggal.append(penumpang.nama)

    # 3. Catat aksi hari ini ke Stack 
    aksi_hari_ini = {
        "terpapar"  : daftar_terpapar[:],
        "sembuh"    : daftar_sembuh[:],
        "meninggal" : daftar_meninggal[:]
    }
    riwayat_aksi.push(aksi_hari_ini)

    #  4. Tampilkan laporan 
    if daftar_terpapar:
        print("\nPenumpang terpapar hari ini:")
        for nama in daftar_terpapar:
            print(f"  - {nama}")
    else:
        print("\nTidak ada penularan baru.")

    if daftar_sembuh:
        print("\nPenumpang sembuh hari ini:")
        for nama in daftar_sembuh:
            print(f"  + {nama}")

    if daftar_meninggal:
        print("\nPenumpang meninggal hari ini:")
        for nama in daftar_meninggal:
            print(f"  x {nama}")

    if not antrian_isolasi.is_empty():
        print(f"\nAntrian isolasi saat ini: {antrian_isolasi.size()} orang")

    statistik = kapal.statistik()
    print("\n=== STATISTIK ===")
    for key, value in statistik.items():
        print(f"  {key:12} : {value}")

    return statistik


def simulasi_selesai(statistik):
    """Return True kalau tidak ada lagi yang terinfeksi atau terpapar."""
    return statistik["terinfeksi"] == 0 and statistik["terpapar"] == 0


# Helper internal 
def _tambah_ke_pohon(pohon, id_sumber, id_target):
    """Cari node sumber di pohon secara rekursif, lalu tambah target sebagai child."""
    node_sumber = _cari_node(pohon.root, id_sumber)
    if node_sumber:
        node_sumber.add_child(TreeNode(id_target))


def _cari_node(node, target_id):
    if node.data == target_id:
        return node
    for child in node.children:
        hasil = _cari_node(child, target_id)
        if hasil:
            return hasil
    return None




def _grafik_ascii(log_harian):
    if not log_harian:
        print("  (belum ada data harian)")
        return

    print("\n=== GRAFIK KASUS PER HARI ===")
    maks = max(h["terpapar"] + h["terinfeksi"] for h in log_harian)
    if maks == 0:
        maks = 1

    for i, hari in enumerate(log_harian, 1):
        total = hari["terpapar"] + hari["terinfeksi"]
        bar = "█" * int((total / maks) * 30)
        print(f"  Hari {i:3} | {bar} {total}")


def _statistik_akhir(kapal, log_harian, pohon):
    print("\n" + "=" * 50)
    print("           SIMULASI SELESAI")
    print("=" * 50)

    stat = kapal.statistik()
    print(f"\n  Total Penumpang  : {kapal.jumlah_penumpang}")
    print(f"  Sembuh           : {stat['sembuh']}")
    print(f"  Meninggal        : {stat['meninggal']}")
    print(f"  Tidak Terinfeksi : {stat['rentan']}")

    _grafik_ascii(log_harian)

    print("\n=== RANTAI PENULARAN AKHIR ===")
    _print_tree_dengan_nama(pohon.root, kapal)


def _menu_lockdown(kapal, deck_terkunci):
    print("\n=== LOCKDOWN DECK ===")
    print(f"Jumlah deck: 1 - {kapal.jumlah_deck}")
    deck = tool.input_angka_tertentu(1, kapal.jumlah_deck, pesan_input="Masukan nomor deck yang ingin di-lockdown: ")

    if deck in deck_terkunci:
        print(f"[Info] Deck {deck} sudah dalam kondisi lockdown.")
        return

    kapal.deck_terkunci.add(deck)
    deck_terkunci.add(deck)

    kapal.generate_koneksi()
    print(f"[Sistem] Deck {deck} berhasil di-lockdown. Semua koneksi di deck ini diputus.")


def _menu_buka_lockdown(kapal, deck_terkunci):
    if not deck_terkunci:
        print("[Info] Tidak ada deck yang sedang di-lockdown.")
        return

    print("\n=== BUKA LOCKDOWN ===")
    print(f"Deck yang sedang di-lockdown: {sorted(deck_terkunci)}")
    deck = tool.input_angka_tertentu(1, kapal.jumlah_deck, pesan_input="Masukan nomor deck yang ingin dibuka lockdown-nya: ")

    if deck not in deck_terkunci:
        print(f"[Info] Deck {deck} tidak sedang di-lockdown.")
        return

    kapal.deck_terkunci.remove(deck)
    deck_terkunci.remove(deck)

    kapal.generate_koneksi()

    print(f"[Sistem] Lockdown deck {deck} berhasil dibuka.")


def _menu_evakuasi(kapal):
    print("\n=== EVAKUASI ===")

    terinfeksi = [p for p in kapal.penumpang if p.status == "terinfeksi"]

    if not terinfeksi:
        print("[Info] Tidak ada penumpang yang sedang terinfeksi.")
        return

    prioritas = bubble_sort_evakuasi(terinfeksi)

    # Pakai Circular Linked List untuk simulasi rotasi shift petugas medis
    petugas = CircularLinkedList()
    petugas.append("Dr. Andi")
    petugas.append("Dr. Budi")
    petugas.append("Dr. Citra")

    print(f"\n{'No':<4} {'Nama':<25} {'Hari Terinfeksi':<18} {'Petugas'}")
    print("-" * 60)

    current_petugas = petugas.head
    for i, p in enumerate(prioritas, 1):
        print(f"{i:<4} {p.nama:<25} {p.hari_terinfeksi:<18} {current_petugas.data}")
        current_petugas = current_petugas.next


def _print_tree_dengan_nama(node, kapal, level=0):
    penumpang = kapal.cari_penumpang(node.data)
    nama = penumpang.nama if penumpang else f"ID {node.data}"
    print("   " * level + "|- " + nama)
    for child in node.children:
        _print_tree_dengan_nama(child, kapal, level + 1)


def _menu_rantai_penularan(kapal, pohon):
    print("\n=== RANTAI PENULARAN ===")
    _print_tree_dengan_nama(pohon.root, kapal)


def _menu_cari_penumpang(kapal):
    print("\n=== CARI PENUMPANG ===")
    print("1. Berdasarkan Nama")
    print("2. Berdasarkan ID")
    print("3. Berdasarkan Status")
    print("4. Berdasarkan Lokasi")
    print("0. Batal")

    pilihan = tool.input_angka_tertentu(0, 4, pesan_input=">> ")

    hasil = []

    if pilihan == 1:
        nama = input("Masukan nama (atau sebagian nama): ")
        hasil = [p for p in kapal.penumpang if nama.lower() in p.nama.lower()]

    elif pilihan == 2:
        id_cari = tool.input_angka(pesan_input="Masukan ID penumpang: ")
        p = cari_penumpang_berdasarkan_id(kapal.penumpang, id_cari)
        hasil = [p] if p else []

    elif pilihan == 3:
        status_valid = ["rentan", "terpapar", "terinfeksi", "sembuh", "meninggal"]
        print("Status yang tersedia:")
        for i, s in enumerate(status_valid, 1):
            print(f"  {i}. {s}")
        pilihan_status = tool.input_angka_tertentu(1, len(status_valid), pesan_input="Pilih status >> ")
        status = status_valid[pilihan_status - 1]
        hasil = [p for p in kapal.penumpang if p.status == status]

    elif pilihan == 4:
        deck = tool.input_angka_tertentu(1, kapal.jumlah_deck, pesan_input="Masukan deck: ")
        hasil = cari_penumpang_berdasarkan_lokasi(kapal.penumpang, deck)

    elif pilihan == 0:
        return

    if not hasil:
        print("[Info] Penumpang tidak ditemukan.")
        return

    print(f"\nDitemukan {len(hasil)} penumpang:")
    print(f"{'ID':<5} {'Nama':<25} {'Status':<12} {'Lokasi'}")
    print("-" * 60)
    for p in hasil:
        print(f"{p.id:<5} {p.nama:<25} {p.status:<12} {p.lokasi}")

        # Pakai Double Linked List untuk tampilkan riwayat status
        riwayat = p.riwayat_status if hasattr(p, "riwayat_status") else None
        if riwayat:
            print("  Riwayat status: ", end="")
            riwayat.display_forward()


def _simpan(kapal, virus, data, save_name, pohon):
    data["save_date"] = str(datetime.datetime.now())
    data["statistik"] = kapal.statistik()

    penumpang_baru = []
    for p in kapal.penumpang:
        penumpang_baru.append({
            "id": p.id,
            "nama": p.nama,
            "umur": p.umur,
            "status": p.status,
            "lokasi": {"deck": p.lokasi.deck, "ruangan": p.lokasi.ruangan},
            "hari_terpapar": p.hari_terpapar,
            "hari_terinfeksi": p.hari_terinfeksi
        })

    data["penumpang"] = penumpang_baru
    data["pohon_penularan"] = _pohon_ke_dict(pohon.root)
    data["id_pasien_0"] = pohon.root.data

    with open(f"data/save/{save_name}", "w") as f:
        json.dump(data, f)

    print(f"[Sistem] Simulasi berhasil disimpan ke \"{save_name}\".")


def _menu_simulasi(hari):
    print("\n" + "=" * 50)
    print(f"                   Hari ke-{hari}")
    print("=" * 50)
    print("1. Next Day")
    print("2. Lockdown Deck")
    print("3. Buka Lockdown")
    print("4. Evakuasi")
    print("5. Rantai Penularan")
    print("6. Cari Penumpang")
    print("7. Simpan")
    print("0. Keluar ke Menu Utama")
    print("=" * 50)


def jalankan_simulasi(kapal, virus, data, save_name, id_pasien_0):
    """
    Loop utama simulasi.

    Parameters:
        kapal       : object Ship
        virus       : object Virus
        data        : dict dari save file (untuk update & simpan)
        save_name   : nama file save (misal 'KapalMaju.json')
        id_pasien_0 : ID penumpang pertama yang terinfeksi
    """

    # Inisialisasi struktur data simulasi
    if "pohon_penularan" in data and data["pohon_penularan"]:
        root = _dict_ke_pohon(data["pohon_penularan"])
        pohon = InfectionTree(id_pasien_0)
        pohon.root = root
    else:
        pohon = InfectionTree(id_pasien_0)
    antrian_isolasi = Queue()
    riwayat_aksi    = Stack()
    deck_terkunci   = set()
    log_harian      = data.get("log_harian", [])

    while True:
        tool.clear_screen()
        _menu_simulasi(data["hari"])
        pilihan = tool.input_angka_tertentu(0, 7, pesan_input=">> ")

        if pilihan == 1:
            statistik = next_day(kapal, virus, pohon, antrian_isolasi, riwayat_aksi)
            log_harian.append(statistik)
            data["log_harian"] = log_harian
            data["hari"] += 1

            if simulasi_selesai(statistik):
                _statistik_akhir(kapal, log_harian, pohon)
                input("\nTekan Enter untuk kembali ke menu utama...")
                break

        elif pilihan == 2:
            _menu_lockdown(kapal, deck_terkunci)

        elif pilihan == 3:
            _menu_buka_lockdown(kapal, deck_terkunci)

        elif pilihan == 4:
            _menu_evakuasi(kapal)

        elif pilihan == 5:
            _menu_rantai_penularan(kapal, pohon)

        elif pilihan == 6:
            _menu_cari_penumpang(kapal)

        elif pilihan == 7:
            _simpan(kapal, virus, data, save_name, pohon)

        elif pilihan == 0:
            simpan = input("\nSimpan sebelum keluar? (y/n): ").strip().lower()
            if simpan == "y":
                _simpan(kapal, virus, data, save_name, pohon)
            break

        input("\nTekan Enter untuk melanjutkan...")

def _pohon_ke_dict(node):
    """Rekursif: ubah TreeNode jadi dict."""
    return {
        "id": node.data,
        "children": [_pohon_ke_dict(child) for child in node.children]
    }

def _dict_ke_pohon(d):
    """Rekursif: ubah dict balik jadi TreeNode."""
    node = TreeNode(d["id"])
    for child_dict in d["children"]:
        node.add_child(_dict_ke_pohon(child_dict))
    return node