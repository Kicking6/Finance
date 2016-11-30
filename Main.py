import sqlite3
import easygui

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
	print("Not done yet")

# Creates the Gui. what else is there to say?
def drawGui():
	mainMenuChoices = ["View Account Summary", "Add a Transaction"]
	title = "Rory's Financerifier"
	msg = "Welcome to the main menu. What would you like to do?"
	# This returns the index of what the user chose. eg, 0 for acc summary, 1 for adding transaction
	mainMenuNavChoice = EG.indexbox(msg, title, mainMenuChoices)
	if mainMenuNavChoice == 0:
		account_summary_GUI()
	elif mainMenuNavChoice == 1:
		add_transaction()
	else:
		pass

# Creates a GUI and allows someone to add a transaction
#TODO: Data validation. Make sure people aren't entering bad things they shouldn't.
def add_transaction():
	msg = "Please enter the details of this transaction"
	title = "Rory's Financerifier"
	fields = ["Amount", "Category", "Date", "Inflow or Outflow?"]

	transactionValues = EG.multenterbox(msg, title, fields)

	# Connects to the database
	conn = sqlite3.connect("transactions.db")
	c = conn.cursor()
	c.execute("INSERT INTO transactions (amount, category, date, inflow_or_outflow) VALUES (?,?,?,?);",
			  tuple(transactionValues))

	# Commits the changes
	conn.commit()
	c.close()


# Draws the GUI for the account summary.
# Maybe you want to get the account summary first? Maybe this calls that function? Just a placeholder for now.
def account_summary_GUI():
	print("Not dont yet")

def main():
    main_menu()
    #filename = input("Enter filename: ")
    filename = "Pratice data.yaml"
    file_reader(filename)
    print("Not done yet")

main()