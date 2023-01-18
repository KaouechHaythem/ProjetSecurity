import sqlite3 as sq
conn=sq.connect("insatdb.dbs")
c=conn.cursor()
c.execute("""create table if not exists insat(
id integer primary key autoincrement , nom text , prenom text

)""")
conn.close()