class HashTable:

    def __init__(self, kapasitas=100):
        self.kapasitas = kapasitas
        self.tabel = [[] for _ in range(kapasitas)]
        self.jumlah_data = 0

    # Hash function — konversi ID ke index bucket
    def _hash(self, key):
        return key % self.kapasitas

    # Tambah atau update data penumpang
    def set(self, id_penumpang, penumpang):
        index = self._hash(id_penumpang)
        bucket = self.tabel[index]

        for i, (k, v) in enumerate(bucket):
            if k == id_penumpang:
                bucket[i] = (id_penumpang, penumpang)
                return

        bucket.append((id_penumpang, penumpang))
        self.jumlah_data += 1

    # Ambil data penumpang berdasarkan ID — O(1) rata-rata
    def get(self, id_penumpang):
        index = self._hash(id_penumpang)
        bucket = self.tabel[index]

        for k, v in bucket:
            if k == id_penumpang:
                return v

        return None

    # Hapus data penumpang berdasarkan ID
    def delete(self, id_penumpang):
        index = self._hash(id_penumpang)
        bucket = self.tabel[index]

        for i, (k, v) in enumerate(bucket):
            if k == id_penumpang:
                bucket.pop(i)
                self.jumlah_data -= 1
                return True

        return False

    # Cek apakah ID ada di tabel
    def ada(self, id_penumpang):
        return self.get(id_penumpang) is not None

    # Ambil semua penumpang sebagai list
    def semua(self):
        hasil = []
        for bucket in self.tabel:
            for k, v in bucket:
                hasil.append(v)
        return hasil

    def ukuran(self):
        return self.jumlah_data

    def tampilkan(self):
        print(f"HashTable ({self.jumlah_data} penumpang, kapasitas {self.kapasitas})")
        for i, bucket in enumerate(self.tabel):
            if bucket:
                for k, v in bucket:
                    print(f"  [{i}] ID={k} -> {v}")