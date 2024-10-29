def sambung_kata(**kata):
  for i in kata:
     print(i) 
sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat")

def sambung_kata(**kata):
  for i in kata.values():
     print(i) 
sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat")


def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i + " "
  return hasil;
print( sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat") )

def test(var1, var2, *args,**kwargs):
  print(var1)
  print(var2)
  print(args)
  print(kwargs)
test(10, 20, 30, 40, 50, a = 60, b = 70, c = 80)
