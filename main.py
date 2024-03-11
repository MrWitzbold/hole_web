def help():
    print("\ n\n================================================\n")
    print("help - get help")
    print("register_person {person_name} - register new person")
    print("search_person {name or part of name} - search in people database")
    print("\n================================================\n\n")

def register_person(name):
    person_list = 0
    register = True
    try:
        person_list_file = open("data/person_list.hole", "r")
        person_list = person_list_file.readlines()
        for line in person_list:
            if "NAME=" + name in line:
                sure = input("Duplicate detected, are you sure? y/n")
                if(sure != "y"):
                    register = False
    except Exception as e:
        person_list_file = open("data/person_list.hole", "w").close()
    if register == True:
        person_list_file = open("data/person_list.hole", "a")
        person_list_file.write("\n\nSTART\n")
        person_list_file.write("NAME=" + name)
        person_list_file.write("\nID=")
        person_list_file.write("\nBIRTH=")
        person_list_file.write("\nNATIONALITY=")
        person_list_file.write("\nRACE=")
        person_list_file.write("\nPHONE_NUMBERS=")
        person_list_file.write("\nWORST_FEAR=")
        person_list_file.write("\nEND")
        person_list_file.close()
        print("\nSuccessfully registered new person " + name)
    else:
        print("Didn't register any new people.")

def search_people(name):
    print_line = False
    person_list = open("data/person_list.hole", "r").readlines()
    for line in person_list:
        if ("NAME=" in line) and (name in line):
            print_line = True
        if "END" in line:
            print_line = False
            print("\n\n")

        if print_line == True:
            print(line)
            

#def delete_person(name)
 #   person_list_file = open("data/person_list.hole", "r")
  #  person_list = person_list_file.readlines()
    #for line in person_list:
    #    if()


help()
while True:
    command = input("\n> ")
    arg1 = ""
    arg2 = ""
    try:
        arg1 = command.split(" ")[0]
        arg2 = command.split(" ")[1]
    except Exception as e:
        print("")
    
    if(command == "help"):
        help()

    if(arg1 == "register_person"):
        register_person(arg2)

    if(arg1 == "search_person"):
        search_people(arg2)







