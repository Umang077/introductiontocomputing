#Question 1
print("Question 1")
print()
#taking input from user
sentence =input("Please give an input- ")
print()
sentence=sentence.lower().strip()
i=0
#defining empty dictionary to use later to store element, counter pairs and eliminating common letters and words
dict={}

#checking if the string input is a word or a sentence
if " " not in sentence:
     #searching for common elements
     while i<len(sentence):
          counter=0
          k=0
          while k<len(sentence):
               if sentence[i]==sentence[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing the values in dictionary
          dict[f"{sentence[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sentence)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurrences of each character in the given input is-")
for key,value in dict.items():
    print(f"{key}:{value}")

#Question 2
print("Question 2")
print()
def is_leap_year(year: int) -> bool:     #Function for checking if the given year is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                           #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:             #Condition for no. of days in February
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:   #Setting no. of days in the given month
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:    #Syntax for incrementing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))

#Question 3
print("Question 3")
print()
#Defining an empty list to take input from the user.
List1=[]
print("Please enter integer number > 0 for number of elements in list.")
n=int(input("Enter number of elements for the list:"))
for i in range(0,n):
     for y in range(i+1,i+2):
         nth_numb=int(y)
     element=int(input("Number %d:"%(nth_numb)))
     List1.append(element)
print("The list formed:",List1)
#Defining an empty list to store tuple pairs later.
List2=[]
for x in List1:
    tuple_a=(x,x**2)
    List2.append(tuple_a)
print(List2)

#Question 4
print("Question 4")
print()
'''given_table is a list of lists'''
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("Error!\nThe grade point must be between 4 and 10")
for i in given_table:                                                                                               #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))
            break

#Question 5
print("Question 5")
print()
print("The pattern is printed below:")
print()
# Letters to be printed
alphabets = "ABCDEFGHIJK"
# forming a list of letters
list_alphabets = []
for i in alphabets:
    list_alphabets.append(i)
# Applying while loop to print only required rows
k = 1
while k <= 6:
    # printing 1st row intially when k=1
    for el in list_alphabets:
        print(el, end="")
    # forming second row elements to be printed
    list_alphabets.pop(len(list_alphabets) - 1)  # removng last element of list
    list_alphabets.pop(len(list_alphabets) - 1)  # removing last element of list
    list_alphabets.insert(0, " ")  # insertind space
    print()  # changing line using print()
    k = k + 1

#Question 6
print("Question 6")
print()
condition=True
#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        Sid=int(input("Please Enter SID of the Student- "))
        student_name=input("Please enter the name of the Student- ")
        Dictionary[Sid]=student_name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part (a)")
print()
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part (b)")
print()
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part (c)")
print()
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary:{Key_sort_dict}")
print("")

print("Part (d)")
print()
Sid_tbf=int(input("Please enter the student's SID whose detail you require: "))
if Sid_tbf in Dictionary.keys():
    print(f"Name of the required student is: {Dictionary[Sid_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")

#Question 7
print("Question(7)")
print()
print("Fibonacci sequence")
print()
number=int(input("Total elements of Fibonacci sequence that you want and it must be greater than 1- "))
#using the formula of the sum of previous two terms is equal to the present term.
a_n1=1
a_n2=0
n=0
#initializing sum with first two terms
sum=a_n1+a_n2
#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)
#Printing the remaining fibonnaci terms
while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
#printing the program end prompt
print(f"Average of total {number} terms of sequence is {average}")
print("END")

#Question 8
print("Question 8")
print()
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#Part(a)
Newset0=Set1^Set2   # (^)This symbol represent exclusive OR operator.
print("Part(a)\nNew Set of all the elements that are in Set1 and Set2 but not in both:",Newset0)
#part (b)
Newset1=Set1^Set2^Set3 
print("Part(b)\nNew Set of all the elements that are in only one of the three sets Set1,Set2,Set3:",Newset1)
#Part (c)
Newset2=(Set1|Set2|Set3)-(Set1^Set2^Set3)  #(|) This symbol reprsents OR operator.
print("Part(c)\nNew Set of elements that are excatly two of the sets:",Newset2)
#Part (d)
Newset3=set()
for x in range(1,11): #.add function allow us to add elements in a set if not already present in it.
    Newset3.add(x)
Not_common_set1=Newset3-Set1
print("Part(d)\nNew Set of all integers in the range1 to 10 that are not present in Set1:",Not_common_set1)
#Part (e)
Newset4=set()
for x in range(1,11):
    Newset4.add(x)
Not_common_anyset=Newset4-(Set1|Set2|Set3)
print("Part(e)\nNew Set of all the integers in the range 1 to 10 that are not in Set1,Set2,Set3:",Not_common_anyset)






