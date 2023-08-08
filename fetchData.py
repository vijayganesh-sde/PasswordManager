import dbconfig
from rich.table import Table
from addEntry import computeHexKey
import aes256
def fetchData(mp,secret,name):
  conn=dbconfig.dbconfig()
  curr=conn.cursor()
  query="SELECT * FROM passwords HAVING site_name=%s"
  curr.execute(query,(name,))
  data = curr.fetchall()
  if len(data)==0:
    print("NO password entries to show!!")
  else:
    table=Table(title='results')
    table.add_column('site_name')
    table.add_column('site_url')
    table.add_column('username')
    table.add_column('email')
    table.add_column('password')
    for i in data:
      mk=computeHexKey(mp,secret)
      decrypted=aes256.decrypt(key=mk,source=i[4],keyType="bytes")
      table.add_row(i[0],i[1],i[2],i[3],decrypted.decode())
  return table
  
  