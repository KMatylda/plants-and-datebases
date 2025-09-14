import sqlite3
import csv

print("=========================")
print("         Plants          ")
print("=========================")
print("Choose what to do?")
print("1. Search by name")
print("2. Search by month")
print("3. Input new plant data")
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
    print("month to search:", end='')
    month_to_search = input()
    cursor.execute(f'''
                    SELECT * FROM plants
                    WHERE (Sowing_From  <= "{month_to_search}" AND Sowing_To  >= "{month_to_search}")
                    ''')
    rows_sowing = cursor.fetchall()
    for r in rows_sowing:
        print(f"{r[0]} sowing")

    cursor.execute(f'''
                    SELECT * FROM plants
                    WHERE (Harvest_From  <= "{month_to_search}" AND Harvest_To  >= "{month_to_search}")
                    ''')
    
    rows_harvest = cursor.fetchall()
    for r in rows_harvest:
        print(f"{r[0]} harvest")

    
elif (choice == '3'):
        print("plant:", end='')
        p = input()
        print("Sowing_From:", end='')
        sf = input()
        print("Sowing_To:", end='')
        st = input()
        print("Harvest_From:", end='')
        hf = input()
        print("Harvest_To:", end='')
        ht = input()
        print("Notes:", end='')
        n = input()
        connection.execute("BEGIN")
        cursor.execute(f'''
        INSERT INTO plants (plant, Sowing_From, Sowing_To, Harvest_From, Harvest_To, Notes)
        VALUES('{p}', {sf}, {st}, {hf}, {ht}, '{n}');
                   ''')
        connection.commit()
elif (choice == '4'):
    print("Preparing...")
    connection.execute("BEGIN")
    cursor.execute("CREATE TABLE plants(plant text, Sowing_From int, Sowing_To int, Harvest_From int, Harvest_To int, Notes text)")
    connection.commit()
    print("Prepared successfully!")
elif (choice == '5'):
    file = open('input.csv', mode ='r')
    rows = csv.reader(file)
    rows_list = list(rows)
    for row in rows_list[1:]:
        # Check if row has no elements
        if(len(row) == 0):
            continue

        # Check if row has elements that are empty (like empty strings: '')
        is_row_empty = False
        for item in row:
            if(len(item) == 0):
                is_row_empty = True     
        if is_row_empty:
            continue

        # Insert the values to database
        connection.execute("BEGIN")
        cursor.execute(f'''
        INSERT INTO plants (plant, Sowing_From, Sowing_To, Harvest_From, Harvest_To, Notes)
        VALUES('{row[0]}', {row[1]}, {row[2]}, {row[3]}, {row[4]}, '{row[5]}');
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
