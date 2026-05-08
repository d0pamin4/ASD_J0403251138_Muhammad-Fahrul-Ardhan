# ============================================================
# Nama: Muhammad Fahrul Ardhan
# NIM: J0403251138
# Kelas: TPL A1
# 
# Praktikum 3 — Konversi Adjacency Matrix ke List
# ============================================================

def matrix_to_adjacency_list(matrix):
    """
    Mengkonversi adjacency matrix menjadi adjacency list.

    Parameter:
        matrix (list[list[int]]): Matriks N×N berisi 0 atau 1

    Returns:
        dict[int, list[int]]: Adjacency list {node: [tetangga]}

    Kompleksitas:
        Waktu  : O(N²) — iterasi semua elemen matrix
        Memori : O(N + E) — N node + E edges
    """
    n = len(matrix)
    adj_list = {}

    for i in range(n):
        adj_list[i] = []
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i].append(j)

    return adj_list


# ── Input Matrix ──────────────────────────────
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# ── Eksekusi Konversi ─────────────────────────
result = matrix_to_adjacency_list(matrix)

# ── Tampilkan Hasil ───────────────────────────
print("ADJACENCY LIST (hasil konversi)")
print("─" * 30)
for node, neighbors in result.items():
    print(f"  Node {node}  →  {neighbors}")