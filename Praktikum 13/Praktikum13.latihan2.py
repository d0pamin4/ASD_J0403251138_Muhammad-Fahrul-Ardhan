# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 
# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 
# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 

connected = set() 
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        
        connected.add(u) 
        connected.add(v) 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight)

#PERTANYAAN ANALISIS

# 1. Edge mana yang dipilih pertama kali?
#Edge yang dipilih PERTAMA adalah C-D dengan bobot 1.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
"""dengan selalu memilih edge paling murah yang tersedia, kita menjamin 
bahwa setiap penambahan edge ke MST memberikan biaya tambahan minimum"""

#3. Berapa total bobot MST yang dihasilkan?
"""Total bobot MST = 1 (C-D) + 2 (A-C) + 3 (B-D) = 6 
Ini adalah total biaya minimum untuk menghubungkan semua 4 node tanpa membentuk cycle."""

# 4. Mengapa edge tertentu tidak dipilih?
"""Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena ketika
giliran mereka dievaluasi, KEDUA node di masing-masing edge sudah ada di dalam set 'connected'"""