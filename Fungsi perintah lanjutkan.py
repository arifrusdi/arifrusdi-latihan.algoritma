for a in range(1,14):
  print(a,' x ',a ,' = ',a*a)

for b in range(1,14):
  if b == 4:
    continue
  print(b,' x ',b ,' = ',b*b)

c = 0
while c < 20:
  c += 1
  if c == 7:
    continue
  print(c,' x ',c ,' = ',c*c)