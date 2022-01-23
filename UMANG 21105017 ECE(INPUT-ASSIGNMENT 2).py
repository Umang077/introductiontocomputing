#Question 1
value="Python is a case sensitive language"
print('(a): The length of the string:',len(value))
value2="Python is a case sensitive language"[::-1]
print('(b): The reverse order of the string in one line code is:',value2)
value3=value[9:]
print('(c): New String =',value3)
value4=value.replace("a case sensitive","object oriented")
print('(d):',value4)
x=value.find('a')
print('(e): Index of substring "a" in the given value is:',x)
value5="Python"+"is"+"a"+"case"+"sensitive"+"language"
print('(f): The new value without any space is:',value5)
#Question 2
name=input('Name of the Student:')
sid=int(input('SID of the Student:'))
depname=input('Department of the Student:').upper()
marks=float(input('CGPA of the Student:'))
print("Hey,%s here!\nMy SID is %d\nI am from %s department and my CGPA is %f"%(name,sid,depname,marks))
#Question 3
a=56
b=10
print("(a)  a&b=%d"%(a&b))
print("(b)  a|b=%d"%(a|b))
print("(c)  a^b=%d"%(a^b))
print("(d)  Left shifting both a and b with 2 bits is:%d,%d"%(a<<2,b<<2))
print("(e)  Right shifting a with 2 bits and b with 4 bits is:%d,%d"%(a>>2,b>>4))
#Question 4
a=int(input("First Number:"))
b=int(input("Second Number:"))
c=int(input("Third Number:"))
if(a>=b) and (a>=c):
  print("The Greatest number is ",a)
elif(b>=a) and (b>=c):
  print("The Greatest number is ",b)
else:
  print("The Greatest number is ",c)
#Question 5
inputstring=input("String: ")
if("name")in inputstring:
  print("Yes.\nThe word 'name'is present in the String.")
else:
  print("No.\nThe word 'name'is not present in the String.")
#Question 6
x=float(input("Lenght(a): "))
y=float(input("Lenght(b): "))
z=float(input("Lenght(c): "))
if(x>=y+z) or(y>=z+x) or (z>=x+y):
  print("NO.\nTriangle cannot be formed.")
else:
  print("YES.\nTriangle can be formed With sides,")
  print("Side(1):%d\nSide(2):%d\nSide(3):%d"%(x,y,z))

    
