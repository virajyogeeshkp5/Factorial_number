# Write a program to display the factorial of given number
n=int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f=f*i
    print("factorial is: ",f)
