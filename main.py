import sqlite3

print("=========================")
print("         Plants          ")
print("=========================")
print("Choose what to do?")
print("1. Search by name")
print("2. Search by month")
print("3. Input new flower data")
print("4. Prepare database")
print("5. Populate the database with input.csv")
print("6. Dump the database")
print("Your choice:", end='')
choice = input()
connection = sqlite3.connect("plants.db")
cursor = connection.cursor()
if (choice == '1'):
    print("name to search:", end='')
    name_to_search = input()
    cursor.execute(f'''
                   SELECT * FROM plants
                   WHERE plant = "{name_to_search}"
                   ''')
    rows = cursor.fetchall()
    print(rows)
elif (choice == '2'):
    print("TODO")
elif (choice == '3'):
    print("TODO")
elif (choice == '4'):
    print("Preparing...")
    connection.execute("BEGIN")
    cursor.execute("CREATE TABLE plants(plant text, Sowing_From int, Sowing_To int, Harvest_From int, Harvest_To int, Notes text)")
    connection.commit()
    print("Prepared successfully!")
elif (choice == '5'):
    print("TODO")
    connection.execute("BEGIN")
    cursor.execute('''
    INSERT INTO plants (plant, Sowing_From, Sowing_To, Harvest_From, Harvest_To, Notes)
    VALUES('Carrot', 4, 6, 7, 10, 'Prefers light, sandy soil');
                   ''')
    connection.commit()
elif (choice == '6'):
    print("Dumping...")
    cursor.execute("SELECT * FROM plants")
    rows = cursor.fetchall()
    print(rows)

else:
    print("Wrong choice. Exiting!")
connection.close()
