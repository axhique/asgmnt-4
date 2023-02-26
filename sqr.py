#to take user input
user = input("Enter a list :").split(',')
l1=[]
for i in user:
    l1.append(int(i))

#actual funtion
square=lambda num: num**2
print(list(map(square,l1)))

#sample :
#  Enter a list :5,8,7,9,22
#  [25, 64, 49, 81, 484]