# Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. 
# This is a very simple program with the only intention of practice of selection commands.
#
#   ID        Specification         Price
#   1        Cachorro Quente       R$ 4.00
#   2           X-Salada           R$ 4.50  
#   3           X-Bacon            R$ 5.00
#   4        Torrada Simples       R$ 2.00
#   5          Refrigerante        R$ 1.50


cod,quant = map(int, input().split(" "))

if cod == 1:
  price = 4.00
  total = price * quant
  print(f"Total = R$ {total:.2f}")
elif cod == 2:
  price = 4.50
  total = price * quant
  print(f"Total = R$ {total:.2f}")
elif cod == 3:
  price = 5.00
  total = price * quant
  print(f"Total = R$ {total:.2f}")
elif cod == 4:
  price = 2.00
  total = price * quant
  print(f"Total = R$ {total:.2f}")
else: 
  price = 1.50
  total = price * quant
  print(f"Total = R$ {total:.2f}")