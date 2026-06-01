# VirusNet
```
Versi: v.1.0
```

## Cara Menginstall Aplikasi
```cmd
git clone https://github.com/Frzkyy/VirusNet.git
cd VirusNet

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py
```
---
## Catatan Kontributor

Cara push ke github

### Ketrin

Sebelum mengedit:
```cmd
git pull origin main
git checkout branch-ketrin
```

Setelah selesai edit file:
```cmd
git add .
git commit -m "pesan commit"
git push origin branch-ketrin
```

### Cika

Sebelum mengedit:
```cmd
git pull origin main
git checkout branch-cika
```

Setelah selesai edit file:
```cmd
git add .
git commit -m "pesan commit"
git push origin branch-cika
```

### Kalau Ada Error
Error:
```
error: pathspec 'nama branch' did not match any file(s) known to git
```
Cara fix:
```
git checkout -b "nama branch"
```
