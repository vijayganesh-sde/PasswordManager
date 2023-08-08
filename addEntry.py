import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import aes256
import dbconfig
import base64
def computeHexKey(p,s):
  enp=p.encode()
  salt=s.encode()
  mk=PBKDF2(enp,salt,32,count=1000000,hmac_hash_module=SHA512)
  return str(mk)
def addEntry(uname,url,sitename,email,mp,secret):
  pwd=getpass.getpass("Enter password: ")
  mkey=computeHexKey(mp,secret)
  encrypt_pass=aes256.encrypt(key=mkey,source=pwd,keyType="bytes")
  conn=dbconfig.dbconfig()
  curr=conn.cursor()
  try:
    query="insert into passwords values(%s,%s,%s,%s,%s)"
    curr.execute(query,(sitename,url,uname,email,encrypt_pass))
    conn.commit()
    print ("Password added successfully")
  except Exception as e:
    print("Error in adding password")