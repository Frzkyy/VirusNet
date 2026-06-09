import file_manager
import tool
import datetime
import os
import virus_manager

def about():
    print("=" * 50)
    print("            Aplikasi Ini Dibuat Oleh:")
    print("=" * 50)
    print("Ketua: Said Fairuz Zacky")
    print("Anggota 1: Ketrin Aprilia Pandiangan")
    print("Anggota 2: Rasyikah Azzahra")
    print("=" * 50)
    input("Tekan key apapun untuk keluar\n")

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


while True:

    tool.clear_screen()
    menu()
    pilihan = tool.input_angka_tertentu(0,4, pesan_input=">> ")
    tool.clear_screen()
    print()
    match pilihan:
        case 1:
            file_manager.new_file()
        case 2:
            pass
        case 3:
            virus_manager.konfigurasi_virus()
        case 4:
            about()
        case 0:
            print("=" * 20)
            print(f"    Terima Kasih")
            print("=" * 20)

            break
    

