'''
Write a program in which input a string and convert the lower case
characters to upper case and upper case characters to lower case.
'''

string = input("Please Enter your Own String : ")

string1 = ''

for i in string:
    if(ord(i) >= 65 and ord(i) <= 90): 
        string1 = string1 + chr((ord(i) + 32)) 
    elif(ord(i) >= 97 and ord(i) <= 122):
        string1 = string1 + chr((ord(i) - 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)