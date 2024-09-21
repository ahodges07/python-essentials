x = 2 
while(x < 5):
    print(x)
    x=x+1

for x in range (20):
    print(x)

#Adds 7, 8, 9 together     
mysum = 0
for i in range (7,10):
    mysum += i
print(mysum)

#Adds 5, 7, 9 together
mysum = 0
for i in range (5,11,2):
    mysum += i
    if mysum == 5:
        break
print(mysum)

happy = -15
    
if (happy > 2):
    print('hello world')
    
else: print('error')

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 


num = 10
while num > 3:
    num -= 1
print(num) 

