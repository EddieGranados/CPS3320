# year = int(input("Enter a year..."))

# if (year%4 == 0 or (year%100==0 and year%400==0)):
#     print("leap year")
# elif(year%4 != 0 and (year%100==0 and year%400!=0)):
#     print("not leap year")
# else:
#     print("not leap year")


# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("LP")
#         else:
#             print("NOT LP")
#     else:
#         print("LP")
# else:
#     print("LP")

##################################################################

# fName_List = ['Eddie Granados', 'Mike Jones', 'Jane Doe', 'Stan Smith', 'Master Chief']

# for login in name_List:
#     print(login[0])


# fName = input("Enter your first name... ")
# lName = input("Enter your last name... ")
# print("Login: ",fName[0] + lName[0:4])

##################################################################

# months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']

# num = eval(input("Enter a month number(1-12)... "))

# print("Month:", months[num-1])

##################################################################

months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']

userInput = input("Enter the date in xx/xx/xxxx format: ")

monthStr, dayStr, yearStr = userInput.split("/")

monthStr = months[int(monthStr)-1]

print("Converted: ", monthStr, dayStr + ", " + yearStr)

##################################################################

# Initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

# Records Intersection

# Using set() + "&" operator

res = tuple(set(test_tup1) & set(test_tup2))

print("The similar elements from tuples are : " + str(res))