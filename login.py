import MySQLdb
db = MySQLdb.connect(host="localhost",user="root",passwd="noweed",db="Users")
cur = db.cursor()
username="sravan"
passwd="sravan"
query = """select * from creds where username = %s and password = %s"""
cur.execute(query,(username,passwd))
results = cur.fetchall()
print(cur.arraysize)
for result in results:
	print(result)