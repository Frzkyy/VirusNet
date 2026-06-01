class Graph:

    def __init__(self):
        self.jaringan = {}

    def tambah_penumpang(self, id_penumpang):

        if id_penumpang not in self.jaringan:
            self.jaringan[id_penumpang] = []

    def tambah_koneksi(self, p1, p2):

        if p2 not in self.jaringan[p1]:
            self.jaringan[p1].append(p2)

        if p1 not in self.jaringan[p2]:
            self.jaringan[p2].append(p1)

    def ambil_koneksi(self, id_penumpang):

        return self.jaringan.get(id_penumpang, [])

    def lockdown_deck(self, daftar_penumpang, deck):

        for penumpang in daftar_penumpang:

            if penumpang.lokasi.deck == deck:

                self.jaringan[penumpang.id] = []

    def tampilkan_graph(self):

        for node in self.jaringan:

            print(node, "->", self.jaringan[node])