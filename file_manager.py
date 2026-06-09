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



def create_penumpang(banyak):
    penumpang = []
    num = 1
    fake = Faker()
    for _ in range(banyak):
        penumpang.append({"id" : num, "nama" : str(fake.name()), "umur":random.randint(1,90), "status":"rentan", "lokasi" : None})
        num += 1
    return penumpang


def new_file():
    template = {
    "save_name": None,
    "save_date": str(datetime.datetime.now()),
    "nama_kapal": None,
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
    print(f"[Sistem] Membuat File \"{template["save_name"]}\"...\n")
    time.sleep(1)


    # Biar save file bisa duplikat
    save_name = f"{template["save_name"].replace(" ","")}"
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
    print(f"[Sistem] Mengubah Nama Kapal Menajadi \"{template['nama_kapal']}\"...\n")

    virus = virus_manager.select_virus()
    with open(f"data/virus/{virus}", "r") as f:
        template["virus"] = json.load(f)
    print(f"[Sistem] Meluncurkan Virus \"{template["virus"]["nama"]}\"...\n")


    banyak_penumpang = tool.input_angka(pesan_input="Masukan Banyak Penumpang: ")
    print(f"[Sistem] Memasukan {banyak_penumpang} Penumpang Kedalam Kapal {template['nama_kapal']}...\n")
    time.sleep(1)
    
    template["penumpang"] = create_penumpang(banyak_penumpang)

    with open(f"data/save/{save_name}","w") as f:
        json.dump(template, f)
    return save_name


