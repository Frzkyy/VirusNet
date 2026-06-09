import tool
import json
import os


def load_virus(file):
    try:
        with open(f"data/virus/{file}", "r") as f:
            return json.load(f)
    except:
        return None


def list_virus():
    virus_list = os.listdir("data/virus")
    print("=" * 75)
    for i, file in enumerate(virus_list, 1):
        virus = load_virus(file)
        print(f"{i}. {virus['nama']} | Penularan: {virus['tingkat_penularan'] * 100}% | Inkubasi: {virus['masa_inkubasi']} Hari | Mortalitas: {virus['mortalitas'] * 100}%")
    print("=" * 75)
    return virus_list


def select_virus():
    virus_list = os.listdir("data/virus")
    num = 1
    print("=" * 30, "Pilih Virus", "=" * 30)
    for i in virus_list:
        virus = load_virus(i)
        print(f"{num}. {virus['nama']} | Tingkat Penularan: {virus['tingkat_penularan'] * 100}% | Masa Inkubasi: {virus['masa_inkubasi']} Hari | Mortalitas: {virus['mortalitas'] * 100}%")
        num += 1
    print("=" * 75)
    pilihan = tool.input_angka_tertentu(1, len(virus_list), pesan_rentang="[Error] Virus Tidak Ditemukan", pesan_input=">> ")
    return virus_list[pilihan - 1]


def create_virus():
    nama = input("Masukan Nama Virus: ")
    tingkat_penularan = tool.input_angka_tertentu(0.01, 1, pesan_input=f"Masukan Tingkat Penularan Virus {nama} (0.01 - 1): ", tipe="float")
    masa_inkubasi = tool.input_angka_tertentu(1, 30, pesan_input=f"Masukan Masa Inkubasi Virus {nama} (1 - 30): ")
    mortalitas = tool.input_angka_tertentu(0.01, 1, pesan_input=f"Masukan Tingkat Mortalitas Virus {nama} (0.01 - 1): ", tipe="float")
    virus = {
        "nama": nama,
        "tingkat_penularan": tingkat_penularan,
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

    with open(f"data/virus/{nama_file}", "w") as f:
        json.dump(virus, f)

    print(f"\n[Sistem] Virus \"{nama}\" berhasil dibuat.\n")
    return nama_file


def edit_virus():
    virus_list = os.listdir("data/virus")

    if not virus_list:
        print("[Error] Tidak ada virus yang tersedia.")
        return

    print("=" * 30, "Edit Virus", "=" * 30)
    file_dipilih = select_virus()
    virus = load_virus(file_dipilih)

    print(f"\nEdit Virus: {virus['nama']}")
    print("Kosongkan input dan tekan Enter untuk tidak mengubah nilai.\n")

    # Nama
    nama_baru = input(f"Nama [{virus['nama']}]: ").strip()
    if nama_baru:
        virus["nama"] = nama_baru

    # Tingkat penularan
    input_penularan = input(f"Tingkat Penularan [{virus['tingkat_penularan']}] (0.01 - 1): ").strip()
    if input_penularan:
        try:
            val = float(input_penularan)
            if 0.01 <= val <= 1:
                virus["tingkat_penularan"] = val
            else:
                print("[Peringatan] Nilai di luar rentang, tidak diubah.")
        except ValueError:
            print("[Peringatan] Input tidak valid, tidak diubah.")

    # Masa inkubasi
    input_inkubasi = input(f"Masa Inkubasi [{virus['masa_inkubasi']}] (1 - 30): ").strip()
    if input_inkubasi:
        try:
            val = int(input_inkubasi)
            if 1 <= val <= 30:
                virus["masa_inkubasi"] = val
            else:
                print("[Peringatan] Nilai di luar rentang, tidak diubah.")
        except ValueError:
            print("[Peringatan] Input tidak valid, tidak diubah.")

    # Mortalitas
    input_mortalitas = input(f"Mortalitas [{virus['mortalitas']}] (0.01 - 1): ").strip()
    if input_mortalitas:
        try:
            val = float(input_mortalitas)
            if 0.01 <= val <= 1:
                virus["mortalitas"] = val
            else:
                print("[Peringatan] Nilai di luar rentang, tidak diubah.")
        except ValueError:
            print("[Peringatan] Input tidak valid, tidak diubah.")

    with open(f"data/virus/{file_dipilih}", "w") as f:
        json.dump(virus, f)

    print(f"\n[Sistem] Virus \"{virus['nama']}\" berhasil diperbarui.\n")


def delete_virus():
    virus_list = os.listdir("data/virus")

    if not virus_list:
        print("[Error] Tidak ada virus yang tersedia.")
        return

    if len(virus_list) == 1:
        print("[Error] Minimal harus ada 1 virus. Tidak bisa menghapus semua virus.")
        return

    print("=" * 30, "Hapus Virus", "=" * 30)
    file_dipilih = select_virus()
    virus = load_virus(file_dipilih)

    konfirmasi = input(f"\nYakin ingin menghapus virus \"{virus['nama']}\"? (y/n): ").strip().lower()

    if konfirmasi == "y":
        os.remove(f"data/virus/{file_dipilih}")
        print(f"\n[Sistem] Virus \"{virus['nama']}\" berhasil dihapus.\n")
    else:
        print("\n[Sistem] Penghapusan dibatalkan.\n")


def konfigurasi_virus():
    while True:
        tool.clear_screen()
        print("=" * 50)
        print("                Konfigurasi Virus")
        print("=" * 50)
        list_virus()
        print("1. Edit Virus")
        print("2. Hapus Virus")
        print("3. Buat Virus Baru")
        print("0. Keluar")
        print("=" * 50)
        pilihan = tool.input_angka_tertentu(0, 3, pesan_input=">> ")
        print()
        match pilihan:
            case 1:
                edit_virus()
                input("Tekan Enter untuk melanjutkan...")
            case 2:
                delete_virus()
                input("Tekan Enter untuk melanjutkan...")
            case 3:
                create_virus()
                input("Tekan Enter untuk melanjutkan...")
            case 0:
                return