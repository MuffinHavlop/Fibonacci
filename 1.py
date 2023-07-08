n = int(input('Enter the series of Fibonacci: '))
n1 = 0
n2 = 1
sum = 0

for i in range(n+1):
    print(sum, end=" ")
    n1 = n2
    n2 = sum
    sum = n1 + n2