import sqlite3

def file_reader(filename):
    file = open(filename, "r")
    contents = yaml.load(file) # this will change depending on file type
    print(contents)
    print("Not done yet")

#Basic menu where the user defines what they want to do in the program.
#The list of options needs to be expanded at a later date	
def main_menu():
    answer = True
    while answer:
        print("\n"
            "            Main Menu\n",
            "* " * 16, "\n",
            "1. View Account Summary \n",
            "2. Add a transaction \n",
            "3. \n",
            "4. Quit \n",
            "* " * 16
            )
        
        answer = int(input("Selection: "))
        print()
        
        if answer == 1:
            account_summary()
    
        elif answer == 2:
            add_transaction()
        
        elif answer == 4:
            answer = False
    
        elif answer != "":
            print("Not a valid answer, please select again.")

#This will return to the user a file and/ or readout (Not decided yet) of their account            
def account_summary():
    print("Not done yet!")

#This will add a transaction to the data base.   
#Will write to the file, date, cost, inflow/ outflow, category
def add_transaction():
    print("Not done yet!")
	
def main():
    print(123)
    main_menu()
    print(456)
    #filename = input("Enter filename: ")
    filename = "Pratice data.yaml"
    file_reader(filename)
    print("Not done yet")

main()