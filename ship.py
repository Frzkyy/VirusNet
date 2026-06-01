import random

from classes.person import Person
from classes.location import Location
from structures.graph import Graph


class Ship:

    def __init__(self, nama_kapal, jumlah_deck, jumlah_penumpang):

        self.nama_kapal = nama_kapal
        self.jumlah_deck = jumlah_deck
        self.jumlah_penumpang = jumlah_penumpang

        self.penumpang = []

        self.jaringan = Graph()

    # generate seluruh penumpang
    def generate_penumpang(self):

        for i in range(1, self.jumlah_penumpang + 1):

            deck = random.randint(1, self.jumlah_deck)

            ruangan = random.randint(1, 10)

            lokasi = Location(deck, ruangan)

            orang = Person(
                i,
                f"Penumpang_{i}",
                random.randint(18, 60),
                "rentan",
                lokasi
            )

            self.penumpang.append(orang)

            self.jaringan.tambah_penumpang(
                orang.id
            )

        self.generate_koneksi()

    # generate koneksi antar penumpang
    def generate_koneksi(self):

        for p1 in self.penumpang:

            for p2 in self.penumpang:

                if p1.id != p2.id:

                    lokasi_sama = (
                        p1.lokasi.deck == p2.lokasi.deck
                        and
                        p1.lokasi.ruangan == p2.lokasi.ruangan
                    )

                    if lokasi_sama:

                        self.jaringan.tambah_koneksi(
                            p1.id,
                            p2.id
                        )

    # cari penumpang berdasarkan id
    def cari_penumpang(self, id_penumpang):

        for penumpang in self.penumpang:

            if penumpang.id == id_penumpang:
                return penumpang

        return None

    # tampil semua penumpang
    def tampilkan_penumpang(self):

        for penumpang in self.penumpang:

            print(penumpang)

    # statistik status
    def statistik(self):

        data = {
            "rentan": 0,
            "terpapar": 0,
            "terinfeksi": 0,
            "sembuh": 0,
            "meninggal": 0
        }

        for penumpang in self.penumpang:

            data[penumpang.status] += 1

        return data