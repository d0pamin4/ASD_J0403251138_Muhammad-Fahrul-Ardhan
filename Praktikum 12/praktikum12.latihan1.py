# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']    # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']    # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
    """Total bobot jalur A -> B -> D = graph['A']['B'] + graph['B']['D']
    = 4 + 5 = 9"""

# 2. Berapa total bobot jalur A -> C -> D?
    """Total bobot jalur A -> C -> D = graph['A']['C'] + graph['C']['D']
    = 2 + 1 = 3"""

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
    """Jalur A -> C -> D dipilih sebagai jalur terpendek karena bobotnya
    lebih kecil (3) dibandingkan jalur A -> B -> D (9).
    Kondisi jalur_1 < jalur_2 bernilai False (9 < 3 = False),
    sehingga blok else dijalankan."""

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
    """Karena jalur terpendek ditentukan dari TOTAL BOBOT (cost/weight),
    bukan dari jumlah edge. Setiap edge memiliki bobot yang berbeda-beda
    yang merepresentasikan jarak, waktu, atau biaya."""
