# program manajemen kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("================================")
        print(f"Nama {kontak['nama']}")
        print(f"Nama {kontak['email']}")
        print(f"Nama {kontak['telepon']}")

def new_kontak():
    nama = input("Nama :")
    email = input("Email :")
    telepon = input("Telepon :")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def del_kontak(daftar_kontak):
    nama = input("Masukan nama yang ingin dihapus : ")

    index = -1

    for i in range (0, len(daftar_kontak)):
        kontak = daftar_kontak[i]

        if nama.lower() == kontak["nama"].lower():
            index = i
            break
    
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del(daftar_kontak[i])
        print("Berhasil hapus data")

def find_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower.find(nama_yang_dicari.lower) != -1:
            print("================================")
            print(f"Nama {kontak['nama']}")
            print(f"Nama {kontak['email']}")
            print(f"Nama {kontak['telepon']}")