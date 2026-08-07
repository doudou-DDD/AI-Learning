n=int(input('Enter a number: '))
sum=0
i=1
while i<n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(f'The sum of all even numbers from 1 to {n} is {sum}.')