from datetime import date
from optparse import Values

aList = ["John", 33,"Toronto", True]
print(aList)

today = date.today()
mahasiswa = ["Bonfillo",2021071024,"Informatika","Universitas Pembangunan Jaya"]
print(mahasiswa, today)

bin_colors = ['red','green','yellow','blue']
print(bin_colors[1])

print(mahasiswa[1])

print(mahasiswa[3])

print(bin_colors[0:2])

print(mahasiswa[1:4])

for i, aColor in enumerate(bin_colors):
    print(i, aColor, " Square")

for i, siMahasiswa in enumerate(mahasiswa):
    print("UPJ ", siMahasiswa)
    
bin_colors=('Red','Green','Blue','Yellow')
print(bin_colors[1])
print(bin_colors[2:])

upj=('Universitas','Pembangunan','Jaya')
print(upj)


Pertama = (100)
Kedua = (200, 400, 600)
Ketiga = (300)
Keempat = (400, 800)

coba_nested = ((Pertama, ) + (Kedua, ) + (Ketiga, ) + (Keempat, ))
print(str(coba_nested))

ban_colors ={"manual_color": "Yellow", "approved_color": "Green", "refused_color": "Red"}
print(ban_colors)

print(ban_colors.get('approved_color'))
print(ban_colors['approved_color'])

ban_colors['approved_color']="lavender"
print(ban_colors)

latMahasiswa ={"NAMA": "Bonfillo", "NIM": 202107102, "PRODI": "Informatika", "UNIVERSITAS": "Universitas Pembangunan Jaya"}
print(latMahasiswa.values())

thisset = {"apple", "banana", "cherry"}
print(thisset)

import pandas as pd

data = {
    "ID": [1,2,3],
    "NAME": ["fares", "elena", "steven"],
    "AGE": [50, 40, 45],
    "DECISION":[True, True, True]
}

df = pd.DataFrame(data)

print(df)