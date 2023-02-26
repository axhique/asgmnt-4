#to take user input
user = input("Enter a list :").split(',')
l1=[]
for i in user:
    l1.append(int(i))


triple = lambda s:s*3
print(list(map(triple,l1)))


#sample  :
#Enter a list :4,5,8,7,12
#[12, 15, 24, 21, 36]
