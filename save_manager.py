import json
from classes.virus import Virus
import os

def load_file(file):
    try:
        with open(f"data/save/{file}","r") as f:
            return json.load(f)
    except:
        return None

def load_virus(file):
    try:
        with open(f"data/virus/{file}","r") as f:
            return json.load(f)
    except:
        return None
    
def select_virus():
    virus_list = os.listdir("data/virus")
    num = 1
    for i in virus_list:
        virus = load_virus(i)
        print(f"{num}. {virus["nama"]} | Tingkat Penularan: {virus["tingkat_penularan"] * 100}% | Masa Inkubasi: {virus["masa_inkubasi"]} Hari | Mortalitas: {virus["mortalitas"] * 100}%")
    print("0. Buat virus baru")


def new_file():
    template = {
    "nama_kapal": None,
    "hari": None,
    "virus": {
        "nama":None,
        "tingkat_penularan":None,
        "masa_inkubasi":None,
        "mortalitas":None
    },
    "penumpang": [],
    "statistik": {
        "rentan": None,
        "terpapar": None,
        "terinfeksi": None,
        "sembuh": None,
        "meninggal": None
    },
    "log_harian": []
}
    return template