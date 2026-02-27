#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0:#kondisi berhenti agar program tidak berjalan terus-menerus
        return 1
    # Recursive case
    return a * pangkat(a, n - 1) #Fungsi memanggil dirinya sendiri, tetapi nilai n dikurangi 1 pada setiap panggilannya untuk secara bertahap menuju base case.

print(pangkat(2, 4)) # Output: 16
#Jika memanggil pangkat(2, 4), program akan melakukan penumpukan (stacking): 2 * pangkat(2, 3), lalu pangkat(2, 3) menjadi 2 * pangkat(2, 2), dan seterusnya hingga pangkat(2, 0). Setelah pangkat(2, 0) mereturn 1 (base case tercapai), hasil tersebut dikembalikan ke atas (unwinding)