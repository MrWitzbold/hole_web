def help():
    print("\n\n================================================\n")
    print("help - get help\n")
    print("register_person \{person_name\}\n")
    print("\n================================================\n\n")

def register_person(name):
    person_list = 0
    register = True
    try:
        person_list_file = open("data/person_list.hole", "r")
        person_list = person_list_file.readlines()
        for line in person_list:
            if line == "NAME=" + name:
                sure = input("Duplicate detected, are you sure? y/n")
                if(sure != "y"):
                    register = False
    except Exception as e:
        person_list_file = open("data/person_list.hole", "w").close()

    person_list_file = open("data/person_list.hole", "a")
    person_list_file.write("\n\nSTART\n")
    person_list_file.write("NAME=" + name)
    person_list_file.write("\nID=")
    person_list_file.write("\nBIRTH=")
    person_list_file.write("\nNATIONALITY=")
    person_list_file.write("\nRACE=")
    person_list_file.write("\nPHONE_NUMBERS=")
    person_list_file.write("\nWORST_FEAR=")
    person_list_file.write("END")
    person_list_file.close()
    print("\nSuccessfully registered new person " + name)


help()
while True:
    command = input("\n> ")
    
    if(command == "help"):
        help()

    if(command.split(" ")[0] == "register_person"):
        register_person(command.split(" ")[1])
