#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Studi Kasus: Generator PIN
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)     
buat_pin(3)
#dengan mengecek apakah angka tersebut sudah ada di dalam variabel penyimpan.