a = 5

try:
    a/0
except ZeroDivisionError:
    print("tidak dapat di bagi 0")
else:
    print("tidak ada ekpresi")
finally:
    print("Blok ekspresi selesai")