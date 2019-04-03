# return 1 nilai
def jumlahkan(*list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka
        return total     

total = jumlahkan(10, 10, 10)
print(total)

# return multi value
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
        return (total, list_angka)

total, list_angka = jumlahkan(10, 10, 10)
print(f"Total {list_angka} = {total}")