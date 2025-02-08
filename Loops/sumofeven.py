# Question:
# Write a Python Program to find the sum of all even numbers between 1 to 20
# using a for loop.

sum = 0

for num in range(1,21):
    if num%2==0 :
        sum += num
print("Sum of even numbers are ", sum)


# Write a PP to count the number of vowels in a given string.

str = input("Please Provide the String")
count = 0

for ch in str:
    # Check if ch is a vowel or not
    if ch.lower() in ['a','e','i','o','u']:
        count += 1
print('Total count of vowel is ', count)


# Write a PP to check if a number is prime or not
num = int(input("Enter the num "))

isPrime = True
if(num <= 1):
    isPrime = False

for  i in range(2,int(num/2)+1):
    if num%i == 0:
        isPrime = False
        break
print("Number Passed is : ",isPrime)


# Write a Python program to print the multiplication table of a given number
# num = int(input("Enter the number to  generate the Mu"))
# for i in range(1,11):
#     print(num,"*",i,"=" num)

for row in range(5):
    for j in range(row+1):
        print("*",end="")
    print()
