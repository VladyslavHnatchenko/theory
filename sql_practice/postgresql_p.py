import psycopg2

conn = psycopg2.connect(dbname='my_database', user='username')
cursor = conn.cursor()

# Run query.
cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()

# Close connection.
cursor.close()
conn.close()
