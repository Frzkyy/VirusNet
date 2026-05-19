import file_manager
import tool
import datetime
from faker import Faker
import os

def menu():
    print("=" * 50)
    print("                  VirusNet v1.0")
    print("                   Menu Utama")
    print("=" * 50)
    print("Pilih Menu: ")
    print("1. Simulasi baru")
    print("2. Pilih Save File")
    print("3. Konfigurasi Virus")
    print("0. Keluar Aplikasi")
    print("=" * 50)

while True:
    os.system("clear")
    menu()
    pilihan = tool.input_angka_tertentu(0,3, pesan_input=">> ")
    os.system("clear")
    print()
    match pilihan:
        case 1:
            file_manager.new_file()

        case 2:
            pass
        case 3:
            file_manager.konfigurasi_virus()
        case 0:
            print(f"\n\n Terima Kasih")
            break
    

