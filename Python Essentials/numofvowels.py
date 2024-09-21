
numVowels = 0
s = 'azcbobobegghakl'

vowels = 'a', 'e', 'i,', 'o', 'u'

for char in s:
    if char in 'aeiou':
        numVowels += 1

print('Number of vowles:' + "" + str(numVowels))


numbob = 0
s = 'azcbobobegghakl'

for i in range(len(s) - 2):  # Loop through the string, but stop 2 chars before the end
    if s[i:i+3] == 'bob':  # Check for the substring 'bob' of length 3
        numbob += 1

print('Number of times bob occurs is:' + " " + str(numbob))


longest = ''
current = ''
for i in range(len(s)):
    if i == 0 or s[i] >= s[i - 1]:  
        current += s[i]  
    else:
        current = s[i]  
    
    if len(current) > len(longest):
        longest = current

# Print the result
print('Longest substring in alphabetical order is: ' + longest)

