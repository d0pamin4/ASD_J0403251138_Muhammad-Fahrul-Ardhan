# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

#Definisi Graph Awal (semua edge yang ada)
# Graph awal menyimpan SEMUA edge termasuk yang membentuk cycle
edges_graph = [
    ('A', 'B'),   # sisi atas
    ('A', 'C'),   # sisi kiri
    ('A', 'D'),   # diagonal A ke D
    ('C', 'D'),   # sisi bawah
    ('B', 'D'),   # sisi kanan
]

# Kumpulkan semua node unik dari daftar edge
nodes_graph = set()
for u, v in edges_graph:
    nodes_graph.add(u)
    nodes_graph.add(v)
 
print("=" * 55)
print("GRAPH AWAL")
print("=" * 55)
print(f"Node  : {sorted(nodes_graph)}")
print(f"Jumlah node  : {len(nodes_graph)}")
print(f"Jumlah edge  : {len(edges_graph)}")
print("\nDaftar edge pada graph:")
for edge in edges_graph:
    print(f"  {edge[0]} --- {edge[1]}")

#Definisi Spanning Tree yang Valid
spanning_tree = [
    ('A', 'C'),   # edge 1: menghubungkan A dan C
    ('C', 'D'),   # edge 2: menghubungkan C dan D
    ('D', 'B'),   # edge 3: menghubungkan D dan B
]

# Kumpulkan semua node yang terlibat dalam spanning tree
nodes_st = set()
for u, v in spanning_tree:
    nodes_st.add(u)
    nodes_st.add(v)
 
print("\n" + "=" * 55)
print("SPANNING TREE (Contoh yang Valid)")
print("=" * 55)
print(f"Node yang terhubung : {sorted(nodes_st)}")
print(f"Jumlah edge         : {len(spanning_tree)}")
print("\nDaftar edge pada spanning tree:")
for edge in spanning_tree:
    print(f"  {edge[0]} --- {edge[1]}")

#Perbandingan Graph Awal vs Spanning Tree
print("\n" + "=" * 55)
print("PERBANDINGAN")
print("=" * 55)
print(f"  {'Aspek':<30} {'Graph Awal':>10} {'Spanning Tree':>15}")
print("  " + "-" * 55)
print(f"  {'Jumlah node':<30} {len(nodes_graph):>10} {len(nodes_st):>15}")
print(f"  {'Jumlah edge':<30} {len(edges_graph):>10} {len(spanning_tree):>15}")
print(f"  {'Mengandung cycle':<30} {'Ya':>10} {'Tidak':>15}")
print(f"  {'Semua node terhubung':<30} {'Ya':>10} {'Ya':>15}")
 
# Verifikasi rumus: edge spanning tree = node - 1
jumlah_node = len(nodes_graph)
expected_st_edges = jumlah_node - 1
print(f"\n  Verifikasi rumus (edge = node - 1):")
print(f"  Jumlah node          : {jumlah_node}")
print(f"  Edge spanning tree   : {len(spanning_tree)}")
print(f"  Ekspektasi (n-1)     : {expected_st_edges}")
print(f"  Valid                : {len(spanning_tree) == expected_st_edges}")

# JAWABAN ANALISIS
# 1. Apa perbedaan graph awal dan spanning tree?
"""Graph awal  : 5 edge, mengandung cycle, lebih banyak jalur
- Spanning tree: 3 edge, tanpa cycle, koneksi minimal"""

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
"""-Struktur "tree" (pohon) secara matematis tidak boleh memiliki cycle. 
-Menyimpan edge A-D berarti membuang biaya/sumber daya tanpa manfaat.
-edge yang membentuk cycle berarti kita membangun koneksi tambahan yang tidak menambah keterhubungan jaringan murni pemborosan biaya."""

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
"""Sebuah tree dengan N node SELALU memiliki tepat N-1 edge.
Jika ada lebih dari N-1 edge, PASTI ada cycle (terbukti secara matematis).
Itulah kenapa spanning tree selalu memiliki lebih sedikit edge dari
graph asal, kecuali graph asal sendiri sudah berbentuk tree."""