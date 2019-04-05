# belajar module
# import function.py secara global
# import function2.py secara spesifik

import function1 # import module umum
from function2 import hitung_luas #import module secara spesifik

function1.say_hello("Ucup")

hasil = function1.total(1,2,3,4,5)
print(hasil)

luas = hitung_luas(10, 5) # cukup nama methodnya
print(luas)