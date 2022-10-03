print('Enter two variables: ')

a = input()
b = input()

x = int(a)
y = int(b)

x = x-y
y = x+y
x = y-x

print('After swapping: ')
print('a = ', x)
print('b = ', y)
