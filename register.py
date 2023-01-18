import sqlite3 as sq
from getpass import  getpass
from hashlib import sha256
def register():
    print("**** Register ****")
    conn = sq.connect("insatdb.dbs")
    c = conn.cursor()
    c.execute("""create table if not exists insat (id integer primary key autoincrement
    , nom text , prenom text ,password text)
    
    """)
 
    prenom = input("enter your first name : ")
    nom = input("enter your Last Name : ")
    pwd = getpass("enter your password : ")
    c.execute("insert into insat (nom,prenom,password) values (?,?,?) ",
    (nom,prenom,sha256(pwd.encode()).hexdigest()))
    conn.commit()
    conn.close()
