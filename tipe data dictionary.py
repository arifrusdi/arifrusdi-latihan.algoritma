# Cara membuat tipe data dictionary python
a = {1: "alita", 2: "azka", 3: "atifa"}
b = {"anak pertama": "alita", "kedua": "azka", "ketiga": "atifa"}
c = {1: "alita", "itu": "anak", "pertama": "om rama"}
print (type(a))
print (type(b))
print (type (c))
print (a)
print (b)
print (c)

my_self = {
    "sifat": "keras kepala",
    "nickname": ["arifkong", "rifpotter", "arip"],
    "username": "https.arif",
    "is_rifpotter": False,
    "panggilan": "arip",
    "masa_pendidikan": {
        "tk": "pindah terus",
        "sd": "SD 4",
        "smp": "SMP 1 corona vibes",
        "sma": "SMA 1 sndana"
    }
}

print(my_self)

s = { "mau balik kemana": "masa sma",
"kenapa": "karena indah",
"apanya": "masanya" }
print (s["mau balik kemana"])


y = {"yg psti2 aja": "hubungannya",
"gamon": "boleh",
"patah hati": "jangan"}
y["yg psti2 aja"] = "harus dong!"
print(y)

g = {"me": "arif",
"umur": "18 tahun",
"calon anak sukses": "ya harus"}
g["target"] = True
print(g)

h = {"me":"arif",
"umur":"18 tahun",
"calon anak sukses": "ya harus"}
del h["umur"]
print(g)

i = dict (pendidikan ="sekolah",
smp = "corona vibes",
sma = " is the best" )
print(i)
