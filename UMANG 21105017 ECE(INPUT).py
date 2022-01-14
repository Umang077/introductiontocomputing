#Question 1
number1=int(input("Enter First Number: "))
number2=int(input("Enter Second Number: "))
number3=int(input("Enter Third Number: "))
avg=(number1 + number2 + number3)/3
print("average of three numbers:",avg)
#Question 2
print("All values are to be entered in dollars.")
grossincome=float(input("Gross Income: "))
dependents=int(input("No.of dependents: "))
taxrate=0.2
standardreduction=10000
dependentdeduction=3000
taxableincome=(grossincome-standardreduction-(dependentdeduction*dependents))
tax=taxableincome*taxrate
print("Tax comes out to be :$",tax)
#Question 3
print("Student Details=[SID,Name,Gender,Course Name,CGPA")
sid=int(input("Enter your SID: "))
name=input("Enter your Name: ")
gender=input("Enter your Gender: ")
coursename=input("Enter Course Name: ")
cgpa=float(input("Enter CGPA: "))
student=[sid,name,gender,coursename,cgpa]
print("Student Info",student)
#Question 4
x=int(input("Enter marks of 1st Student: "))
y=int(input("Enter marks of 2nd Student: "))
z=int(input("Enter marks of 3rd Student: "))
w=int(input("Enter marks of 4th Student: "))
v=int(input("Enter marks of 5th Student: "))
marks=[x,y,z,w,v]
print("Marks of 5 Students are",marks)
#sorting the marks of student in ascending order
asc=marks.sort()
print("Marks in Ascending order",marks)
#Question 5
colour=['Red','Green','White','Black','Pink','Yellow']
print("Colour:",colour)
#Removing the 4th element.
colour.pop(3)
#Printing the modified list.
print("The modified list is Colour 1 =",colour)
#Removing 'Black' and 'Pink' colour with'Purple'.
colourB=['Red','Green','White','Black','Pink','Yellow']
colourB[3:5]=['purple']
print("The mdified list is colourB:",colourB)


