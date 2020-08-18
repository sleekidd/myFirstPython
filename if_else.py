# username = 'sleekidd'
# password = 'ade2012'

# input_username = input("Please enter username: ")
# input_password = input("Please enter password: ")

# if input_username == username:
#     print("Well done. Your username is correct")
#     print("...checking your password..")
#     print()

#     if input_password == password:
#         print("Congratulations! You are successfully logged in!")

# x = input("Enter a number: ")
# y = input("Enter a number: ")

# int_x = int(x)
# int_y = int(y)

# if int_x > int_y:
#     print("X is greater than Y")
#     print(x + " is greater than " + y)

# elif int_x < int_y:
#     print("X is less than Y")
#     print(x + " is less than " + y)

# else:
#     print("They have equal values")

# user_score = input("Enter score : ")

# score = int(user_score)

# print("Student", 'passed' if score >= 50 else 'failed')

# title = input("Title: ")
# name = input("Name: ")
# weight = input("Weight: ")
# height = input("Height: ")

# int_weight = int(weight)
# int_height = int(height)

# bmi = int_weight / (int_height * int_height)

# text = f"Hello {title} {name}, we realised that you recently signed up for our weight loss program, we see that you have a {weight}kgs and {height}ft tall which gives you a BMI of {bmi} and by standards is {'optimal' if bmi <= 25 else 'overweight'}, hence we recommend the {'optimal package' if bmi <= 25 else 'overweight package'}. Buy now at {'200' if bmi <= 25 else '500'} naira"

# print(text)

# If character variable taxCode is ’T’, increase price by adding the taxRate percentage of price to it.

# taxCode = input("TaxCode: ")
# price = input("Price: ")
# taxRate = input("TaxRate: ")

# int_price = int(price)
# int_taxRate = int(taxRate)

# if taxCode == "T":
#     price = int_price + (int_taxRate*int_price/100)

# print(price)


# Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.)

# year = input("Enter a year: ")

# int_year = int(year)

# # if int_year % 4 == 0:
# #     leapYear = True
# # else:
# #     leapYear = False
7
# # text = f"{leapYear}, {int_year} is {'a' if leapYear == True else 'not a'} leapyear"

# text = f"{'True' if int_year % 4 == 0 else 'False'}, {int_year} is {'a' if int_year % 4 == 0 else 'not a'} leapyear"

# print(text)


feeling_good = input("Are you feeling good? y/n: ")

if feeling_good == "yes":
    print("You are doing well, bye!")

elif feeling_good == "no":
    headache = input("Having headache?: ")

    if headache == "no":
        print("Drink water")

    elif headache == "yes":
        stressed = input("Stressed lately?: ")

        if stressed == "yes":
            print("Have some rest")

        elif stressed == "no":
            fever = input("Have you been feverish?: ")

            if fever == "yes":
                print("Call NCDC!")

            else:
                print("Sorry get help now!")
