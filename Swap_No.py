#Swapping of 2 no's using temp variable

x = 15
y = 20

temp = x
x = y
y = temp

print("The value of x after swapping:", x)
print("The value of y after swapping:", y)

#Swapping of 2 no's without using temp variable

x = 20
y = 40

x,y = y,x

print("The value of x after swapping:", x)
print("The value of y after swapping:", y)

#Swapping of 2 no's by taking input from user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

x,y = y,x

print("The value of x after swapping:", x)
print("The value of y after swapping:", y)



