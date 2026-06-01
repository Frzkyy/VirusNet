import random


def next_day(kapal, virus):

    print("\n=== SIMULASI HARI BERIKUTNYA ===")

    daftar_terpapar = []

    # proses penyebaran
    for penumpang in kapal.penumpang:

        if penumpang.status == "terinfeksi":

            koneksi = kapal.jaringan.ambil_koneksi(
                penumpang.id
            )

            for target_id in koneksi:

                target = kapal.cari_penumpang(
                    target_id
                )

                if target.status == "rentan":

                    peluang = random.random()

                    if peluang <= virus.tingkat_penularan:

                        target.terpapar()

                        daftar_terpapar.append(
                            target.nama
                        )

    for penumpang in kapal.penumpang:

        penumpang.update_status(
            virus.masa_inkubasi
        )

    if daftar_terpapar:

        print("\nPenumpang terpapar hari ini:")

        for nama in daftar_terpapar:

            print("-", nama)

    else:

        print("\nTidak ada penularan baru")

    statistik = kapal.statistik()

    print("\n=== STATISTIK ===")

    for key, value in statistik.items():

        print(f"{key} : {value}")