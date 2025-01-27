n = int(input("Enter a number:"))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)




# using function
def calc_fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)  
(calc_fac(6))