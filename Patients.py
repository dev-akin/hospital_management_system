import json
import os
from datetime import date, datetime

class Patients:
    def __init__(self, ID = 0, name = "gusest", age = "2001-01-01", typ = "default", status = False):
        self.ID = ID
        self.name = name
        self.age = age
        self.typ = typ
        self.status = status
        
    def patients(self):
        # file path
        filePath = "C:/Users/USER/Desktop/mini_project/project/hospital/patients.json"  

        # data to be written in json file 
        data = {
            "id"    : self.ID,
            "name"  : self.name,
            "DOB"   : self.age,
            "type"  : self.typ,
            "status": self.status
        }
        
        # checking if file exists and is not empty
        f = []
        if os.path.exists(filePath) and os.path.getsize(filePath) > 0:
            with open(filePath, "r") as reader:
                try:
                    f = json.load(reader)
                except(FileExistsError, json.JSONDecodeError):
                    f = []
        else:
            f = []

        # appending data to the list
        f.append(data)

        # writing to json file
        with open(filePath, "w") as writer:
            json.dump(f, writer, indent=4)

        # success message
        print("Patient added successfully")       

    # view patient details
    def viewPatient(self):

        # file path
        filePath = "C:/Users/USER/Desktop/mini_project/project/hospital/patients.json"
         
        # reading from a json file
        with open(filePath, "r") as reader:
            json_data = json.load(reader)

            # menu
            print()
            print("="*30)
            print("Enter 1 to search user")
            print("Enter 2 to view all users")
            print()
            inp = int(input("Option: "))
            print("="*30)
            print()
            
            # validating user input
            if inp == 1:
                id = int(input("Enter user ID: "))

                # searching for user in json file
                for i in json_data:
                    if i["id"] == id:
                        print(f"ID: {i["id"]}")
                        print(f"Name: {i["name"]}")
                        print(f"DOB: {i["DOB"]}")
                        print(f"Type: {i["type"]}")
                        print(f"Status: {i["status"]}")
                        break
                # if user is not found in json file
                else:
                    if i["id"] != id:
                        print()
                        print("="*20)
                        print("No record found")
                        print("="*20)

            # validating user input
            elif inp == 2:
                count = 1
                for i in json_data:
                    print(f"========== Patient {count} ==========")
                    print(f"ID: {i["id"]}")
                    print(f"Name: {i["name"]}")
                    print(f"DOB: {i["DOB"]}")
                    print(f"Type: {i["type"]}")
                    print(f"Status: {i["status"]}")
                    print()

                    count += 1

                


                

