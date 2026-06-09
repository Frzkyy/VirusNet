import tool
import json

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
    nama_file = f"{nama.lower()}"

    # Biar virus bisa duplikat
    if os.path.exists(f"data/virus/{nama_file}.json"):
        num = 1
        base_name = nama_file
        while os.path.exists(f"data/virus/{nama_file}.json"):
            nama_file = f"{base_name}({num})"
            num += 1
        nama_file = nama_file + ".json"
    else:
        nama_file = f"{nama_file}.json"
    # ===================================

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
    print("=" * 75)
    pilihan = tool.input_angka_tertentu(1,len(virus_list), pesan_rentang="[Error] Virus Tidak Ditemukan", pesan_input=">> ")
    return virus_list[pilihan - 1]
