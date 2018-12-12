import adodbapi


database = "db1.mdb"
constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'
tablename = "address"

# Connect to database.
conn = adodbapi.connect(constr)

# Create cursor.
cur = conn.cursor()

# Get all data.
sql = "select * from %s" % tablename
cur.execute(sql)

# Show result.
result = cur.fetchall()
for item in result:
    print(item)

# Close connection.
cur.close()
conn.close()
