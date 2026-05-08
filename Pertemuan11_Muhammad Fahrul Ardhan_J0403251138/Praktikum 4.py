# ============================================================
# Nama: Muhammad Fahrul Ardhan
# NIM: J0403251138
# Kelas: TPL A1
# 
# Praktikum 4 — Studi Kasus Peta Kota Malaysia
# Node      : Kuala Lumpur, Ipoh, Penang, Melaka, Johor Bahru
# Edge      : 6 lebuhraya penghubung antar kota (undirected)
# ============================================================

# ── Daftar node dan edge ──────────────────────────────────
nodes = ["Kuala Lumpur", "Ipoh", "Penang", "Melaka", "Johor Bahru"]

edges = [
    ("Kuala Lumpur", "Ipoh"),        # Lebuhraya PLUS E1  (~205 km)
    ("Kuala Lumpur", "Melaka"),      # Lebuhraya PLUS E2  (~144 km)
    ("Kuala Lumpur", "Johor Bahru"), # Lebuhraya PLUS E2  (~330 km)
    ("Ipoh",         "Penang"),       # Lebuhraya PLUS E1  (~161 km)
    ("Melaka",       "Johor Bahru"), # Lebuhraya PLUS E2  (~213 km)
    ("Penang",       "Melaka"),      # Lebuhraya PLUS E1+E2 (~365 km)
]

# ADJACENCY LIST  —  menggunakan dictionary Python
adj_list = {node: [] for node in nodes}

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)   # undirected → dua arah

# ADJACENCY MATRIX  —  menggunakan list 2D
n      = len(nodes)
index  = {node: i for i, node in enumerate(nodes)}
matrix = [[0] * n for _ in range(n)]

for u, v in edges:
    i, j           = index[u], index[v]
    matrix[i][j] = 1
    matrix[j][i] = 1   # simetris (undirected)

# ══════════════════════════════════════════════════════════
# OUTPUT 1 — Nama Node
# ══════════════════════════════════════════════════════════
print("=" * 50)
print("  DAFTAR NODE (KOTA DI MALAYSIA)")
print("=" * 50)
for i, node in enumerate(nodes):
    print(f"  [{i}] {node}")

# ══════════════════════════════════════════════════════════
# OUTPUT 2 — Adjacency List
# ══════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("  ADJACENCY LIST")
print("=" * 50)
for kota, tetangga in adj_list.items():
    print(f"  {kota:15} → {', '.join(tetangga)}")

# ══════════════════════════════════════════════════════════
# OUTPUT 3 — Adjacency Matrix
# ══════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("  ADJACENCY MATRIX")
print("=" * 50)
abbr = {"Kuala Lumpur":"KL", "Ipoh":"Ipoh",
        "Penang":"PNG", "Melaka":"MLK", "Johor Bahru":"JB"}
labels = [abbr[n] for n in nodes]
print(f"  {'':15}" + "".join([f"{lb:>6}" for lb in labels]))
print("  " + "-" * 46)
for i, row in enumerate(matrix):
    row_str = "".join([f"{v:>6}" for v in row])
    print(f"  {nodes[i]:15}{row_str}")

# ══════════════════════════════════════════════════════════
# OUTPUT 4 — Hubungan Antar Node
# ══════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("  HUBUNGAN ANTAR NODE")
print("=" * 50)
for u, v in edges:
    print(f"  {u:15} ── {v}")