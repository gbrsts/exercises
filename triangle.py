a,b,c = map(float, input().split(" "))

perimeter = (a + b + c)
area = (((a +  b) * c) / 2)

if (a < (b + c)) and (b < (a + c)) and (c < (b + a)):
  print(f"Perimetro: {perimeter}")
else:
  print(f"Área: {area}")