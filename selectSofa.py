import sqlite3


def query_db(super_category):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('model_info.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute the SQL query
    c.execute("SELECT * FROM model_info WHERE superCategory = ?", (super_category,))

    # Fetch all the rows returned by the query
    rows = c.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the connection
    conn.close()


# Query the database for entries where the superCategory is 'Sofa'
query_db('Sofa')
