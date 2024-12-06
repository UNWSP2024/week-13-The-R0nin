# Program #2 (3/4) phonebook
# From data on page #796 (not avalible, Use Cities DB)
# have the program allow user to read, update, and delete rows from the data base

import sqlite3
# Connection
connection = sqlite3.connect('#cities.db')
cursor = connection.cursor()
# table
cursor.execute('Create table cities (city_id integer, City_Name text, Population integer)')

cities_list = [
    (1,'Tokyo',38001000),
    (2,'Delhi',25703168),
    (3,'Shanghai',23740778),
    (4,'Sao Paulo',21066245),
    (5,'Mumbai',21042538),
    (6,'Mexico City',20998543),
    (7,'Beijing',20383994),
    (8,'Osaka',20237645),
    (9,'Cairo',18771769),
    (10,'New York',18593220),
    (11,'Dhaka',17598228),
    (12,'Karachi',16617644),
    (13,'Buenos Aires',15180176),
    (14,'Kolkata',14864919),
    (15,'Istanbul',14163989),
    (16,'Chongqing',13331579),
    (17,'Lagos',13122829),
    (18,'Manila',12946263),
    (19,'Rio de Janeiro',12902306),
    (20,'Guangzhou',12458130)]
# Display table
cursor.executemany("insert into cities values (?,?,?)", cities_list)
for row in cursor.execute('select * from cities'):
    print(row)
# Seperation
print("**************************")
# Choice functions
def update():
    city_input = input('Insert New City:')
    pop_input = input('Insert the population:')

    cursor.execute('SELECT city_id From cities')
    ID = cursor.fetchall()
    last_row = len(ID)
    ID_input = int(last_row) + 1 

    cursor.execute("insert into cities", (ID_input, city_input, pop_input))

def delete():
    delete = int(input('City to remove from db (By ID):'))
    cursor.execute("DELETE cities FROM city_id={delete}")

def end():
    print('OK')
# Choice Input
print('would you like to Update or Delete items from database')
print('If not just put done, reminder type in all lowercase')
choice = input(':')

if choice == 'update':
    update()
if choice == 'delete':
    delete()
if choice == 'done':
    end()
#End of program
connection.close()
