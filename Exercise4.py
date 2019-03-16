n = int(input("Enter the number: "))
divsrs = [1]
for i in range(2,(int(n/2 +1))):
    if n%i == 0:
        divsrs.append(i)
divsrs.append(n)
print("The list of divisors for " + str(n) + " is " + str(divsrs))
