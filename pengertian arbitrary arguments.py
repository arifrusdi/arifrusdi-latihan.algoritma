def sapa_teman(teman, temann, temannn):
  print("Halo",teman)
  print("Halo",temann)
  print("Halo",temannn)   
sapa_teman("iccang","fatir","sibli")

def sapa_idola(*args):
  print(args)
  print(type(args))   
sapa_idola("afgan","Devano","Riswan Njan")

def sapa_besti(*nama):
  for a in nama:
    print("Halo",a)  
sapa_besti("iccang","dani","sibli","fatir","mufli","fadil")

def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil 
print( jumlah(1,2) )
print( jumlah(3,4,5,6) )
print( jumlah(7,8,9,10,11,12,13,14) )

def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil / len(args) 
print( jumlah(1,2) )
print( jumlah(3,4,5,6) )
print( jumlah(7,8,9,10,11,12,13,14) )