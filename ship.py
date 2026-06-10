import random

from classes.person import Person
from classes.location import Location
from structures.graph import Graph
from structures.hash_table import HashTable


class Ship:

    def __init__(self, nama_kapal, jumlah_deck, jumlah_penumpang):

        self.nama_kapal = nama_kapal
        self.jumlah_deck = jumlah_deck
        self.jumlah_penumpang = jumlah_penumpang

        self.penumpang = []
        self.db = HashTable(kapasitas=jumlah_penumpang * 2)

        self.jaringan = Graph()
        self.deck_terkunci = set()

    # generate seluruh penumpang
    # daftar_nama: list nama dari luar (misal dari Faker di file_manager)
    # kalau tidak dikirim, fallback ke nama default
    def generate_penumpang(self, daftar_nama=None):

        for i in range(1, self.jumlah_penumpang + 1):

            deck = random.randint(1, self.jumlah_deck)
            ruangan = random.randint(1, 10)
            lokasi = Location(deck, ruangan)

            if daftar_nama and i <= len(daftar_nama):
                nama = daftar_nama[i - 1]
            else:
                nama = f"Penumpang_{i}"

            orang = Person(
                i,
                nama,
                random.randint(18, 60),
                "rentan",
                lokasi
            )

            self.penumpang.append(orang)
            self.db.set(orang.id, orang)
            self.jaringan.tambah_penumpang(orang.id)

        self.generate_koneksi()


    # cari penumpang berdasarkan id — O(1) via HashTable
    def cari_penumpang(self, id_penumpang):
        return self.db.get(id_penumpang)

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
    
    def generate_koneksi(self):

        for p1 in self.penumpang:
            if p1.lokasi.deck in self.deck_terkunci:
                continue

            for p2 in self.penumpang:
                if p2.lokasi.deck in self.deck_terkunci:
                    continue
                if p1.id != p2.id:
                    lokasi_sama = (
                        p1.lokasi.deck == p2.lokasi.deck
                        and
                        p1.lokasi.ruangan == p2.lokasi.ruangan
                    )

                    if lokasi_sama:
                        self.jaringan.tambah_koneksi(p1.id, p2.id)