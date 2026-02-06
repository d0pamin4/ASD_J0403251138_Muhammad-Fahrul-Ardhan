# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 1: membuat fungsi load data
# ------------------------------------------

# VARIABEL MENYIMPAN DATA FILE
nama_file = "data_mahasiswa.txt"


def baca_data(nama_file):
    data_dict = {}  # inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(',')
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
    return data_dict


buka_data = baca_data(nama_file)
print("jumlah data terbaca", len(buka_data))


# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 2: membuat fungsi load data
# ------------------------------------------

def tampilkan_data(data_dict):
    # membuat header tabel
    print("\n======DAFTAR MAHASISWA=======")
    print(f"{'NIM': <10} | {'NAMA': <12} | {'NILAI': >1}")
    print("-"*35)  # membuka garis

    # menampilkan isi data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {int(nilai): >1}")

# tampilkan_data(buka_data)#memanggil fungsi untuk menampilkan data

# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 3: membuat fungsi mencari data
# ------------------------------------------


def cari_data(data_dict):
    # pencarian data berdasarkann nim sebagai key dictionary
    # membuat input nim mahasiswa yang akan dicari
    nim_cari = input("masukkan NIM Mahasiswa yang dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\nData Mahasiswa Ditemukan:")
        print(f"NIM  : {nim_cari}")
        print(f"NAMA : {nama}")
        print(f"NILAI: {nilai}")
    else:
        print("\nData Mahasiswa Tidak Ditemukan.")

# cari_data(buka_data) #memanggil fungsi untuk mencari data

# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 4: membuat fungsi update data
# ------------------------------------------


def update_data(data_dict):
    # awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("masukkan nim mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan.")
        return
    try:
        nilai_baru = int(input("masukkan nilai baru 0-100 :").strip())
    except ValueError:
        print("Nilai harus berupa angka antara 0-100.")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100.")
        return

    nilai_lama = data_dict[nim]["nilai"]

    data_dict[nim]["nilai"] = nilai_baru
    print(
        f"update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

# memanggil fungsi ubah data
# update_data(buka_data)

# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 5: membuat fungsi menyimpat data pada file
# ------------------------------------------

# membuat fungsi menyimpat data ke file


def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data(nama_file, buka_data) #memanggil fungsi simpan data
print("data berhasil disimpan ke file : ", nama_file)


# ------------------------------------------
# Praktikum 2: konsep adt dan file handling
# Latihan 6: membuat menu interaktif
# ------------------------------------------

def main():
    buka_data = baca_data(nama_file)
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan ke file:", nama_file)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
