import file_manager
import tool
import virus_manager
import simulasi


def about():
    print("=" * 50)
    print("            Aplikasi Ini Dibuat Oleh:")
    print("=" * 50)
    print("Ketua: Said Fairuz Zacky")
    print("Anggota 1: Ketrin Aprilia Pandiangan")
    print("Anggota 2: Rasyikah Azzahra")
    print("=" * 50)
    while True:
        a = input("Ketik exit untuk keluar\n")
        if a.lower() == "exit":
            break 

def menu():
    print("=" * 50)
    print("                  VirusNet v1.0")
    print("                   Menu Utama")
    print("=" * 50)
    print("Pilih Menu: ")
    print("1. Simulasi baru")
    print("2. Pilih Save File")
    print("3. Konfigurasi Virus")
    print("4. About")
    print("0. Keluar Aplikasi")
    print("=" * 50)


def pilih_pasien_0(kapal):
    print("\n=== PILIH PASIEN 0 ===")
    print("(Orang pertama yang terinfeksi)\n")
    kapal.tampilkan_penumpang()
    print()
    id_pasien = tool.input_angka_tertentu(1, kapal.jumlah_penumpang, pesan_input="Masukan ID pasien 0: ")
    pasien = kapal.cari_penumpang(id_pasien)
    if pasien:
        pasien.status = "terinfeksi"
        print(f"\n[Sistem] {pasien.nama} ditetapkan sebagai pasien 0.\n")
    return id_pasien


while True:

    tool.clear_screen()
    menu()
    pilihan = tool.input_angka_tertentu(0,4, pesan_input=">> ")
    tool.clear_screen()
    print()
    match pilihan:
        case 1:
            save_name = file_manager.new_file()
            kapal, virus, data = file_manager.load_ship(save_name)
            if kapal:
                id_pasien_0 = pilih_pasien_0(kapal)
                input("Tekan Enter untuk mulai simulasi...")
                simulasi.jalankan_simulasi(kapal, virus, data, save_name, id_pasien_0)
        case 2:
            save_name = file_manager.pilih_save()
            if save_name:
                kapal, virus, data = file_manager.load_ship(save_name)
                if kapal:
                    # Cek apakah sudah ada yang terinfeksi (lanjutan save)
                    ada_terinfeksi = any(p.status in ["terinfeksi", "terpapar"] for p in kapal.penumpang)
                    if not ada_terinfeksi:
                        id_pasien_0 = pilih_pasien_0(kapal)
                    else:
                        # Ambil pasien pertama yang terinfeksi sebagai root pohon
                        id_pasien_0 = next((p.id for p in kapal.penumpang if p.status == "terinfeksi"),None)
                        print(f"[Sistem] Melanjutkan simulasi hari ke-{data['hari']}...\n")
                    input("Tekan Enter untuk mulai simulasi...")
                    simulasi.jalankan_simulasi(kapal, virus, data, save_name, id_pasien_0)
        case 3:
            virus_manager.konfigurasi_virus()
        case 4:
            about()
        case 0:
            print("=" * 20)
            print(f"    Terima Kasih")
            print("=" * 20)

            break