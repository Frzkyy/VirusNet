class Virus:
    def __init__(self, nama, tingkat_penularan, masa_inkubasi, mortalitas):
        self.nama = nama
        self.tingkat_penularan = tingkat_penularan
        self.masa_inkubasi = masa_inkubasi
        self.mortalitas = mortalitas

    def info(self):
        return {
            "nama": self.nama,
            "tingkat_penularan": self.tingkat_penularan,
            "masa_inkubasi": self.masa_inkubasi,
            "mortalitas": self.mortalitas
        }

    def tampilkan_info(self):
        print(f"Nama Virus          : {self.nama}")
        print(f"Tingkat Penularan   : {self.tingkat_penularan}")
        print(f"Masa Inkubasi       : {self.masa_inkubasi} hari")
        print(f"Mortalitas          : {self.mortalitas}")