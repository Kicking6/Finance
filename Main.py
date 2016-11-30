import sqlite3

def file_reader(filename):
	file = open(filename, "r")
	contents = yaml.load(file) # this will change depending on file type
	print(contents)
	print("Not done yet")
	
def user_input():
	print("Not done yet")
	
def main():
	#filename = input("Enter filename: ")
	filename = "Pratice data.yaml"
	file_reader(filename)
	print("Not done yet")

main()