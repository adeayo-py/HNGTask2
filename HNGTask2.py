from random import choice
from string import ascii_letters


employee_data = []

def initializer():
    question=input("Are you a new employee? Type Y for Yes and N for No: ")
    cont=True
    while cont:
        if question.upper()=="Y":
            return password_generator()
        elif question.upper()=="N" and employee_data!=[]:
            print(" ")
            print("Here is the database of the newly registered member(s)")
            print(" ")
            for employee in employee_data:
                print(f"Hello {employee['First name']} {employee['Last name']}, your email address is "
                      f"{employee['email address']} and your password is {employee['Password']}")
                print(" ")
            print("Thank you. Bye!")
            break
        elif question.upper()=="N" and employee_data==[]:
            print("This place is not for oldies and there is no data available. Bye!")
            break
        else:

            question=input("Are you a new employee? Type Y for Yes and N for No: ")



def employee_info():
    print(" ")
    print("Welcome to HNG tech! To continue your onboarding process,we need you to provide us with some details.")
    print(" ")

    first = str(input("Kindly input your first name: "))
    last = str(input("Kindly input your last name: "))
    email_add = str(input("Kindly input your email address: "))
    first_name=first.title()
    last_name=last.title()
    email=email_add.lower()

    employee_details = {
        "First name": first_name,
        "Last name": last_name,
        "email address": email
        }
    employee_data.append(employee_details)
    return employee_details, employee_data

def password_generator():

    details, data =employee_info()
    password=details["First name"][0:2]+details["Last name"][-2:]+''.join(choice(ascii_letters) for x in range(5))
    print(" ")
    print(f"Based on our suggestion {details['First name']}, your password is {password}")
    print(" ")

    while True:
        new_password=str(input("Are you cool with the password generated for you? Type Y for Yes and N for No: "))
        print("")
        if new_password.upper()=="Y":

            print("Hold on to check for your details. Thank you for registering!")
            print(" ")
            break

        elif new_password.upper()=="N":
            change_password=str(input("Kindly type your desired password. Make sure that it has atleast 7 characters: "))

            while len(change_password)<7:
                change_password=str(input("Kindly type your desired password. Make sure that it has atleast 7 characters: "))
            else:
                password=change_password
                print(" ")
                print("Thank you for registering!")
                print(" ")
                break
        else:
            print(" ")
            print("Check the instruction again!")
            print(" ")
    details["Password"]=password

    return data, initializer()


initializer()
