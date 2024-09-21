num = 1/10
if num < 0:
    isneg = True
    num = abs(num)
else: 
    isneg = False
result = ''

if num == 0:
    result - '0'
while num > 0: 
    result = str(num%2) + result
    num = num//2
if isneg:
    result = '-' + result
    
print(result)