#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:#Berhenti saat pengecekan sudah berada di indeks elemen paling akhir dari list.
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)#terus menggeser pengecekan ke elemen sebelah kanannya.

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
#Program bergerak mentok ke ujung kanan list. Saat mundur, ia membandingkan angka saat ini dengan nilai maksimum dari elemen-elemen di sisa kanannya.