a = int(input('Enter first side: '))  
b = int(input('Enter second side: '))  
c = int(input('Enter third side: '))  
   
s = (a + b + c) / 2  
area = (s*(s-a)*(s-b)*(s-c)) 
print("The area of the triangle is" ,area)   