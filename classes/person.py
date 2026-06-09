import random

class Person:
    def __init__(self,id,nama,umur,status,lokasi):
        self.id = id
        self.nama = nama
        self.umur = umur
        self.status = status
        self.lokasi = lokasi

        self.hari_terpapar = 0
        self.hari_terinfeksi = 0

    def terpapar(self):
        if self.status == "rentan":
            self.status = "terpapar"

    def update_status(self, masa_inkubasi):
        if self.status == "terpapar":
            self.hari_terpapar += 1
            if self.hari_terpapar >= masa_inkubasi:
                self.status = "terinfeksi"

    def sembuh(self):
        self.status = "sembuh"

    def meninggal(self):
        self.status = "meninggal"

    def pindah_lokasi(self, lokasi_baru):
        self.lokasi = lokasi_baru

    def tampilkan_info(self):

        print("ID       :", self.id)
        print("Nama     :", self.nama)
        print("Umur     :", self.umur)
        print("Status   :", self.status)
        print("Lokasi   :", self.lokasi)

    def update_status(self, masa_inkubasi, mortalitas):
        if self.status == "terpapar":
            self.hari_terpapar += 1
            if self.hari_terpapar >= masa_inkubasi:
                self.status = "terinfeksi"
        elif self.status == "terinfeksi":
            self.hari_terinfeksi += 1
            if random.random() <= mortalitas:
                self.meninggal()
            elif self.hari_terinfeksi >= 5:
                self.sembuh()

    def __str__(self):

        return (
            f"{self.nama} | "
            f"{self.status} | "
            f"{self.lokasi}"
        )