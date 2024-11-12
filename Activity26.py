#Write a program to calculate the sum of whole numbers.

num = int(input('Enter the folowing numbers you want the sum of'))
sum = 0


for a in range(1,num+1):
    sum=sum+a
    print("\n Sum", sum)
