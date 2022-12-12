# EXAMPLE - 1:
# Write a python function which gives the length of string without using built-in len() method

# def length(s):
#     """This new function to find the length of your string"""
#     count = 0
#     for i in s:
#         if type(s) == str:
#             count += 1
#     return count
#
#
# s = input("Enter your string : ")
#
# print(f"The length of {s} string is {length(s)}")

# EXAMPLE - 2:
# Write a python function which print the index of list element without using index function

# count = int(input("Enter the number of elements in your list : "))
# lists = []
#
# for i in range(1, count + 1):
#     ele = int(input(f"Enter your {i} list element : "))
#     lists.append(ele)
#
#
# def indexes(lists):
#     for i in range(0, length(lists)):
#         print(lists[i], " : ", i)
#
#
# print("Element : Index")
# indexes(lists)

# EXAMPLE - 3:
# Write a function that gives the IP address of your system

# import socket
#
#
# def ip_address():
#     print("IP Address of my system is : ", socket.gethostbyname(socket.gethostname()))
#
#
# ip_address()

# EXAMPLE - 4:
# Write a function which will shut down your system

# import os
#
# os.system("Shutdown /r /t 4")
# /s : shutdown /r : restart /t : timer

lists = ["aayush", "pratvi", "chirag", "falguni"]

print(list(map(lambda a: a.upper(), lists)))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func = lambda a: a if a % 2 == 0 else ''

print(list(map(func, l)))