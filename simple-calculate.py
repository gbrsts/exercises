# In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, 
# the code of a product 2, the number of units of product 2 and the price for one unit of product 2. 
# After this, calculate and show the amount to be paid.

a,b,c = input().split(" ")
d,e,f = input().split(" ")

a = int(a)
b = int(b)
c = float(c)

d = int(d)
e = int(e)
f = float(f)

piece_1 = (b * c)
piece_2 = (e * f)

total = piece_1 + piece_2

print(f"VALOR A PAGAR = {total}")