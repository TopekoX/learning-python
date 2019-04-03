# yang perlu diperhatikan di dalam python 
# pastikan method dibuat terlebih dahulu kemudian baru dipanggil
# karena python eksekusi program dari atas ke bawah

nama = []

def print_nama():
    print("========================")
    for data in nama:
        print(data)

nama.append("ucup")
print_nama()

nama.append("timposu")
print_nama()

nama.append("azwar")
print_nama()