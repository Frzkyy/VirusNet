def input_angka(pesan_eror="[Error] Masukan Hanya Angka",pesan_input=None, tipe="int"):
    while True:
        try:
            if tipe == "int":
                if pesan_input:
                    temp = int(input(pesan_input))
                else:
                    temp = int(input())
            elif tipe == "float":
                if pesan_input:
                    temp = float(input(pesan_input))
                else:
                    temp = float(input())
            else:
                return None
            return temp
        except ValueError:
            if pesan_eror:
                print(pesan_eror)

def input_angka_tertentu(batas_bawah, batas_atas ,pesan_eror="[Error] Masukan Hanya Angka",pesan_input=None, pesan_rentang="[Error] Angka Tidak Tersedia", tipe="int"):
    while True:
        pilihan = input_angka(pesan_input=pesan_input, pesan_eror=pesan_eror, tipe=tipe)
        if pilihan >= batas_bawah and pilihan <= batas_atas:
            return pilihan
        else:
            print(pesan_rentang)