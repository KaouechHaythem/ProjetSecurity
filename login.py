import sqlite3 as sq
from getpass import  getpass
from hashlib import sha256
def login(prenom , password):
    
    conn=sq.connect("insatdb.dbs")
    c=conn.cursor()
    while True :
        prenom = input("Enter Your First Name : ")
        if (len(c.execute("select prenom from insat where (prenom)=(?)",(prenom,)).fetchall())>0) :
            pwd = sha256(getpass("enter your password : " ).encode()).hexdigest()
            if(c.execute("select password from insat where (password,prenom)=(?,?)",(pwd,prenom)).fetchone()):
                entity=c.execute("select nom,prenom from insat where (prenom,password) = (?,?)",(prenom,pwd)).fetchone()
                print(entity[1])
            else: 
                print("verify your password")

        else:
            print("Verify Your First Name") 
    conn.close()