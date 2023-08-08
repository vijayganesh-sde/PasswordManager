from dbconfig import dbconfig
import getpass
import hashlib
def config():
  conn=dbconfig()
  curr=conn.cursor()
  try:
    query="create table passManager.admin(master_key text not null, secret_text text not null)"
    curr.execute(query)
    print("table created")
  except Exception as e:
    print("Table already exists")
  try:
    query="create table passManager.passwords(site_name text, site_url text not null, username text, email text not null, password text not null)"
    curr.execute(query)
    print("table created")
  except Exception as e:
    print("Table already exists")
  np=""
  while 1:
    np=getpass.getpass("enter passyy: ")
    repass=getpass.getpass("Retype: ")
    if np==repass:
      break
    print("TRy again")
  hash_pass=hashlib.sha256(np.encode()).hexdigest()
  secret="lilolally"
  ins_query="insert into admin values(%s,%s)"
  curr.execute(ins_query,(hash_pass,secret))
  conn.commit()
  print("master password inserted")
config()
    