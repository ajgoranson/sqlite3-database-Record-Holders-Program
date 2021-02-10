import sqlite3


db = 'record_db.sqlite'

sql_error = 'SQL Error please try again'

class RecordError(Exception):
    pass

def create_table():
    try:

        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS juggleing (Name text, Country text, NumberOfCatches int)')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()


def insert_example_data():
    try:

        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO juggleing values ("Janne Mustonen", "Finland", 98)')
            conn.execute('INSERT INTO juggleing values ("Ian Stewart", "Canada", 94)')
            conn.execute('INSERT INTO juggleing values ("Aaron Gregg", "Canada", 88)')
            conn.execute('INSERT INTO juggleing values ("Chad Taylor", "USA", 78)')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()
#insert_example_data() #commented out so it would not repete the duplicate data

def delete_record(delete_record_holder):
    input('Whose record would you like to delete? ')
    
    delete_record_holder = delete_record_holder.title()

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE from juggleing WHERE Name = ?', (delete_record_holder, ))
    except sqlite3.Error as e:
        print(sql_error + e) 
    conn.close()      

def add_new_record(new_name, new_country, new_record):

    new_name = new_name.title().strip()
    new_country = new_country.title().strip()

    if new_name == '':
        raise RecordError('Please enter a name')
    
    if new_country == '':
        raise RecordError('Please enter a country')
    
    if new_record == None:
        raise RecordError('Please enter the new record')

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO juggleing VALUES (?, ?, ?)', (new_name, new_country, new_record))
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()
    


def update_record(record_holder, new_record):

    record_holder = record_holder.title().strip()

    if record_holder == '':
        raise RecordError('Please enter the name')

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('UPDATE juggleing SET NumberOfCatches = ? WHERE name = ?', (new_record, record_holder) )
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def search_for_record(record_holder):

    record_holder = record_holder.title().strip()

    if record_holder == '':
        raise RecordError('Please enter a record holders name')

    try:

        conn = sqlite3.connect(db)
        results = conn.execute('SELECT * FROM products WHERE name like ?', (record_holder, ))
        record_found = results.fetchone()
        if record_found:
            print('Here is the record: ')
            print(record_found)
        else:
            print('Record not found')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def view_all_data():
    try:

        with sqlite3.connect(db) as conn:
            results = conn.execute('SELECT * from juggleing')
            print('Here is all of the records')

            for row in results:
                print(row)
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def main():
    create_table()

    print('Welcome to the chainsaw record holders database')

    while True:

        selection = int(input('Please select from one of the following options \n'
        + ' 1 = View all data \n'
        + ' 2 = Add new record \n'
        + ' 3 = Delete a record \n'
        + ' 4 = Search for a record \n'
        + ' 5 = Update a record \n'
        + ' Press any other number to quit: '))

        if selection == 1:
            view_all_data()
        elif selection == 2:
            add_new_record(input('Please enter the name of the record holder '), input('Please Enter the Country of the record holder '), int(input('Please enter the number of chainsaws juggled')))
        elif selection == 3:
            delete_record(input('Whose record would you like to delete? '))
        elif selection == 4:
            search_for_record(input('Please enter the name of the record you would like to view: '))
        elif selection == 5:
            update_record(input('Please enter the name of the record holder you would like to update: '),  new_record = int(input('Please enter the new amount of catches: ')))
        else:
            exit()

if __name__ == '__main__':
    main()