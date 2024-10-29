# + Penambahan 20+6, hasil: 26
#- Pengurangan 20-6, hasil: 14
#* Perkalian 20*6, hasil: 120
#/ Pembagian (real/pecahan) 20/6, hasil: 3.3333
#// Pembagian (dibulatkan ke bawah) 20//6, hasil: 3
#% Modulus (sisa hasil bagi) 20%6, hasil:120
#** Pemangkatan 20**6, hasil: 64000000

a= 20
j= 40
hasil = a+j
print (hasil)

a=20
j=40
hasil =a-j
print (hasil)

a=20
j=40
hasil = a*j
print (hasil)

a=2
j=40
hasil =a/j
print(hasil)

a=20
j=40
hasil=a//j
print(hasil)

a=20
j=40
hasil=a%j
print(hasil)

a=20
j=40
hasil=a**j
print(hasil)

e = (5>6) and (8<=7)
print (e)
g = ('grexpofs'=='grexpofs') and (8<=7)
print (g)
e = not (1 < 1)
print (e)
g = ('grexpofs' == 'grexpofs') and (8<=7)or (8!=8)
print (g)

h=6
a=3

print('h berisi angka', h, 'desimal atau',bin(h), 'biner')
print('a berisi angka', a, 'desimal atau', bin(a), 'biner')

print('h & a:', h & a)  
print('h | a:', h | a) 
print('h ^ a:', h ^ a) 
print('~h:', ~h)       
print('h << 1:', h << 1) 
print('h >> 1:', h >> 1) 

i = 2
j = 4 
j = j + 1
k = i + j
l = k + k + i
m = (k+l)+ i
print ('isi variabel i:', i)
print ('isi variabel j:', j)
print ('isi variabel k:',k)
print('isi variabel l:',l)
print('isi variabel m:',m)

n = 20
n += 10
print ('n+= 5 :', n)
n = 20
n/= 10
print ('n /= 10:', n)
n = 20
n **=10
print('n *=10:', n)
n = 20
n <<= 2
print ('n<<=2:',n)

e= 6
f=6
g=7
print('e is f:', e is f)
print('e is g:', e is g)
print('e is not g:', e is not g)
print ('\n')

h= 'belajar python'
i= 'belajar python'
print('h is i:', h is i)
print('h is not i:', h is not i)
print('\n')

j = ['j', 'k', 'l']
k = ['j', 'k', 'l']

print('j is k:', j is k)  
print('j is not k:', j is not k)  

m = 'belajar python'
print('m:', m)
print('\'i\' in m:', 'i' in m)  
print('\'k\' not in m:', 'k' not in m)  
print('\'d\' not in m:', 'd' not in m)   

n = ['a', 'b', 'c']
print('n:', n)
print('\'a\' in n:', 'a' in n)  
print('\'a\' not in n:', 'a' not in n)  
print('\'d\' not in n:', 'd' not in n) 

o = (12, 43, 102, 55)
print('o:', o)
print('102 in o:', 102 in o)  
print('102 not in o:', 102 not in o) 
print('35 not in o:', 35 not in o)  
