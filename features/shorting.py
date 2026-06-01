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