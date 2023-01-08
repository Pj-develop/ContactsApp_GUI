import time
import os

name_list = ['PRIYANSHU JHA','HARJASPAL SINGH','AYUSHI BHUTANI','PRINCE']
contact_list = [9518474744,1234567890,7894561230,4567891230]

def Dlt():
    name=str(input("     Enter Name to be Deleted from the Database:    \n\t"))
    popping=name.upper()
    if popping in name_list:
        index = name_list.index(popping)
        time.sleep(2)
        print("{}: {} has been deleted from the Database".format(name_list[index],contact_list[index]))
        time.sleep(5)
        del name_list[index]
        del contact_list[index]
    else:
        os.system('cls')
        print("\n     --------------- No Such Name is Found in the Directory ---------------\n")
        time.sleep(0.25)
        os.system('cls')

print('''
 ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗████████╗     █████╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║        ██║       ███████║██████╔╝██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║        ██║       ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╗   ██║       ██║  ██║██║     ██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 --------------------->"Forget the Old ways to Save & Store Your Contacts Manually , One Stop Solution to Save Your Contacts" <------------------ )
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~) VERSION 2.O ( APLHA) (~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~) 
''')
while(True):
    print("\n     ---------------     1. Add a New Contact        ---------------\n")
    print("     ---------------     2. Delete a Contact         ---------------\n")
    print("     ---------------     3. Search a Contact         ---------------\n")
    print("     ---------------     4. Display all Contacts     ---------------\n")
    print("     ---------------     5. Extract Multiple Contacts     ----------\n")
    print("     ---------------     0. Exit                     ---------------\n")
    choice = input("Enter Your Choice: ")
    time.sleep(0.25)
    os.system('cls')
    if(choice == '1'):
        name = str(input("     Enter The Name    \n\t"))
        contact = int(input("     Enter Contact Number     \n\t"))
        name_list.append(name.upper())
        contact_list.append(contact)
        os.system('cls')
    elif(choice == '2'):
        Dlt()
        os.system('cls')

    elif(choice == '3'):
        print("\n     ---------------     1. Search by Name        ---------------\n")
        print("     ---------------     2. Search by Contact     ---------------\n")
        usr_choice = input("Enter Your Choice: ")
        time.sleep(0.25)
        os.system('cls')
        if(usr_choice == '1'):
            name = str(input("      Enter the Name of Contact You want to Search     \n\t"))
            name=name.upper()
            if(name in  name_list):
                index = name_list.index(name)
                os.system('cls')
                print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
                time.sleep(1)
                os.system('cls')
            else:
                os.system('cls')
                print("\n     --------------     Sorry, Name Not Found     ---------------\n")
                time.sleep(0.50)
                os.system('cls')
        elif(usr_choice == '2'):
            while True:
                contact = input("      Enter the Contact Number of Contact You want to Search     \n\t")
                if contact.isnumeric():
                    contact=int(contact)
                    break
                else:
                    os.system('cls')
                    print("\n     --------------     Invalid Contact Number Entered     ---------------\n")
                    time.sleep(0.50)
                    os.system('cls')
            
            if(contact in  contact_list):
                index = contact_list.index(contact)
                os.system('cls')
                print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
                time.sleep(3)
                os.system('cls')
            else:
                os.system('cls')
                print("\n     --------------     Sorry, Contact Not Found     ---------------\n")
                time.sleep(0.50)
                os.system('cls')
        else:
            os.system('cls')
            print("\n     ---------------     INVALID  CHOICE     ---------------\n")
            time.sleep(1)
            os.system('cls')
    elif(choice == '4'):
        print("\n     ---------------     Contacts     ----------------\n")
        for index in range(0, len(name_list)):
            print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
            time.sleep(1)
        time.sleep(2)
    elif(choice == '5'):
        print("\n     -----     Type 'exit' to quit entering names     -----\n")
        n_name = ""
        new_name_list = []
        new_contact_list = []
        while(n_name != "EXIT"):
            n_name = str(input())
            n_name=n_name.upper()
            if(n_name in  name_list):
                index = name_list.index(n_name)
                new_name_list.append(name_list[index])
                new_contact_list.append(contact_list[index])
        for index in range(0, len(new_name_list)):
            print("---     ", new_name_list[index], " : ", new_contact_list[index], "     ---\n")
            time.sleep(0.5)
    elif(choice == '0'):
        print("\n     ---------------     Thanks For Using Our Software!!!     ---------------\n")
        break
    else:
        os.system('cls')
        print("\n     ---------------     INVALID  CHOICE     ---------------\n")
        time.sleep(0.25)
        os.system('cls')
        print("\n     ---------------     RESTARTING.........     ---------------\n")
        time.sleep(0.25)
        os.system('cls')