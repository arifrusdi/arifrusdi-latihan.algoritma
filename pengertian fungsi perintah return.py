def plus(var1, var2):
  return var1 + var2
print(plus(3,5))
print(plus(3,6))

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(4) )      
print( pangkat(5) )      
print( pangkat(6) )     
print( pangkat(7,7) )    
print( pangkat(8,8) )    
print( pangkat(9,9) )    