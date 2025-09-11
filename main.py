import sqlite3

print("=========================")
print("         Plants          ")
print("=========================")
print("Choose what to do?")
print("1. Search by name")
print("2. Search by month")
print("3. Input new flower data")
print("4. Prepare database")
print("Your choice:", end='')
choice = input()
if (choice == '1'):
    print("Search bla bla")
elif (choice == '2'):
    print("Search month bla bla")
elif (choice == '3'):
    print("Input new plant")
elif (choice == '4'):
    print("Preparing...")
    connection = sqlite3.connect("plants.db")
    cursor = connection.cursor()
    connection.execute("BEGIN")
    cursor.execute("CREATE TABLE plants(one text, two int)")
    connection.commit()
    print("Prepared successfully!")
else:
    print("Wrong choice. Exiting!")
