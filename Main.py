import sqlite3

def file_reader(filename):
	file = open(filename, "r")
	#contents = yaml.load(file) # this will change depending on file type
	#print(contents)
	print("Not done yet")

def user_input():
	print("Not done yet")


def add_transaction():
	# Connects to the database
	conn = sqlite3.connect("transactions.db")
	c = conn.cursor()

	print("Entering a transaction: \n")
	amount = input("Please enter the amount: ")
	cat = input("Under what category does this fall?")
	date = input("What date did this occur?")
	i_or_out = input("Was this an inflow or outflow?")
	c.execute("INSERT INTO transactions (amount, category, date, inflow_or_outflow) VALUES (?,?,?,?);", (amount, cat, date, i_or_out))

	# Commits the changes
	conn.commit()
	c.close()

def main():
	add_transaction()
	#filename = input("Enter filename: ")
	filename = "Pratice data.yaml"
	#file_reader(filename)
	print("Not done yet")

main()