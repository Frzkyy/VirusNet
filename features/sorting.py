# =========================
# SORTING
# =========================


def bubble_sort_desc(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# Urutkan penumpang berdasarkan hari_terinfeksi descending
# Dipakai untuk menentukan prioritas evakuasi (paling lama terinfeksi = prioritas tertinggi)
def bubble_sort_evakuasi(data_penumpang):
    data = data_penumpang[:]
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j].hari_terinfeksi < data[j + 1].hari_terinfeksi:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# =========================
# SEARCHING
# =========================


def cari_penumpang_berdasarkan_nama(data_penumpang, nama):
    hasil = []

    for penumpang in data_penumpang:
        if nama.lower() in penumpang["nama"].lower():
            hasil.append(penumpang)

    return hasil


def cari_penumpang_berdasarkan_status(data_penumpang, status):
    hasil = []

    for penumpang in data_penumpang:
        if penumpang["status"].lower() == status.lower():
            hasil.append(penumpang)

    return hasil


# Cari penumpang berdasarkan ID (exact match)
# Menerima list object Person, return object Person atau None
def cari_penumpang_berdasarkan_id(data_penumpang, id_penumpang):
    for penumpang in data_penumpang:
        if penumpang.id == id_penumpang:
            return penumpang

    return None


# Cari semua penumpang di deck dan/atau ruangan tertentu
# ruangan bersifat opsional — kalau tidak diisi, cari semua di deck tersebut
def cari_penumpang_berdasarkan_lokasi(data_penumpang, deck, ruangan=None):
    hasil = []

    for penumpang in data_penumpang:
        if penumpang.lokasi.deck == deck:
            if ruangan is None or penumpang.lokasi.ruangan == ruangan:
                hasil.append(penumpang)

    return hasil