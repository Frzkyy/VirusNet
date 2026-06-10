import json
import os
import tool
import datetime
import random
from faker import Faker
import time
import virus_manager

def load_file(file):
    try:
        with open(f"data/save/{file}","r") as f:
            return json.load(f)
    except:
        return None


def create_penumpang(banyak, jumlah_deck, jumlah_ruangan=10):
    penumpang = []
    num = 1
    fake = Faker()
    for _ in range(banyak):
        lokasi = {
            "deck": random.randint(1, jumlah_deck),
            "ruangan": random.randint(1, jumlah_ruangan)
        }
        penumpang.append({
            "id": num,
            "nama": str(fake.name()),
            "umur": random.randint(1, 90),
            "status": "rentan",
            "lokasi": lokasi
        })
        num += 1
    return penumpang


def new_file():
    template = {
    "save_name": None,
    "save_date": str(datetime.datetime.now()),
    "nama_kapal": None,
    "jumlah_deck": None,
    "hari": 1,
    "virus": {
        "nama":None,
        "tingkat_penularan":None,
        "masa_inkubasi":None,
        "mortalitas":None
    },
    "penumpang": [],
    "statistik": {
        "rentan": 0,
        "terpapar": 0,
        "terinfeksi": 0,
        "sembuh": 0,
        "meninggal": 0
    },
    "log_harian": []
}
    
    print("=" * 50)
    print("                 VirusNet v1.0")
    print("   Konfigurasi Awal Simulasi Penyebaran Virus")
    print("=" * 50)

    template["save_name"] = input("Masukan Nama Save: ")
    print(f"[Sistem] Membuat File \"{template['save_name']}\"...\n")
    time.sleep(1)

    # Biar save file bisa duplikat
    save_name = f"{template['save_name'].replace(' ','')}"
    if os.path.exists(f"data/save/{save_name}.json"):
        num = 1
        base_name = save_name
        while os.path.exists(f"data/save/{save_name}.json"):
            save_name = f"{base_name}({num})"
            num += 1
        save_name = save_name + ".json"
    else:
        save_name = f"{save_name}.json"
    # =================================

    template["nama_kapal"] = input("Masukan Nama Kapal: ")
    print(f"[Sistem] Mengubah Nama Kapal Menjadi \"{template['nama_kapal']}\"...\n")

    jumlah_deck = tool.input_angka(pesan_input="Masukan Jumlah Deck: ")
    template["jumlah_deck"] = jumlah_deck
    print(f"[Sistem] Kapal \"{template['nama_kapal']}\" memiliki {jumlah_deck} deck.\n")

    virus = virus_manager.select_virus()
    with open(f"data/virus/{virus}", "r") as f:
        template["virus"] = json.load(f)
    print(f"[Sistem] Meluncurkan Virus \"{template['virus']['nama']}\"...\n")

    banyak_penumpang = tool.input_angka(pesan_input="Masukan Banyak Penumpang: ")
    print(f"[Sistem] Memasukan {banyak_penumpang} Penumpang Kedalam Kapal {template['nama_kapal']}...\n")
    time.sleep(1)
    
    template["penumpang"] = create_penumpang(banyak_penumpang, jumlah_deck)

    with open(f"data/save/{save_name}","w") as f:
        json.dump(template, f)
    return save_name


def pilih_save():
    save_list = os.listdir("data/save")

    if not save_list:
        print("[Error] Tidak ada save file yang tersedia.")
        return None

    print("=" * 50)
    print("               Pilih Save File")
    print("=" * 50)
    for i, file in enumerate(save_list, 1):
        data = load_file(file)
        if data:
            print(f"{i}. {data['save_name']} | Kapal: {data['nama_kapal']} | Hari: {data['hari']} | Virus: {data['virus']['nama']}")
        else:
            print(f"{i}. {file} (gagal dibaca)")
    print("0. Batal")
    print("=" * 50)

    pilihan = tool.input_angka_tertentu(0, len(save_list), pesan_input=">> ")

    if pilihan == 0:
        return None

    return save_list[pilihan - 1]


def load_ship(file):
    """
    Baca save file JSON dan reconstruct jadi object Ship yang siap disimulasikan.
    Return: (kapal, virus, data) atau (None, None, None) kalau gagal.
    """
    from ship import Ship
    from classes.person import Person
    from classes.location import Location
    from classes.virus import Virus

    data = load_file(file)
    if data is None:
        print(f"[Error] Gagal memuat file \"{file}\".")
        return None, None, None

    # --- Reconstruct Ship ---
    jumlah_deck    = data.get("jumlah_deck", 1)
    jumlah_penumpang = len(data["penumpang"])

    kapal = Ship(data["nama_kapal"], jumlah_deck, jumlah_penumpang)

    # --- Reconstruct setiap Person + isi Graph & HashTable ---
    for p in data["penumpang"]:

        lok = p["lokasi"]

        # FIX: save file lama punya "lokasi": null, kasih lokasi random biar tidak crash
        if lok is None:
            lokasi = Location(random.randint(1, jumlah_deck), random.randint(1, 10))
        else:
            lokasi = Location(lok["deck"], lok["ruangan"])

        orang = Person(
            p["id"],
            p["nama"],
            p["umur"],
            p["status"],
            lokasi
        )

        # Pulihkan counter hari kalau ada di save (opsional, untuk save lanjutan)
        orang.hari_terpapar   = p.get("hari_terpapar", 0)
        orang.hari_terinfeksi = p.get("hari_terinfeksi", 0)

        kapal.penumpang.append(orang)
        kapal.db.set(orang.id, orang)
        kapal.jaringan.tambah_penumpang(orang.id)

    # Generate koneksi graph berdasarkan lokasi yang sudah ada
    kapal.generate_koneksi()

    # --- Reconstruct Virus ---
    v = data["virus"]
    virus = Virus(
        v["nama"],
        v["tingkat_penularan"],
        v["masa_inkubasi"],
        v["mortalitas"]
    )

    print(f"[Sistem] Save \"{data['save_name']}\" berhasil dimuat.")
    print(f"         Kapal  : {kapal.nama_kapal} ({jumlah_penumpang} penumpang, {jumlah_deck} deck)")
    print(f"         Virus  : {virus.nama}")
    print(f"         Hari   : {data['hari']}\n")

    return kapal, virus, data