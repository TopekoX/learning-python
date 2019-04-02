# list => []
# tuple => ()
# set => {}
# perbedaannya data dalam set harus unik
# dan tidak bisa menggunakan indeks
# dan tidak ada operasi ubah data yang ada tambah dan hapus

nama = {"ucup", "azwar", "ikhwal"}

for data in nama:
    print(data)

# menambah data
nama.add("gandi")

print(nama)

# menghapus data
nama.remove("ucup")
nama.remove("ikhwal")

print(nama)