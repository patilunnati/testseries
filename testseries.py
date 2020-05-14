'''
#1.[a] Given a number count the total number of digits in a number

x = input("enter your no :")
print(len(x))        
'''

'''
#[b] Reverse the following list using for loop
#list1 = [10, 20, 30, 40, 50]

list1 = [10,20,30,40,50]
for i in range(len(list1)):
    print(list1[-(i+1)])

'''

'''
#2. given two string, s1 and s2, create a new string by  s

def appendMiddle(s1, s2):
    Indx = int(len(s1)/2)
    print("Orginal String : ",s1 , s2)
    Middle = s1[:Indx-1:] + s2 + s1[Indx-1:]
    print("After appending new string in middle : ", Middle)
s1 = str(input("Enter the string :"))
s2 = str(input("Enter the string :"))
appendMiddle(s1 , s2)
'''

    
'''
#3. Arrange String characters such that lowercase letters should come first

Str = str(input("Enter the String : "))
lowerCase = []
UpperCase = []

for i in Str:
    if i.islower():
         lowerCase.append(i)
    else:
         UpperCase.append(i)
Str1 = ''.join(lowerCase + UpperCase)
print("Final String : \n", Str1)

'''
'''
# 4.4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters


import re

Str = "English = 88 Science = 80 Math = 90 History = 60"
MarkList = [int(num) for num in re.findall(r'\b\d+\b', Str)]
TotalMarks = 0
for i in MarkList:
	TotalMarks += i

Percentage = TotalMarks/len(MarkList) 
print("Total Marks is = ", TotalMarks, "\n","Percentage is = ", Percentage)
'''
'''
#.5 .Given a two list. Create a third list by picking an odd-index element from the first list and even index
#   elements from second.

p = input("Enter the list1 : ")
list1 = p.split(",")
q = input("Enter the list2 : ")
list2 = q.split(",")

list3 = list()

OddElement = list1[1::2]
print("Element at odd-index positions from list one : \n",OddElement)

EvenElement = list2[0::2]
print("Element at even-index positions from list two : \n",EvenElement)

print("Printing Final third list :")
list3.extend(OddElement)
list3.extend(EvenElement)
print(list3)
'''
















