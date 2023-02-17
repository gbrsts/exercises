#Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

a,b,c,d = map(int, input().split(" "))

diference = ((a * b) - (c * d))

print(f"DIFERENCA = {diference}")