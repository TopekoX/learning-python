# tipe data dictionary
# sama seperti list hanya bukan index tapi key

customer = {"nama":"Ucup Timposu", "usia":30}

nama = customer["nama"] # cara aksesnya
usia = customer["usia"]

# cara extrat 1
for key in customer:
    value = customer[key]
    print(f"{key} : {value}")

# menambah data
customer["alamat"] = "Palu"
customer["skill"] = "Java, Python"  

# mengubah data
customer["nama"] = "Sugandi"

# cara melihat data secara langsung
print(customer.items())

# menghapus data
del customer["skill"]

# cara extrart 2
for key, value in customer.items():
    print(f"{key} = {value}")