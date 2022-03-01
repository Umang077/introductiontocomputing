#Question 1
# Recursive Python function to solve tower of hanoi
print("Question 1")
print()

def TowerOfHanoi(n , A_rod, B_rod, C_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1,A_rod, C_rod, B_rod)
    print("Move disk",n,"from rod",A_rod,"to rod",B_rod)
    TowerOfHanoi(n-1, C_rod, B_rod, A_rod)
         
# Driver code
n =int(input("No of Disc chosen by the user(must be Greater than 0): "))
print("Tower Of Hanoi is:")
TowerOfHanoi(n, 'A', 'C', 'B') # A, C, B are the name of rods

#Question 2
from math import comb
while True:                                                                                             #Loop for preventing -ve input of no. of rows (because they can't be -ve)
    n = int(input("Enter the number of rows you want to print: "))                                      #Asking the user the number of rows he/she wants
    if n >= 0:
        break
    else:
        print("Number of rows must be positive, please enter the value again!")

#RECURSION
print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    if num == 0:
        return [[0]]
    elif num == 1:                                                                                      #Base case
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                                                  #Recursive call
        current_row = [1]                                                                               #The first element of each row, i.e. 1
        previous_row = result[-1]                                                                       #Taking the last row from the data of all rows
        for i in range(len(previous_row)-1):                                                            #Loop for adding the values of top 2 numbers for computing current number's value
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                                              #The last element of each row, i.e. 1
        result.append(current_row)                                                                      #Adding the computed row to the data of all rows
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                                                        #This print() adds space before printing each row
    for j in i:
        if j != 0:
            print(j, end =" ")
    print()

#ITERATION
print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                      #Outer loop is for the rows
    print((n-i-1)*" ",end="")                                                                           #This print() adds space before printing each row
    for j in range(n):                                                                                  #Inner loop is for the individual elements to be printed
        if comb(i,j) != 0:                                                                              #Condition to ignore the cases when combination = 0 (when j>i)
            print(comb(i,j),end=" ")                                                                    #This print() prints each element and adds space after printing each value
    print()                                                                                             #This print() is for changing line for next row

#Question 3
print("Question 3")
print()
first_value = int(input("Enter first integer value(dividend): "))
while True:                                                                                             #Loop to make sure second_value != 0(i.e. denominator must not be 0)
    second_value = int(input("Enter second integer value(divisor): "))
    if second_value != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(first_value,second_value)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("Part a")
print("\nCheck whether the function (divmod()) is callable or not:")                                 
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")
print("Part b")
print("\nCheck whether all the values are zero or not:")                                             
if all(x != 0 for x in result):
    print("All values in result(i.e. quotient and remainder) are non-zero.")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0).")

print("Part c")
print("\nAdd (4,5,6) to the result and filter out values greater than 4:")                           
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4(in list format) are:", c_part_output)

print("Part d")
print("\nConvert the above result into a set datatype:")                                             
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("Part e")
print("\nMake the set immutable:")                                                                   
e_part = frozenset(d_part)
print("The immutable set would be:", e_part)

print("Part f")
print("\nEvaluate the maximum value from the set and find out its hash value:")                      
f_part = max(e_part)
print("The maximum value from the set is:", f_part)
print("The hash value of %d(considering it to be integer) is %d and its hash value is %d(if we consider %s as a string)." % (f_part,hash(f_part),hash(str(f_part)),str(f_part)))

#Question 4
print("Question 4")
print()
class Student:                                                                                          
    def __init__(Self,Name,RollNumber):
        Self.Name = Name
        Self.RollNumber = RollNumber
        print("Object Created\n")
    def __del__(self):
        print("\nObject destroyed")
Name = input("Enter name of student: ").strip()                                                         
Roll_No = int(input("Enter SID of %s: " % (Name)))
student1 = Student(Name,Roll_No)                                                                        
print("The name of the student is %s and his/her roll number is %d." % (student1.Name,student1.RollNumber))     
del student1                                                                                            

#Question 5
print("Question 5")
print()
#forming class employees
class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
first_employee=employees("Mehak",40000)
second_employee=employees("Ashok",50000)
third_employee=employees("Viren",60000)
#print employee detail
first_employee.pfun()
second_employee.pfun()
third_employee.pfun()
#Updating salary of Mehak to 70000
print("\nPart(a)")
first_employee.salary=70000
print("Mehak salary Updated to 70000")
first_employee.pfun()
#Deleting Viren's data
print("\nPart(b)")
del third_employee
print("Employee Viren's data has been removed.")

#Question 6
print("Question 6")
print()
gap=" "*10
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME:")
#definig principle of game i.e. anagram
def anagram(word1,word2):
   
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter name of first player:"))
player2=str(input("Enter name of the second player:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")

