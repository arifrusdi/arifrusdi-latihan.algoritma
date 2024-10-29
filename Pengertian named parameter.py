def pangkat(angka, pangkat = 4):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil; 
print( pangkat(4) )      
print( pangkat(4,5) )    
print( pangkat(5,6) )    


def pangkat(angka, pangkat = 4):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
print( pangkat(angka = 1,pangkat = 2) )     
print( pangkat(pangkat = 3,angka = 4) )     


def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database("arif.rusdi","rifpotter","060801")