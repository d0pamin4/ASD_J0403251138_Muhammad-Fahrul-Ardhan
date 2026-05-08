# ============================================================
# Nama: Muhammad Fahrul Ardhan
# NIM: J0403251138
# Kelas: TPL A1
# 
# Praktikum 2 — Adjacency List
# Graph: 4 node (A,B,C,D), undirected
# ============================================================

# Inisialisasi dictionary dengan list kosong per node
graph = {node: [] for node in ['A', 'B', 'C', 'D']}

# Definisi edges berdasarkan diagram
edges = [('A','B'), ('A','C'), ('B','D'), ('C','D')]

# Isi adjacency list (undirected → dua arah)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Urutkan tetangga agar tampilan konsisten
for node in graph:
    graph[node].sort()

# ── Tampilkan Adjacency List ──────────────────
print("ADJACENCY LIST")
print("─" * 25)
for node, neighbors in graph.items():
    n_str = " → ".join(neighbors) if neighbors else "(tidak ada)"
    print(f"  {node}  :  {n_str}")