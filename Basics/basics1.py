#Chapter 1:
# the basics

# name = input("enter first name :")
# name2 = input("enter surname :")
# print("Hello ", name, name2)

# print('what do you call a bear with no teeth ? \n "A gummy brear!" ')

# num1 = int(input("enter num1"))
# num2 = int(input("enter num2"))
# num3 = int(input("enter num3"))
# print("the total is ", (num1+num2)*num3)
#
#
# print("how many slices of the pizza you started with\n")
# slices = int(input())
# print("How many slices have you eaten till now?")
# eaten = int(input())
#
# remaining = slices - eaten
# print(f"so now you have left with {remaining} slices")

# name = input("enter name ")
# age = int(input("enter age"))
#
# print(f"{name} next birthday you will be {age+1}")

# total = int(input("total bill price :"))
# person = int(input("total persons had dinner :"))
#
# print(f" each person has to pay {total/person} amount !")

# days = int(input("enter days :"))
#
# hour = 24*days
# minutes = 24*60*days
# seconds = 24*60*60*days
#
# print(f"In {days} there will be {hour} hours, {minutes} minutes and {seconds} seconds!")

# weight = int(input("enter weight in kg :"))
# print(f"{weight} kg in pounds = {2204 * weight} pounds")

# num1 = int(input("enter the number over 100"))
# num2 = int(input("enter the number less then 10"))
#
# print(f"{num1} is larger then {num2} : {num1//num2} times approx")
#
# num1 = int(input("enter num1 :"))
# num2 = int(input("enter num2 :"))
#
# if num1>num2:
#     print(num1, num2)
# else:
#     print(num2, num1)
#
# print("Is it raining")
# raining = input()
# raining = str.lower(raining)
# if raining == "yes":
#     print("is it windy ")
#     windy = input()
#     if windy == "yes":
#         print("it is too windy for an umbrella ")
#     else:
#         print("taka an umbrella")
# else:
#     print("enjoy your day")
#
# name = input("enter name")
# print(len(name))

# name = input("enter name")
# surname = input("enter surname")
# join = name + " " + surname
# print(join)
# print(len(join))

# word = input("enter the word :")
# first = word[0]
# length = len(word)
#
# Next = word[1:length]
#
# if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
#     newword = Next + first + "ay"
# else:
#     newword = word +"way"
# print(newword.lower())

#
# num = float(input("enter number :"))
# print(round(num*2 ,2))
#
# import math
# num = int(input("enter num larger then 500"))
# sq = math.sqrt(num)
# print(round(sq, 2))

# print(round(math.pi, 2))

# import  math
# radius = float(input("enter the radius of the circle :"))
# area = round(math.pi, 2) * radius * radius
# print(area)
#
# num1 = int(input("enter num1 :"))
# num2 = int(input("enter num2 :"))
#
# div = num1//num2
# rem = num1 % num2
#
# print(f"{num1} divided by {num2} is {div} with {rem} remaining")
#
# print(" 1-> square\n2-> triangle")
# value = int(input("enter a number :"))
# if value == 1:
#     side = int(input("enter the side of square :"))
#     print(side * side)
# elif value == 2:
#     base = int(input("enter the base of a triangle :"))
#     height = int(input("enter the height of a triangle :"))
#     print(1/2 * base * height)
# else:
#     print("invalid input :")

# name = input("enter name :")
# num = int(input("enter total time name should be printed :"))
# for i in range(0, num):
#     print(name)
#
# name = input("enter name :")
# for i in range(0, len(name)):
#     print(name[i])
#
# name = input("enter name :")
# num = int(input("enter total times you want to print name :"))
# for x in range(0, num):
#     for i in name:
#         print(i)

# num = int(input("enter a number smaller then 50 :"))
# for i in range(50, num-1, -1):
#     print(i)

# name = input("enter name :")
# num  = int(input("enter number :"))
# if num<10:
#     for i in range(0, num):
#         print(name)
# else:
#     for i in range(0, 3):
#         print("Too high")
#
# total = 0
# print("enter 5 numbers")
# for i in range(0, 5):
#     num = int(input("enter  number"))
#     ask = input("do you want to add this number to total : y or n")
#     if ask == "y":
#         total = total + num
# print(total)

# total = 0
# while total <= 50:
#     num  = int(input("enter number"))
#     total = total + num
#     print("total is  = ", total)
