from addEntry import addEntry
import hashlib
from dbconfig import dbconfig
import fetchData
from rich.console import Console
print("Welcome to Password Manager System!!!")
print("Do you want to fetch(type 1) or add a Password(type 2): ")
inp=int(input())
def validate_admin():
  mp=input("Enter the master Password: ")
  hash_mp=hashlib.sha256(mp.encode()).hexdigest()
  conn=dbconfig()
  curr=conn.cursor()
  curr.execute("select * from admin")
  data=curr.fetchall()
  if data[0][0]!=hash_mp:
    print("Wrong Attempt!!")
    return ""
  print("Admin Accepeted")
  return mp
if inp==2:
  mp=validate_admin()
  if mp:
    uname=input("Enter username: ")
    url=input("Enter the website url: ")
    sitename=input("Enter the website name: ")
    email=input("Enter the mailId: ")
    addEntry(uname,url,sitename,email,mp,"lilolally")
else:
  mp=validate_admin()
  if mp:
    sitename=input("Enter the site name: ")
    data=fetchData.fetchData(mp,"lilolally",sitename)
    console=Console()
    console.print(data)