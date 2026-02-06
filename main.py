import Patients
import random
import json
import os
import bcrypt
def main():

    """    
    password hashing
    print()
    passs = "admin@hospital".encode()
    hashed = bcrypt.hashpw(passs, bcrypt.gensalt())
    print(hashed)
    """



    # admin login
    adminUser = input("Admin Username: ")
    adminPass = input("Admin Password: ").encode()

    # file path
    filePath = "C:/Users/USER/Desktop/mini_project/project/hospital/admin.json"  

    # reading from a json file
    with open(filePath, "r") as admin:
        adminDetail = json.load(admin)

    # password from json file
    adminPasswordJson = adminDetail["password"].encode()

    # validating admin login details
    if adminDetail["username"] == adminUser:
        if bcrypt.checkpw(adminPass, adminPasswordJson):
            os.system("cls")
            print(" " * 8,"Admin logged in successfully"," " * 8)
            print()

            # main menu
            while True:

                # menu
                print()
                print(" "*12, "="*20, " "*12)
                inc =" " * 10
                print(inc,"Enter 1 to add Patient",inc)
                print(inc,"Enter 2 to view Patient",inc)
                print(inc,"Enter 3 to add Doctor",inc)
                print(inc,"Enter 4 to view Doctor",inc)
                print(inc,"Enter 5 to add Appointment",inc)
                print(inc,"Enter 6 to view Appointment",inc)
                print(inc,"Enter 7 to Exit",inc)
                print(" "*12, "="*20, " "*12)
                print()

                # user input for menu option
                choice = int(input("Choice: "))
                
                # menu options
                match choice:
                    case 1:
                        ID = random.randint(100000, 999999)
                        name = input("Enter your name: ")
                        dob_input = input("Enter date of birth(yyyy-mm-dd): ")
                        typ = "Patients"
                        status = True

                        p = Patients.Patients(ID, name, dob_input, typ, status)
                        p.patients()
                    case 2:
                        p = Patients.Patients()
                        p.viewPatient()
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        break
        else:
            print("Invalid Details")
    else:
        print("Invalid Details")



if __name__ == "__main__":
    main()