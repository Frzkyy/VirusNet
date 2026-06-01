class Location:

    def __init__(self, deck, ruangan):
        self.deck = deck
        self.ruangan = ruangan

    def tampilkan_lokasi(self):
        print(f"Deck {self.deck} - Ruangan {self.ruangan}")

    def __str__(self):
        return f"Deck {self.deck} - Ruangan {self.ruangan}"