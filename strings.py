#Generate a function to check whether a given string contains only alphabets.
s="pythonisinterpretedlanguage"
m=s.isalpha()
print(m)

#Create a method to verify if a string consists solely of digits.
d="63865245"
m=d.isdigit()
print(m)

#Develop a function to determine if a string is alphanumeric.
d="jhf8638"
m=d.isalnum()
print(m)

#Write a function that capitalizes the first letter of every word in a sentence.
m="python is interepreted dynamic programming"
c=m.title()
print(c)

#Implement a method to count the number of words in a given sentence.
s="python is interepreted dynamic programming"
m=s.split(" ")
count=0
for i in m:
    count+=1
print(count)

#Design a function to remove all vowels from a specified string.
s="Design a function to remove all vowels from a specified string."
cons=""
for i in s:
    if i not in "aeiouAEIOU":
        cons+=i
print(cons)

#Construct a function to check whether a given string is a palindrome.
s="madam"
m=s[::-1]
if m==s:
    print("palindrome")
else:
    print("not palindrome")
        
#Develop a method to replace multiple spaces in a string with a single space.
n="python   is good  programming   language"
q=""
m=n.split()
for i in range(len(m)):
    if i==0:
        q+=m[i]
    else:
        q+=" "+m[i]
print(q)

#Create a function to convert a sentence into camelCase.
s="python is simple to understand"
p=""
m=s.split()
for i in range(len(m)):
    if i==0:
        p+=m[i]
    else:
        p+=m[i].title()
print(p)


#Write a function to convert a sentence into snake_case.
s="Python Is Simple To Understand"
snake_case=""
m=s.split()
for i in range(len(m)):
    if i==0:
        snake_case+=m[i].lower()
    else:
        snake_case+="_"+m[i].lower()
print(snake_case)

    