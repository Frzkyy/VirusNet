import json
import os
import tool

def load_file(file):
    try:
        with open(f"data/save/{file}","r") as f:
            return json.load(f)
    except:
        return None

def load_virus(file):
    try:
        with open(f"data/virus/{file}","r") as f:
            return json.load(f)
    except:
        return None

def create_virus():
    nama = input("Masukan Nama Virus: ")
    tingkat_penularan = tool.input_angka_tertentu(0.01,1,pesan_input=f"Masukan Tingkat Penularan Virus {nama} (0.01 - 1): ", tipe="float")
    masa_inkubasi = tool.input_angka_tertentu(1,30, pesan_input=f"Masukan Masa Inkubasi Virus {nama} (1 - 30): ")
    mortalitas = tool.input_angka_tertentu(0.01,1,pesan_input=f"Masukan Tingkat Mortalitas Virus {nama} (0.01 - 1): ", tipe="float")
    virus = {
    "nama": nama,
    "tingkat_penularan" : tingkat_penularan,
    "masa_inkubasi": masa_inkubasi,
    "mortalitas": mortalitas
    }
    nama_file = f"{nama.lower()}.json"
    with open(f"data/virus/{nama_file}","w") as f:
        json.dump(virus,f)
    return nama_file

def select_virus():
    virus_list = os.listdir("data/virus")
    num = 1
    print("=" * 30, "Pilih Virus", "=" * 30)
    for i in virus_list:
        virus = load_virus(i)
        print(f"{num}. {virus["nama"]} | Tingkat Penularan: {virus["tingkat_penularan"] * 100}% | Masa Inkubasi: {virus["masa_inkubasi"]} Hari | Mortalitas: {virus["mortalitas"] * 100}%")
        num += 1
    print("0. Buat virus baru")
    print("=" * 75)
    pilihan = tool.input_angka_tertentu(0,len(virus_list), pesan_rentang="[Error] Virus Tidak Ditemukan", pesan_input=">> ")
    if pilihan == 0:
        return create_virus()
    else:
        return virus_list[pilihan - 1]

def new_file():
    template = {
    "nama_kapal": None,
    "hari": None,
    "virus": {
        "nama":None,
        "tingkat_penularan":None,
        "masa_inkubasi":None,
        "mortalitas":None
    },
    "penumpang": [],
    "statistik": {
        "rentan": None,
        "terpapar": None,
        "terinfeksi": None,
        "sembuh": None,
        "meninggal": None
    },
    "log_harian": []
}
    return template