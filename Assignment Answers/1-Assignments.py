
#1. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population, 
#  write a program to find the total number of illiterate men and women if the population of the town is 80,000.

"""

mens_literacy = 35
total_population = 80000
percentage_of_total_literacy =  48


percentage_of_total_illiteracy =  100 - percentage_of_total_literacy

total_number_of_illiterate_men_and_women = (percentage_of_total_illiteracy / 100) * total_population

#print(total_number_of_illiterate_men_and_women)

total_number_of_illiterate_men = (mens_literacy/100) * total_number_of_illiterate_men_and_women
#print(total_number_of_illiterate_men)

total_number_of_illiterate_women = total_number_of_illiterate_men_and_women - total_number_of_illiterate_men 
print("Total illiterate men and women = ",total_number_of_illiterate_men_and_women)
print("Total illiterate men = ",total_number_of_illiterate_men)
print("Total illiterate Women = ",total_number_of_illiterate_women)

"""


#2. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, 
#   find the total number of currency notes of each denomination the cashier will have to give to the withdrawer

"""
   
amount = int(input("Enter Amount Greater Than are Equals to 100 : "))

hundreds = 0
fifties = 0 
tens = 0

remaining_amount = 0

if amount >= 100 :
    hundreds = amount // 100 
    remaining_amount = amount - (hundreds * 100)
    #print(remaining_amount)
    if remaining_amount >= 50 :
        fifties = remaining_amount // 50
        remaining_amount = remaining_amount - (fifties * 50)
    if remaining_amount >= 10 :
        tens = remaining_amount // 10
        remaining_amount = remaining_amount - (tens * 10)

print("No of Hundreds : ", hundreds, " No of Fifties : ", fifties, " No of Tens : ", tens)

"""


#3. While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. 
#   If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

"""
quantity = int(input("Enter Quantity : "))
price = int(input("Enter Price : "))
discount_per = 10

if quantity > 10 :
    amount = quantity * price
    #print(amount)
    discount_amount = (amount/100) * discount_per
    #print(discount_amount)
    total_amount = amount - discount_amount
    print("Total expenses : ", total_amount)
else :
    total_amount = quantity * price
    print("Total expenses : ", total_amount)
"""


#4. If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. 
#   If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. 
#   If the employee's salary is input through the keyboard write a program to find his gross salary

"""

basic_salary = int(input("Entrer Basic Salary : "))

if basic_salary < 1500 :
    hra_per = 10
    da_per = 90
    hra_amount = (basic_salary/100) * hra_per
    da_amount = (basic_salary/100) * da_per
    gross_salary = basic_salary + hra_amount + da_amount
    print("Gross Salary : ", gross_salary)
else :
    hra_amount = 500
    da_per = 98
    da_amount = (basic_salary/100) * da_per 
    gross_salary = basic_salary + hra_amount + da_amount
    print("Gross Salary : ", gross_salary)


"""    


# 5. If the ages of Ram, Shyam and Ajay are input through the keyboard, 
# write a program to determine the youngest of the three.

"""

ram = int(input("Enter Ram Age : "))
shyam = int(input("Enter Shyam Age : "))
ajay = int(input("Enter Ajay Age : "))

if ram < shyam and ram < ajay :
    print("Ram is Youngest")
elif shyam < ajay :
    print("Shyam is Youngest")
else :
    print("Ajay is Youngest")


"""


#6. Any year is entered through the keyboard, write a program to determine whether the year is leap or not. 
#   Use the logical operators && and ||.

# Leap year conditions:
    # 1. If a year is divisible by 400, or
    # 2. If a year is divisible by 4 and not divisible by 100.
    

"""

year = int(input("Enter a Year : "))

if (year % 400 == 0 ) or (year % 4 == 0  and  year % 100 != 0) :
    print(year, " is a leap year")
else :
    print(year, " is not a leap year")


"""


# 7. A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, 
#   for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. 
#   If you return the book after 30 days your membership will be cancelled. 
#   Write a program to accept the number of days the member is late to return the book
#   and display the fine or the appropriate message.

"""

days = int(input("Enter the no of days the member is late : "))

if days <= 5 :
    fine_amount = days * 0.5
    print("Fine Amount : ",fine_amount)
elif days <= 10 :
    fine_amount = (5 * 0.5) + ((days-5) * 1)
    print("Fine Amount : ",fine_amount)
elif days <= 30 :
    fine_amount = (5 * 0.5) + ((5) * 1) + ((days-10) * 5)
    print("Fine Amount : ",fine_amount)
else :
    print("Your membership is cancelled." )


"""


#8. In a company, worker efficiency is determined on the basis of the time required for a worker to complete a particular job. 
#   If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly efficient. 
#   If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve speed. 
#   If the time taken is between 4 – 5 hours, the worker is given training to improve his speed, 
#   and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. 
#   If the time taken by the worker is input through the keyboard, find the efficiency of the worker.

"""

time = float(input("Enter the time is more than are equals to 2 hours : "))
if time >= 2 and time < 3 :
    print("Highly efficient")
elif time >= 3 and time < 4 :
    print("Improve speed")
elif time >= 4 and time < 5 :
    print("Given training to improve his speed")
elif time >= 5 :
    print("worker has to leave the company")

"""



#9. Write a program to print the Armstrong numbers between 100 to 999.
#Example : 371 is an Armstrong Number as the sum of the powers of all digits of N is equal to 371.
#          ( 3**3 + 7**3 + 1**3 )

"""

armstrong_nums = []
for i in range(100, 999):
    arm = 0 
    for j in str(i):
        arm += int(j) ** 3
    if arm == i :
        armstrong_nums.append(i)
print("The Armstrong numbers between 100 to 999 : ", armstrong_nums)

"""


#10. Write a program to find the reverse of n digit number using While loop  

"""

number = input("Enter a number : ")

reverse = "" 

count = 1
while count <= len(number):
    reverse += number[len(number) - count]
    #print(number[len(number) - count])
    count += 1 
print("Original number : ", number, " => Reverse number : ", reverse)

"""


#11. Write a Python program to check a list is empty or not

"""
list_a = [1, 2, 3, 4, 5]
list_b = []
msg = ""
if len(list_a) == 0 :
    #print("List_A is empty")
    msg += "List_A is empty"
else :
    #print("List_A is not empty")
    msg += "List_A is not empty"

msg += " and "

if len(list_b) == 0 :
    #print("List_B is empty")
    msg += "List_B is empty"
else :
    #print("List_B is not empty")
    msg += "List_B is not empty"
print(msg)

"""



#12. Write a program to find the Fibonacci Series of the given number.

"""

number = int(input("Enter a number : "))
fibonacci_series = [0, 1]
for i in range(number):
    if i <= 1:
        continue
    fibonacci_series.append(fibonacci_series[-1]+fibonacci_series[-2])
print(fibonacci_series)

"""


# 13. Write a program to find the given number is perfect number

"""

n = int(input("Enter number : "))
sums = 0 
for i in range(1, n):
    if(n%i == 0):
        sums += i 
if (sums == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

"""


#14. Write a program to check whether a triangle is valid or not, 
#    when the three angles of the triangle are entered through the keyboard. 
#    A triangle is valid if the sum of all the three angles is equal to 180 degrees.

    
"""

angle_a = int(input("Enter the angle a : "))
angle_b = int(input("Enter the angle b : "))
angle_c = int(input("Enter the angle c : "))
sum_of_three_angles = angle_a + angle_b + angle_c
if sum_of_three_angles == 180 :
    print("Sum of three angles are equals to 180, so it is valid triangle")
else :
    print("Sum of three angles are not equals to 180, so it is not a valid triangle")

"""



#15. A five-digit number is entered through the keyboard. 
#    Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.

"""

num = input("Enter a five-digit number : ")
reversed_number = num[::-1]

if int(num) == int(reversed_number) :
    print("The original and reversed numbers are equal")
else:
    print("The original and reversed numbers are equal or not")

"""