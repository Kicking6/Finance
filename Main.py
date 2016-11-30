import sqlite3
import easygui as EG

def file_reader(filename):
	file = open(filename, "r")
	#contents = yaml.load(file) # this will change depending on file type
	#print(contents)
	print("Not done yet")

def user_input():
	print("Not done yet")


def add_transaction():
	msg = "Please enter the details of this transaction"
	title = "Rory's Financerifier"
	fields = ["Amount", "Category", "Date", "Inflow or Outflow?"]


	transactionValues = EG.multenterbox(msg, title, fields)

	# Connects to the database
	conn = sqlite3.connect("transactions.db")
	c = conn.cursor()
	c.execute("INSERT INTO transactions (amount, category, date, inflow_or_outflow) VALUES (?,?,?,?);", tuple(transactionValues))

	# Commits the changes
	conn.commit()
	c.close()


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

# Draws the GUI for the account summary.
# Maybe you want to get the account summary first? Maybe this calls that function? Just a placeholder for now.
def account_summary_GUI():
	print("Not dont yet")



def main():
	drawGui()
	# add_transaction()
	#filename = input("Enter filename: ")
	filename = "Pratice data.yaml"
	#file_reader(filename)
	print("Not done yet")

main()