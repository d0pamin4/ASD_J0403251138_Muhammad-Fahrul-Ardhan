# ============================================================
# Nama: Muhammad Fahrul Ardhan
# NIM: J0403251138
# Kelas: TPL A1
# Praktikum 1 - Membuat Adjacency Matrix
# ============================================================

num_nodes = 4

# Inisialisasi matrix N×N dengan nilai 0
matrix = [[0] * num_nodes for _ in range(num_nodes)]

# Definisi edges berdasarkan diagram
edges = [(0,1), (0,2), (1,2), (2,3)]

# Set nilai 1 untuk setiap edge (dua arah)
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1  # undirected → simetris

# Tampilkan Matrix
print("    ", end="")
for i in range(num_nodes):
    print(f"  {i}", end="")
print()
print("    " + "---" * num_nodes)

for i, row in enumerate(matrix):
    print(f" {i} |", end="")
    for val in row:
        print(f"  {val}", end="")
    print()